#!/usr/bin/env python3
"""PHONE VOICE (runs on the Pi, reached from the phone over Tailscale HTTPS). Everything here answers ONLY to the phone that is talking: the reply audio goes back to that phone,
nothing is played on the home speakers and nothing is shown on the Pi screen.
Phase 1: always-listening wake-word logger. The phone page streams 16 kHz audio; every wake-word candidate is logged with a short clip so you can mark it good / false / missed and tune the threshold.
Phase 2: conversation. After the wake word it records one utterance, transcribes (OpenAI), answers (OpenAI chat), speaks (ElevenLabs), then stays open for follow-ups
         (10 s of quiet, 20 s if its last reply was a question; "that's all" / "goodbye" ends it; a soft tone marks the close).
Phase 3 (voice ID) plugs into speaker_check() below; until a voiceprint model is installed everything is treated as the owner and logged as "unverified".
Audio is kept only as short clips around wake-word candidates (never continuous). Stdlib + numpy; openwakeword/onnxruntime for the real detector.
  python3 phone_voice.py [port=8099]"""
import urllib.parse, http.server, io, json, math, os, re, socketserver, struct, sys, threading, time, urllib.request, uuid, wave
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voiceid

DATA = os.environ.get("VOICE_DIR", os.path.join(os.path.expanduser("~"), "voice-data"))
CLIPS = os.path.join(DATA, "clips")
REPLIES = os.path.join(DATA, "replies")
for d in (DATA, CLIPS, REPLIES):
    os.makedirs(d, exist_ok=True)
SR = 16000
FRAME = 1280                                  # 80 ms, what the wake-word model wants
LOG_MIN = 0.25                                # log every candidate this strong (so thresholds can be tuned from real data)
RING_SECS = 8
KEEP_DAYS = 21
HERE = os.path.dirname(os.path.abspath(__file__))
MOCK = os.environ.get("VOICE_MOCK") == "1"
LOCK = threading.RLock()


def now(): return time.time()
def jl_append(name, obj):
    with open(os.path.join(DATA, name), "a") as fh: fh.write(json.dumps(obj) + "\n")
def trace(sid, kind, **kw):
    """One line per thing that happened, so a conversation can be replayed afterwards (see /report)."""
    try:
        with LOCK: jl_append("trace.jsonl", dict(t=round(now(), 3), sid=sid, kind=kind, **kw))
    except Exception: pass
def jl_read(name):
    out = []
    try:
        for l in open(os.path.join(DATA, name)):
            try: out.append(json.loads(l))
            except ValueError: pass
    except OSError: pass
    return out


# ------------------------------------------------------------------ settings
DEFAULTS = {"threshold": 0.6, "paused": False, "private": False, "models": ["hey_jarvis"], "follow_quiet": 25.0, "follow_question": 40.0, "voice_id": "Brian", "max_utter": 20.0, "speech_speed": 1.0, "max_tokens": 150, "tts_model": "eleven_flash_v2_5", "silence_end": 1.3, "barge_in": True, "stream": True, "voice_threshold": 3.0, "ask_unknown": False}
def load_settings():
    s = dict(DEFAULTS)
    try: s.update(json.load(open(os.path.join(DATA, "settings.json"))))
    except Exception: pass
    return s
SET = load_settings()
def save_settings():
    json.dump(SET, open(os.path.join(DATA, "settings.json"), "w"))


def load_keys():
    k = {}
    try:
        for l in open(os.path.join(DATA, "keys.env")):
            if "=" in l and not l.startswith("#"):
                a, b = l.strip().split("=", 1); k[a] = b
    except OSError: pass
    return k


# ------------------------------------------------------------------ wake-word detector
class FakeDetector:
    """Test stand-in: scores the strength of a 1 kHz tone in the frame. Used only when VOICE_MOCK=1."""
    name = "fake"
    def predict(self, frame):
        x = frame.astype(np.float32) / 32768.0
        t = np.arange(len(x)) / SR
        c = abs(np.dot(x, np.exp(-2j * np.pi * 1000 * t))) / (len(x) / 2.0)
        return {"fake": float(min(1.0, c * 2.0))}


class OWWDetector:
    name = "openwakeword"
    def __init__(self, models):
        from openwakeword.model import Model
        try:
            self.m = Model(wakeword_models=models, inference_framework="onnx")
        except Exception:
            import openwakeword
            openwakeword.utils.download_models(models)
            self.m = Model(wakeword_models=models, inference_framework="onnx")
    def predict(self, frame):
        return {k: float(v) for k, v in self.m.predict(frame).items()}
    def reset(self):
        try: self.m.reset()
        except Exception: pass


def make_detector():
    if MOCK:
        return FakeDetector()
    try:
        return OWWDetector(SET["models"])
    except Exception as e:
        print("wake-word model not available:", e, flush=True)
        return None


# ------------------------------------------------------------------ audio helpers
def wav_bytes(pcm):
    b = io.BytesIO()
    with wave.open(b, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.astype("<i2").tobytes())
    return b.getvalue()


def rms(x):
    return float(np.sqrt(np.mean(np.square(x.astype(np.float32))))) if len(x) else 0.0


# ------------------------------------------------------------------ OpenAI / ElevenLabs (urllib only)
TL = threading.local()
def timed(name):
    def deco(fn):
        def w(*a, **k):
            t0 = time.time()
            try: return fn(*a, **k)
            finally:
                if not hasattr(TL, "t"): TL.t = {}
                TL.t[name] = round(time.time() - t0, 2)
        return w
    return deco
def times_reset(): TL.t = {}
def times_get(): return dict(getattr(TL, "t", {}))


def load_pron():
    p = {"Kylar": "Kyler"}
    try: p.update(json.load(open(os.path.join(DATA, "pronunciations.json"))))
    except Exception: pass
    return p
def apply_pron(text):
    for k, v in load_pron().items():
        if k: text = re.sub(r"\b%s\b" % re.escape(k), v, text, flags=re.I)
    return text


def _post(url, headers, body, timeout=60):
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    return urllib.request.urlopen(req, timeout=timeout).read()


@timed("stt")
def stt(pcm):
    if MOCK: return os.environ.get("VOICE_MOCK_TEXT", "what time is it")
    key = load_keys().get("OPENAI_API_KEY")
    if not key: raise RuntimeError("no OPENAI_API_KEY in %s/keys.env" % DATA)
    boundary = uuid.uuid4().hex
    parts = []
    def field(n, v): parts.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n" % (boundary, n, v)).encode())
    field("model", "gpt-4o-mini-transcribe"); field("language", "en")
    parts.append(("--%s\r\nContent-Disposition: form-data; name=\"file\"; filename=\"u.wav\"\r\nContent-Type: audio/wav\r\n\r\n" % boundary).encode() + wav_bytes(pcm) + b"\r\n")
    parts.append(("--%s--\r\n" % boundary).encode())
    r = _post("https://api.openai.com/v1/audio/transcriptions", {"Authorization": "Bearer " + key, "Content-Type": "multipart/form-data; boundary=" + boundary}, b"".join(parts))
    return (json.loads(r).get("text") or "").strip()


def sniff_audio(b):
    """Guess the audio type from the first bytes: returns (extension, mime)."""
    if b[:4] == b"RIFF": return "wav", "audio/wav"
    if b[4:8] == b"ftyp": return "m4a", "audio/mp4"
    if b[:3] == b"ID3" or b[:2] in (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2"): return "mp3", "audio/mpeg"
    if b[:4] == b"caff": return "caf", "audio/x-caf"
    if b[:4] == b"OggS": return "ogg", "audio/ogg"
    return "m4a", "audio/mp4"


@timed("stt")
def stt_file(data):
    if MOCK: return os.environ.get("VOICE_MOCK_TEXT", "what time is it")
    key = load_keys().get("OPENAI_API_KEY")
    if not key: raise RuntimeError("no OPENAI_API_KEY in %s/keys.env" % DATA)
    ext, mime = sniff_audio(data)
    boundary = uuid.uuid4().hex; parts = []
    def field(n, v): parts.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n" % (boundary, n, v)).encode())
    field("model", "gpt-4o-mini-transcribe"); field("language", "en")
    parts.append(("--%s\r\nContent-Disposition: form-data; name=\"file\"; filename=\"u.%s\"\r\nContent-Type: %s\r\n\r\n" % (boundary, ext, mime)).encode() + data + b"\r\n")
    parts.append(("--%s--\r\n" % boundary).encode())
    r = _post("https://api.openai.com/v1/audio/transcriptions", {"Authorization": "Bearer " + key, "Content-Type": "multipart/form-data; boundary=" + boundary}, b"".join(parts))
    return (json.loads(r).get("text") or "").strip()


def audio_from_body(ctype, raw):
    """The Shortcut may send the recording as a raw file or as a multipart form. Return the audio bytes."""
    m = re.search(r"boundary=([^;]+)", ctype or "")
    if m and "multipart" in (ctype or "").lower():
        bd = ("--" + m.group(1).strip('"')).encode()
        for part in raw.split(bd):
            if b"filename=" in part[:400] and b"\r\n\r\n" in part:
                body = part.split(b"\r\n\r\n", 1)[1]
                return body[:-2] if body.endswith(b"\r\n") else body
    return raw


def _read(path, limit):
    try: return open(os.path.expanduser(path), encoding="utf-8", errors="ignore").read().strip()[:limit]
    except OSError: return ""


TOPICS = [
    ("kalshi-ai", r"kalshi|bet|market|bitcoin|btc|trade|trading|strategy"),
    ("pi-home-assistant", r"\bpi\b|home assistant|tailscale|router|wifi|wi-fi|jarvis|voice|hub|screen"),
    ("amazon-kdp", r"kdp|amazon|book|publish"),
    ("truck-project", r"truck|tacoma|vehicle|car\b|engine|tires?|lift|parts?"),
    ("family", r"wife|girlfriend|kids?|son|daughter|mom|dad|family|birthday|dinner"),
    ("business", r"business|invoice|client|customer|sales|revenue|llc"),
    ("todo", r"to-?do|remind|need to|don.t forget|deadline|by (monday|tuesday|wednesday|thursday|friday|saturday|sunday|tomorrow)"),
]


def route_topic(text):
    for name, rx in TOPICS:
        if re.search(rx, text, re.I): return name
    return "todo"


def _read(path, limit):
    try: return open(os.path.expanduser(path), encoding="utf-8", errors="ignore").read().strip()[:limit]
    except OSError: return ""


def prompt_text():
    base = _read(os.path.join(DATA, "prompt.txt"), 4000) or (
        "You are Jarvis, the Lovelady family's home assistant, talking to the owner (Kylar) through his phone and earbuds, often while driving. Be blunt and honest, say when you do not know, "
        "keep answers short enough to listen to (one to three sentences unless he asks for more), and ask a short question back only when you really need the answer.")
    extra = ""
    repo = os.path.expanduser("~/starship/memory")
    mem = ""
    try:
        for root, dirs, files in os.walk(repo):
            dirs[:] = sorted(d for d in dirs if d != "inbox")
            for f in sorted(files):
                if f.endswith(".md") and f not in ("README.md", "_archive.md"):
                    pth = os.path.join(root, f)
                    mem += "\n## %s\n%s\n" % (os.path.relpath(pth, repo), _read(pth, 4500))
    except OSError: mem = ""
    if not mem.strip(): mem = _read("~/starship/BUILD_MEMORY.md", 5000)
    if mem.strip(): extra += "\n\nShared memory notes (written with Claude, the coding assistant; trust as background, they may be slightly out of date):" + mem[:18000]
    mine = ""
    try:
        for f in sorted(os.listdir(os.path.join(DATA, "memory"))):
            mine += "\n[%s]\n%s\n" % (f, _read(os.path.join(DATA, "memory", f), 2000))
    except OSError: pass
    if mine.strip(): extra += "\n\nThings Kylar told you to remember (newest last):" + mine[:6000]
    who = getattr(TL, "who", None)
    if who and who != "owner": extra += "\n\nThe person talking right now is: %s%s. Greet them by name if it fits; only Kylar can change settings or notes." % (who, " (voice not recognized, a guest)" if who == "unknown" else "")
    return base + extra


@timed("llm")
def chat(history):
    if MOCK: return "It is a mock reply. Anything else?"
    key = load_keys().get("OPENAI_API_KEY")
    body = json.dumps({"model": "gpt-4o-mini", "messages": [{"role": "system", "content": prompt_text()}] + history[-12:], "max_tokens": int(SET.get("max_tokens", 150))}).encode()
    r = _post("https://api.openai.com/v1/chat/completions", {"Authorization": "Bearer " + key, "Content-Type": "application/json"}, body)
    return json.loads(r)["choices"][0]["message"]["content"].strip()


def chat_stream(history):
    """Yield the answer in pieces as OpenAI writes it, so speech can start before the whole answer exists."""
    if MOCK:
        for w in os.environ.get("VOICE_MOCK_REPLY", "It is a mock reply. It has two sentences. Anything else?").split(" "): yield w + " "
        return
    key = load_keys().get("OPENAI_API_KEY")
    body = json.dumps({"model": "gpt-4o-mini", "messages": [{"role": "system", "content": prompt_text()}] + history[-12:], "max_tokens": int(SET.get("max_tokens", 150)), "stream": True}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=body, headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        for line in r:
            line = line.decode("utf-8", "ignore").strip()
            if not line.startswith("data:"): continue
            d = line[5:].strip()
            if d == "[DONE]": break
            try: piece = json.loads(d)["choices"][0]["delta"].get("content") or ""
            except (ValueError, KeyError, IndexError): continue
            if piece: yield piece


SENT_END = re.compile(r"(?<=[.!?])\s+")
def sentences(pieces, first_min=14, min_len=40):
    """Group streamed text into speakable sentences. The first one goes out as early as possible."""
    buf = ""; n = 0
    for p in pieces:
        buf += p
        while True:
            m = SENT_END.search(buf, first_min if n == 0 else min_len)
            if not m: break
            out, buf = buf[:m.start() + 1].strip(), buf[m.end():]
            if out: n += 1; yield out
    if buf.strip(): yield buf.strip()


@timed("tts")
def tts(text, path):
    if MOCK:
        pcm = (np.sin(2 * np.pi * 440 * np.arange(SR // 4) / SR) * 3000).astype("<i2")
        open(path, "wb").write(wav_bytes(pcm)); return "audio/wav"
    k = load_keys(); key = k.get("ELEVENLABS_API_KEY"); vid = k.get("ELEVENLABS_VOICE_ID")
    if not key or not vid: raise RuntimeError("no ELEVENLABS_API_KEY / ELEVENLABS_VOICE_ID in %s/keys.env" % DATA)
    body = json.dumps({"text": apply_pron(text), "model_id": SET.get("tts_model", "eleven_flash_v2_5"), "voice_settings": {"speed": max(0.7, min(1.2, float(SET.get("speech_speed", 1.0))))}}).encode()
    audio = _post("https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=mp3_44100_64&optimize_streaming_latency=3" % vid, {"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"}, body)
    open(path, "wb").write(audio); return "audio/mpeg"


_VB = None
def voicebook():
    global _VB
    if _VB is None: _VB = voiceid.VoiceBook(os.path.join(DATA, "voiceid", "voices.json"))
    return _VB


def speaker_check(pcm):
    """Returns (who, distance). who is a name, 'unknown' (voices enrolled but nobody matches), or 'owner' (no voices enrolled yet: treated as Kylar)."""
    vb = voicebook()
    if not vb.v: return ("owner", None)
    name, d, rank = vb.identify(pcm)
    if name is None: return ("owner", None)
    if d <= float(SET.get("voice_threshold", 3.0)): return (name, round(d, 2))
    return ("unknown", round(d, 2))


def speaker_level(who):
    if who == "owner": return "owner"
    if who == "unknown": return "guest"
    return voicebook().v.get(who, {}).get("level", "guest")


END_RE = re.compile(r"\b(that'?s all|that is all|goodbye|good bye|never ?mind|stop listening|thanks,? that'?s it|we'?re done)\b", re.I)


# ------------------------------------------------------------------ the session: one per phone page
class Session:
    def __init__(self, sid):
        self.sid = sid; self.det = None; self.ring = np.zeros(0, dtype=np.int16); self.buf = np.zeros(0, dtype=np.int16)
        self.hist = []; self.state = "idle"; self.t_state = now(); self.floor = 300.0
        self.ep = None; self.pending = []; self.scores = []; self.heard = 0.0; self.started = now(); self.last_seen = now()
        self.utt = []; self.speech_t = None; self.last_voice = now(); self.hold_until = 0.0; self.follow_for = 10.0
        self.ew = None; self.discard_until = 0.0; self.gen = 0; self.ask_pcm = None

    def det_ok(self):
        if self.det is None: self.det = DET
        return self.det is not None

    def set_state(self, s, why=""):
        if s != self.state: trace(self.sid, "state", frm=self.state, to=s, why=why)
        self.state = s; self.t_state = now()

    # ---- main entry: raw int16 PCM from the phone
    def feed(self, pcm):
        self.last_seen = now(); acts = []
        if SET["paused"]:
            return acts
        self.heard += len(pcm) / SR
        self.ring = np.concatenate([self.ring, pcm])[-RING_SECS * SR:]
        self.buf = np.concatenate([self.buf, pcm])
        while len(self.buf) >= FRAME:
            fr, self.buf = self.buf[:FRAME], self.buf[FRAME:]
            self.frame(fr, acts)
        return acts

    def frame(self, fr, acts):
        r = rms(fr); t = now()
        if self.state == "idle":
            if r < self.floor * 2: self.floor = 0.98 * self.floor + 0.02 * max(r, 50.0)
            self.wake(fr, acts)
        elif self.state == "speaking":
            if SET.get("barge_in", True) and self.det_ok():
                sc = self.det.predict(fr); s_ = max(sc.values()) if sc else 0.0
                if s_ >= SET["threshold"] and t - self.t_state > 0.8:
                    self.barge(acts, round(s_, 3)); return
            if (t >= self.hold_until and self.ew == "played") or t - self.t_state > 90:
                self.begin_follow(acts)
        elif self.state in ("listening", "follow"):
            self.listen(fr, r, acts)

    # ---- wake word
    def wake(self, fr, acts):
        if not self.det_ok(): return
        sc = self.det.predict(fr); name, s = max(sc.items(), key=lambda kv: kv[1]) if sc else ("", 0.0)
        self.scores.append((now(), s)); self.scores = self.scores[-120:]
        ep = self.ep
        if s >= LOG_MIN:
            if ep is None:
                ep = self.ep = {"id": uuid.uuid4().hex[:10], "t": now(), "peak": s, "model": name, "quiet": 0, "live": False, "voice": None}
            ep["peak"] = max(ep["peak"], s); ep["quiet"] = 0
            if s >= SET["threshold"] and not ep["live"]:
                ep["live"] = True
                acts.append({"type": "trigger", "id": ep["id"], "score": round(s, 3)})
                self.on_trigger(ep, acts)
        elif ep is not None:
            ep["quiet"] += 1
            if ep["quiet"] >= 6: self.close_ep()

    def barge(self, acts, score):
        """He said its name while it was talking: stop at once and listen."""
        self.gen += 1; self.ew = None
        self.pending = [a for a in self.pending if a.get("type") not in ("play", "play_done", "say")]
        trace(self.sid, "barge", score=score)
        acts.append({"type": "stop_audio"}); acts.append({"type": "trigger", "id": "barge", "score": score})
        with LOCK: jl_append("events.jsonl", {"id": uuid.uuid4().hex[:10], "t": now(), "peak": score, "model": "-", "triggered": True, "threshold": SET["threshold"], "clip": None, "kind": "barge", "sid": self.sid})
        self.on_trigger({"live": True, "barge": True}, acts)

    def close_ep(self):
        ep, self.ep = self.ep, None
        if not ep: return
        clip = None
        if not SET["private"]:
            clip = ep["id"] + ".wav"
            try: open(os.path.join(CLIPS, clip), "wb").write(wav_bytes(self.ring[-6 * SR:]))
            except OSError: clip = None
        rec = {"id": ep["id"], "t": ep["t"], "peak": round(ep["peak"], 3), "model": ep["model"], "triggered": ep["live"], "threshold": SET["threshold"], "clip": clip, "kind": "auto", "sid": self.sid}
        with LOCK: jl_append("events.jsonl", rec)
        self.pending.append(dict(rec, type="event"))

    def on_trigger(self, ep, acts):
        self.gen += 1
        self.utt = []; self.speech_t = None; self.last_voice = now() + 0.6; self.follow_for = 6.0; self.discard_until = now() + 0.5
        self.set_state("listening", "interrupted him" if ep.get("barge") else "wake word")
        acts.append({"type": "chime"})

    # ---- listening for an utterance (after the wake word, or as a follow-up)
    def listen(self, fr, r, acts):
        t = now()
        if self.ep and t - self.ep["t"] > 2.0: self.close_ep()          # keep the wake-word clip from the moment it happened
        if t < self.discard_until: return                                # the wake word itself is not part of the question
        voiced = r > max(450.0, self.floor * 3.0)
        if voiced:
            if self.speech_t is None: self.speech_t = t
            self.last_voice = t
        self.utt.append(fr)
        silent_for = t - self.last_voice
        utter = (t - self.speech_t) if self.speech_t else 0.0
        if self.speech_t is None:
            limit = self.follow_for
            if t - self.t_state > limit:                      # nobody spoke: close the conversation with a soft tone
                self.close_conv(acts, "quiet")
        elif silent_for > float(SET.get("silence_end", 1.0)) or utter > SET["max_utter"]:
            spoke = self.last_voice - self.speech_t
            if spoke < 0.35 and utter <= SET["max_utter"]:       # a click or a bump, not speech: keep listening instead of answering it
                trace(self.sid, "noise_blip", secs=round(spoke, 2), floor=round(self.floor))
                self.utt = []; self.speech_t = None; self.last_voice = t
                return
            self.respond(np.concatenate(self.utt), acts, why="silence" if silent_for > float(SET.get("silence_end", 1.0)) else "max length")

    def close_conv(self, acts, why):
        self.gen += 1; self.pending = [a for a in self.pending if a.get("type") not in ("play", "play_done", "say")]
        if self.ep: self.close_ep()
        trace(self.sid, "hangup", why=why, after=round(now() - self.t_state, 1), state=self.state)
        acts.append({"type": "tone_end", "why": why}); self.hist = []; self.set_state("idle", "hung up: " + why)
        if self.det and hasattr(self.det, "reset"): self.det.reset()

    def begin_follow(self, acts):
        self.utt = []; self.speech_t = None; self.last_voice = now(); self.ew = None; self.discard_until = now() + 0.9
        self.set_state("follow", "he finished talking")
        if self.ep: self.close_ep()

    def respond(self, pcm, acts, why=""):
        uid = "u" + uuid.uuid4().hex[:9]; self.cur_utt = uid
        if not SET["private"]:
            try: open(os.path.join(CLIPS, uid + ".wav"), "wb").write(wav_bytes(pcm))
            except OSError: pass
        a = np.abs(pcm.astype(np.float32)) if len(pcm) else np.zeros(1)
        trace(self.sid, "utterance", utt=uid, secs=round(len(pcm) / SR, 2), speech=round((self.last_voice - self.speech_t) if self.speech_t else 0, 2), ended_by=why,
              rms=round(rms(pcm)), peak=int(a.max()), floor=round(self.floor), clipped=round(float((a >= 32000).mean()), 4), state_before=self.state)
        self.set_state("thinking", "utterance ended")
        threading.Thread(target=self._think, args=(pcm, self.gen), daemon=True).start()

    def _think(self, pcm, gen):
        out = []; times_reset()
        try:
            who, conf = speaker_check(pcm); TL.who = who
            text = stt(pcm)
            t0 = now()
            trace(self.sid, "heard", utt=getattr(self, "cur_utt", None), text=text, stt_secs=times_get().get("stt"), who=who)
            jl_append("conversations.jsonl", {"t": t0, "sid": self.sid, "who": who, "who_conf": conf, "heard": text, "utt": getattr(self, "cur_utt", None)})
            if getattr(self, "ask_pcm", None) is not None and text:
                m = re.search(r"(?:this is|it'?s|i'?m|i am|my name is|name'?s)?\s*([A-Z][a-zA-Z'-]{1,20})\b", text.strip())
                name = (m.group(1) if m else "").strip().title(); apcm = self.ask_pcm; self.ask_pcm = None
                if name and name.lower() not in ("yes", "no", "nobody", "none", "nothing"):
                    ok, msg = voicebook().enroll(name, np.concatenate([apcm, pcm]) if len(apcm) + len(pcm) > 8 * SR else apcm, "guest")
                    reply = ("Nice to meet you, %s. I'll recognize you as a guest. Kylar can change that." % name) if ok else ("Nice to meet you, %s. I need a longer sample to remember your voice, so I will ask again later." % name)
                    rid = uuid.uuid4().hex[:10]; mime = tts(reply, os.path.join(REPLIES, rid + ".bin"))
                    with LOCK:
                        self.pending.append({"type": "say", "text": text}); self.pending.append({"type": "play", "url": "/reply/%s.bin" % rid, "mime": mime, "text": reply}); self.pending.append({"type": "play_done"})
                        self.ew = "waiting_played"; self.set_state("speaking"); self.hold_until = now() + 600
                    jl_append("conversations.jsonl", {"t": now(), "sid": self.sid, "heard": text, "reply": reply, "who": name, "enroll": ok}); return
            if who == "unknown" and SET.get("ask_unknown") and text and len(pcm) >= 2 * SR and getattr(self, "ask_pcm", None) is None:
                self.ask_pcm = pcm; reply = "I don't recognize your voice. Who am I talking to?"
                rid = uuid.uuid4().hex[:10]; mime = tts(reply, os.path.join(REPLIES, rid + ".bin"))
                with LOCK:
                    self.pending.append({"type": "play", "url": "/reply/%s.bin" % rid, "mime": mime, "text": reply}); self.pending.append({"type": "play_done"})
                    self.ew = "waiting_played"; self.set_state("speaking"); self.hold_until = now() + 600; self.follow_for = 20.0
                jl_append("conversations.jsonl", {"t": now(), "sid": self.sid, "heard": text, "reply": reply, "who": "unknown", "asked_who": True}); return
            if not text or len(text) < 2:
                with LOCK:
                    if gen == self.gen:
                        self.blanks = getattr(self, "blanks", 0) + 1
                        trace(self.sid, "nothing_heard", count=self.blanks)
                        if self.blanks >= 3: out.append({"type": "tone_end", "why": "nothing heard 3 times"}); self.hist = []; self.set_state("idle", "nothing heard 3 times"); self.blanks = 0
                        else: self.begin_follow([])                    # keep the conversation open and keep listening
            elif memory_command_hit(text):
                reply = memory_command(text); rid = uuid.uuid4().hex[:10]; mime = tts(reply, os.path.join(REPLIES, rid + ".bin"))
                trace(self.sid, "memory", text=text[:120], reply=reply)
                with LOCK:
                    if gen == self.gen:
                        self.pending.append({"type": "say", "text": text}); self.pending.append({"type": "play", "url": "/reply/%s.bin" % rid, "mime": mime, "text": reply, "seq": 0}); self.pending.append({"type": "play_done"})
                        self.ew = "waiting_played"; self.set_state("speaking", "saved a note"); self.hold_until = now() + 600; self.follow_for = float(SET["follow_quiet"])
                jl_append("conversations.jsonl", {"t": now(), "sid": self.sid, "heard": text, "reply": reply, "who": who, "memory_action": True})
            elif END_RE.search(text) and len(text.split()) <= 7:
                with LOCK:
                    if gen == self.gen: out.append({"type": "say", "text": text}); out.append({"type": "tone_end", "why": "you ended it"}); self.hist = []; self.set_state("idle")
            else:
                self.blanks = 0
                self.hist.append({"role": "user", "content": text})
                parts = []; first = None; tl0 = now()
                if SET.get("stream", True): gen_text = sentences(chat_stream(self.hist))
                else: gen_text = iter(sentences(iter([chat(self.hist)])))
                for sent in gen_text:
                    if gen != self.gen: return
                    ts0 = now(); rid = uuid.uuid4().hex[:10]; mime = tts(sent, os.path.join(REPLIES, rid + ".bin"))
                    trace(self.sid, "sentence", n=len(parts), text=sent, tts_secs=round(now() - ts0, 2), since_heard=round(now() - t0, 2))
                    with LOCK:
                        if gen != self.gen: return
                        if not parts:
                            self.pending.append({"type": "say", "text": text}); self.ew = "waiting_played"; self.set_state("speaking"); self.hold_until = now() + 600
                            first = round(now() - t0, 2)
                        self.pending.append({"type": "play", "url": "/reply/%s.bin" % rid, "mime": mime, "text": sent, "seq": len(parts)})
                    parts.append(sent)
                reply = " ".join(parts)
                if not parts:
                    with LOCK:
                        if gen == self.gen: self.begin_follow([]); trace(self.sid, "no_answer")
                    return
                self.hist.append({"role": "assistant", "content": reply})
                tm = times_get(); tm["first_audio"] = first; tm["llm"] = round(now() - tl0, 2)
                jl_append("conversations.jsonl", {"t": now(), "sid": self.sid, "heard": text, "reply": reply, "secs": round(now() - t0, 1), "times": tm, "who": who})
                self.follow_for = float(SET["follow_question"] if reply.rstrip().endswith("?") else SET["follow_quiet"])
                with LOCK:
                    if gen == self.gen: self.pending.append({"type": "play_done"})
        except Exception as e:
            print("conversation error:", repr(e), flush=True)
            with LOCK:
                trace(self.sid, "error", text=repr(e)[:200])
                if gen == self.gen: self.pending.append({"type": "error", "text": str(e)[:160]}); self.begin_follow([])
        with LOCK: self.pending.extend(out)

    def played(self):
        with LOCK:
            if self.state == "speaking":
                self.ew = "played"; self.hold_until = now() + 0.5

    def missed(self):
        """The owner says: I said the wake word just now and it did not react. Keep the last 6 s and the strongest score in it."""
        peak = max([s for t, s in self.scores if t > now() - 6] or [0.0])
        eid = uuid.uuid4().hex[:10]; clip = None
        if not SET["private"]:
            clip = eid + ".wav"; open(os.path.join(CLIPS, clip), "wb").write(wav_bytes(self.ring[-6 * SR:]))
        rec = {"id": eid, "t": now(), "peak": round(peak, 3), "model": "-", "triggered": False, "threshold": SET["threshold"], "clip": clip, "kind": "missed", "sid": self.sid, "label": "missed"}
        with LOCK: jl_append("events.jsonl", rec); jl_append("labels.jsonl", {"id": eid, "label": "missed", "t": now()})
        self.pending.append(dict(rec, type="event"))


SESS = {}
DET = None


def session(sid):
    with LOCK:
        s = SESS.get(sid)
        if not s:
            s = SESS[sid] = Session(sid)
        return s


# ------------------------------------------------------------------ tuning from the owner's own labels
def events_with_labels(limit=200):
    ev = jl_read("events.jsonl"); lab = {}
    for l in jl_read("labels.jsonl"): lab[l["id"]] = l["label"]
    for e in ev: e["label"] = lab.get(e["id"], e.get("label"))
    return ev


def tuning(ev):
    good = [e["peak"] for e in ev if e.get("label") in ("good", "missed")]
    bad = [e["peak"] for e in ev if e.get("label") == "false"]
    rows = []
    for t in [x / 100.0 for x in range(25, 100, 5)]:
        rows.append({"t": t, "hits": sum(1 for p in good if p >= t), "false": sum(1 for p in bad if p >= t)})
    rec = None
    if good or bad:
        ok = [r for r in rows if not good or r["hits"] >= 0.9 * len(good)]
        ok.sort(key=lambda r: (r["false"], -r["hits"], r["t"]))
        if ok: rec = ok[0]["t"]
        if bad and not good: rec = min(0.95, max(bad) + 0.05)
    return {"good": len(good), "false": len(bad), "rows": rows, "recommended": rec}


def state_json(sid=None):
    ev = events_with_labels()
    s = SESS.get(sid)
    unrev = sum(1 for e in ev if e.get("triggered") and not e.get("label"))
    hrs = sum(x.heard for x in SESS.values()) / 3600.0
    total_h = sum(r.get("hours", 0) for r in jl_read("hours.jsonl")) + hrs
    return {"settings": SET, "detector": (DET.name if DET else "NOT LOADED (see setup)"), "state": s.state if s else "idle", "heard_hours": round(total_h, 2),
            "events": ev[-40:][::-1], "tuning": tuning(ev), "unreviewed_triggers": unrev, "mock": MOCK, "keys": sorted(load_keys().keys())}


# ------------------------------------------------------------------ HTTP
SIRI = {"hist": [], "t": 0.0}
SIRI_LOCK = threading.Lock()


def memory_command(text):
    """'remember that ...', 'mark ... done', 'forget ...' typed or spoken. Returns Jarvis's reply, or None if it was not a memory command.
    Nothing is deleted: done items are kept with a date, forgotten items go to _archive.md."""
    mem = re.match(r"^\W*(?:jarvis[, ]+)?(?:please[, ]+)?(?:remember|make a note|take a note|note to self|save this)(?: that| this)?[:, ]*(.+)$", text, re.I | re.S)
    dn = re.match(r"^\W*(?:jarvis[, ]+)?(?:please[, ]+)?(?:mark|check off|cross off|set)\s+(.+?)\s+(?:as\s+)?(?:done|complete|completed|finished)\W*$", text, re.I | re.S) or \
         re.match(r"^\W*(?:jarvis[, ]+)?(?:please[, ]+)?(?:i (?:finished|completed)|we (?:finished|completed)|(?:it'?s|that'?s) done)[:, ]*(.*)$", text, re.I | re.S)
    fg = re.match(r"^\W*(?:jarvis[, ]+)?(?:please[, ]+)?(?:forget|remove|delete|take off)(?: that| the note| the reminder)?(?: about)?[:, ]*(.+)$", text, re.I | re.S)
    if not ((mem and len(mem.group(1).strip()) > 2) or (dn and len(dn.group(1).strip()) > 2) or (fg and len(fg.group(1).strip()) > 2)): return None
    mdir = os.path.join(DATA, "memory"); os.makedirs(mdir, exist_ok=True)
    if mem:
        topic = route_topic(mem.group(1))
        with LOCK, open(os.path.join(mdir, topic + ".md"), "a", encoding="utf-8") as f: f.write("- %s: %s\n" % (time.strftime("%Y-%m-%d"), mem.group(1).strip()))
        return "Got it. I saved that under %s." % topic.replace("-", " ")
    if dn:
        what = dn.group(1).strip(); topic = route_topic(what)
        with LOCK, open(os.path.join(mdir, topic + ".md"), "a", encoding="utf-8") as f: f.write("- %s DONE: %s\n" % (time.strftime("%Y-%m-%d"), what))
        return "Marked done under %s. I kept it in the history." % topic.replace("-", " ")
    words = [w for w in re.findall(r"[a-z0-9']+", fg.group(1).lower()) if len(w) > 2]
    moved = 0
    with LOCK:
        for fn in os.listdir(mdir):
            path = os.path.join(mdir, fn)
            if not fn.endswith(".md") or fn == "_archive.md": continue
            lines = open(path, encoding="utf-8").read().splitlines(); keep = []
            for ln in lines:
                if words and sum(w in ln.lower() for w in words) >= max(1, (len(words) + 1) // 2) and moved < 3:
                    open(os.path.join(mdir, "_archive.md"), "a", encoding="utf-8").write("- archived %s from %s: %s\n" % (time.strftime("%Y-%m-%d"), fn, ln)); moved += 1
                else: keep.append(ln)
            open(path, "w", encoding="utf-8").write("\n".join(keep) + ("\n" if keep else ""))
    return ("Done. I moved %d note%s to the archive." % (moved, "" if moved == 1 else "s")) if moved else "I couldn't find a note matching that."


def memory_command_hit(text):
    return bool(re.match(r"^\W*(?:jarvis[, ]+)?(?:please[, ]+)?(?:remember|make a note|take a note|note to self|save this|mark .+ (?:as )?(?:done|complete|completed|finished)\W*$|check off|cross off|forget|remove|delete|take off|i (?:finished|completed) |we (?:finished|completed) |(?:it'?s|that'?s) done)", text, re.I | re.S)) and len(text) > 6


def ask_text(text, want_audio=True, host=None):
    """Text in, answer out, for the Siri Shortcut. Keeps a short running conversation (resets after 3 minutes of quiet)."""
    text = (text or "").strip()
    if len(text) < 2: return {"reply": "", "end": True, "followup": False}
    t0 = now()
    reply = memory_command(text)
    if reply is not None:
        out = {"reply": reply, "end": False, "followup": False}
        if want_audio:
            try:
                rid = uuid.uuid4().hex[:10]; tts(reply, os.path.join(REPLIES, rid + ".bin"))
                out["audio_url"] = "https://%s/reply/%s.bin" % (host, rid) if host else "/reply/%s.bin" % rid
            except Exception as e: out["audio_error"] = str(e)[:120]
        jl_append("conversations.jsonl", {"t": t0, "sid": "siri", "who": "owner", "heard": text, "reply": reply, "memory_action": True})
        return out
    with SIRI_LOCK:
        if t0 - SIRI["t"] > 180: SIRI["hist"] = []
        if END_RE.search(text):
            SIRI["hist"] = []; SIRI["t"] = t0
            jl_append("conversations.jsonl", {"t": t0, "sid": "siri", "who": "owner", "heard": text, "reply": "(ended)"})
            return {"reply": "Okay.", "end": True, "followup": False}
        SIRI["hist"].append({"role": "user", "content": text})
        reply = chat(SIRI["hist"]); SIRI["hist"].append({"role": "assistant", "content": reply}); SIRI["t"] = now()
    out = {"reply": reply, "end": False, "followup": reply.rstrip().endswith("?")}
    if want_audio:
        try:
            rid = uuid.uuid4().hex[:10]; tts(reply, os.path.join(REPLIES, rid + ".bin"))
            out["audio_url"] = "https://%s/reply/%s.bin" % (host, rid) if host else "/reply/%s.bin" % rid
        except Exception as e:
            print("siri tts error:", repr(e), flush=True); out["audio_error"] = str(e)[:120]
    jl_append("conversations.jsonl", {"t": now(), "sid": "siri", "who": "owner", "heard": text, "reply": reply, "secs": round(now() - t0, 1), "times": times_get()})
    return out


def tips_for(rows):
    """Plain-English suggestions from the tags Kylar tapped and the timings logged."""
    tags = {}
    for r in rows:
        for t in r.get("tags", []): tags[t] = tags.get(t, 0) + 1
    tips = []; tot = []
    for r in rows:
        tm = r.get("times") or {}
        v = tm.get("first_audio") if tm.get("first_audio") is not None else sum(tm.get(k, 0) for k in ("stt", "llm", "tts"))
        if tm: tot.append(v)
    avg = sum(tot) / len(tot) if tot else 0
    if tot and avg > 4: tips.append("Answers take %.1f s on average to start. Use the Flash voice model, shorten the reply length, and keep streaming on." % avg)
    if tags.get("too slow", 0) >= 2: tips.append("You tagged 'too slow' %d times. Lower the reply length and use Flash; check the 'hear' time if the recording or Wi-Fi is the slow part." % tags["too slow"])
    if tags.get("too long", 0) >= 1: tips.append("He talked too long %d time(s). Lower the reply length; say 'be brief' to him and ask him to remember it." % tags["too long"])
    if tags.get("misheard", 0) >= 2: tips.append("He misheard you %d times. Try AirPods or a mounted phone closer to you, and lower the pause before he decides you're done if he cuts you off." % tags["misheard"])
    if tags.get("bad pronunciation", 0) >= 1: tips.append("Add the word he said wrong to the Pronunciations box, spelled the way it should sound.")
    if tags.get("wrong answer", 0) >= 2: tips.append("Wrong answers: tell him the correct fact and say 'remember that' so it goes in his notes.")
    if tags.get("good", 0) >= 3 and not tips: tips.append("Looks good so far. Keep tagging so the suggestions stay accurate.")
    return tips


def build_report(minutes=20):
    """Plain-text replay of recent conversations: every state change, what was heard, every sentence he spoke, timings, hang-up reasons."""
    cut = now() - minutes * 60
    ev = [r for r in jl_read("trace.jsonl") if r.get("t", 0) >= cut]
    if not ev: return "No activity in the last %d minutes." % minutes
    out = ["JARVIS REPLAY, last %d minutes (clock times, then seconds after the first line)" % minutes, ""]
    t0 = ev[0]["t"]; cur = None
    for r in ev:
        if r["sid"] != cur:
            cur = r["sid"]; out.append("--- session %s ---" % str(cur)[:6])
        k = r["kind"]; ts = "%s +%5.1fs" % (time.strftime("%H:%M:%S", time.localtime(r["t"])), r["t"] - t0)
        if k == "state": line = "state %s -> %s%s" % (r["frm"], r["to"], (" (%s)" % r["why"]) if r.get("why") else "")
        elif k == "utterance": line = "YOUR RECORDING: %.1fs long, %.1fs of it speech, ended by %s; loudness %d (room noise %d), peak %d%s  [audio /clip/%s.wav]" % (r["secs"], r["speech"], r["ended_by"], r["rms"], r["floor"], r["peak"], ", CLIPPING" if r.get("clipped", 0) > 0.002 else "", r["utt"])
        elif k == "heard": line = "HE HEARD: %r  (transcribe %.1fs, speaker %s)" % (r.get("text"), r.get("stt_secs") or 0, r.get("who"))
        elif k == "sentence": line = "HE SAYS #%d (voice %.1fs, %.1fs after you stopped): %s" % (r["n"] + 1, r["tts_secs"], r["since_heard"], r["text"])
        elif k == "noise_blip": line = "ignored a %.2fs blip (not speech)" % r["secs"]
        elif k == "nothing_heard": line = "heard nothing in the recording (%d in a row), stayed listening" % r["count"]
        elif k == "hangup": line = "HUNG UP: %s (state was %s)" % (r["why"], r["state"])
        elif k == "barge": line = "you interrupted him (wake word score %s)" % r["score"]
        elif k == "error": line = "ERROR: %s" % r["text"]
        elif k == "no_answer": line = "he had no answer to say"
        elif k == "client": line = "PHONE: %s %s" % (r.get("what"), r.get("info", ""))
        else: line = k + " " + json.dumps({a: b for a, b in r.items() if a not in ("t", "sid", "kind")})
        out.append("%s  %s" % (ts, line))
    first = [r for r in ev if r["kind"] == "sentence" and r["n"] == 0]
    if first: out += ["", "Time from end of your speech to his first voice: average %.1fs, slowest %.1fs, over %d answers" % (sum(r["since_heard"] for r in first) / len(first), max(r["since_heard"] for r in first), len(first))]
    hang = [r for r in ev if r["kind"] == "hangup"]
    if hang: out.append("Hang-ups: " + ", ".join(str(r["why"]) for r in hang))
    out.append("Settings: " + ", ".join("%s=%s" % (k, SET.get(k)) for k in ("silence_end", "follow_quiet", "follow_question", "max_tokens", "speech_speed", "tts_model", "barge_in", "threshold")))
    return "\n".join(out)


class H(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *a): pass
    def _send(self, code, body, ctype="application/json", extra=None):
        if isinstance(body, (dict, list)): body = json.dumps(body).encode()
        elif isinstance(body, str): body = body.encode()
        self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body))); self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers(); self.wfile.write(body)
    def _json(self):
        n = int(self.headers.get("Content-Length") or 0)
        try: return json.loads(self.rfile.read(n) or b"{}")
        except ValueError: return {}

    def do_GET(self):
        p = self.path.split("?")[0]
        q = dict(x.split("=", 1) for x in (self.path.split("?")[1].split("&") if "?" in self.path else []) if "=" in x)
        if p in ("/", "/index.html"):
            return self._send(200, open(os.path.join(HERE, "phone.html"), "rb").read(), "text/html; charset=utf-8")
        if p == "/ask":
            import urllib.parse
            try: return self._send(200, ask_text(urllib.parse.unquote_plus(q.get("text", "")), q.get("audio", "1") != "0", self.headers.get("Host")))
            except Exception as e: return self._send(500, {"error": str(e)[:200]})
        if p == "/lab": return self._send(200, open(os.path.join(HERE, "lab.html"), "rb").read(), "text/html; charset=utf-8")
        if p == "/conv":
            rows = jl_read("conversations.jsonl")[-60:]; fb = {}
            for f in jl_read("feedback.jsonl"): fb.setdefault(round(f.get("t", 0), 1), []).append(f.get("tag"))
            for r in rows: r["tags"] = fb.get(round(r.get("t", 0), 1), [])
            return self._send(200, {"rows": rows[::-1], "settings": {k: SET.get(k) for k in ("speech_speed", "max_tokens", "tts_model", "follow_quiet", "follow_question", "silence_end", "barge_in")}, "pron": load_pron(), "tips": tips_for(rows)})
        if p == "/voices": return self._send(200, {"voices": voicebook().listing(), "threshold": SET.get("voice_threshold"), "ask_unknown": SET.get("ask_unknown")})
        if p == "/report":
            return self._send(200, build_report(float(q.get("min", 20))).encode(), "text/plain; charset=utf-8")
        if p == "/state": return self._send(200, state_json(q.get("sid")))
        m = re.match(r"^/clip/([0-9a-zA-Z]+)\.wav$", p)
        if m:
            try: return self._send(200, open(os.path.join(CLIPS, m.group(1) + ".wav"), "rb").read(), "audio/wav")
            except OSError: return self._send(404, {"error": "gone"})
        m = re.match(r"^/reply/([0-9a-f]+)\.bin$", p)
        if m:
            try:
                b = open(os.path.join(REPLIES, m.group(1) + ".bin"), "rb").read()
                return self._send(200, b, "audio/wav" if b[:4] == b"RIFF" else "audio/mpeg")
            except OSError: return self._send(404, {"error": "gone"})
        self._send(404, {"error": "not found"})

    def do_POST(self):
        p = self.path.split("?")[0]
        q = dict(x.split("=", 1) for x in (self.path.split("?")[1].split("&") if "?" in self.path else []) if "=" in x)
        if p == "/audio":
            n = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(n)
            pcm = np.frombuffer(raw[: len(raw) // 2 * 2], dtype="<i2")
            s = session(q.get("sid", "x"))
            with LOCK:
                acts = s.feed(pcm)
                pend, s.pending = s.pending, []
                lvl = rms(pcm)
            return self._send(200, {"acts": acts + pend, "state": s.state, "level": round(lvl), "paused": SET["paused"]})
        if p in ("/enroll", "/whois"):
            n = int(self.headers.get("Content-Length") or 0); raw = self.rfile.read(n)
            pcm = np.frombuffer(raw[: len(raw) // 2 * 2], dtype="<i2")
            if p == "/whois":
                name, d, rank = voicebook().identify(pcm)
                if name is None: return self._send(200, {"ok": False, "msg": "Not enough speech, or no voices enrolled yet."})
                return self._send(200, {"ok": True, "best": name, "distance": round(d, 2), "accepted": d <= float(SET.get("voice_threshold", 3.0)), "ranked": [[a, round(b, 2)] for a, b in rank]})
            nm = urllib.parse.unquote_plus(q.get("name", "")).strip()[:30]
            if not nm: return self._send(200, {"ok": False, "msg": "Type a name first."})
            ok, msg = voicebook().enroll(nm, pcm, q.get("level", "guest")); return self._send(200, {"ok": ok, "msg": msg, "voices": voicebook().listing()})
        if p == "/ask":
            n = int(self.headers.get("Content-Length") or 0); raw = self.rfile.read(n); ct = self.headers.get("Content-Type", ""); times_reset()
            try:
                if "json" in ct.lower() or raw[:1] == b"{":
                    try: b = json.loads(raw or b"{}")
                    except ValueError: b = {}
                else:
                    b = {"text": stt_file(audio_from_body(ct, raw))}
                    jl_append("conversations.jsonl", {"t": now(), "sid": "siri", "heard_raw": b["text"]})
                if b.get("format") == "json": return self._send(200, ask_text(b.get("text", ""), b.get("audio", True), self.headers.get("Host")))
                # default for the Siri Shortcut: answer comes back as Brian's voice (an audio file)
                out = ask_text(b.get("text", ""), True, None)
                rid = (out.get("audio_url") or "").rsplit("/", 1)[-1].replace(".bin", "")
                if not rid and out.get("reply"):
                    rid = uuid.uuid4().hex[:10]; tts(out["reply"], os.path.join(REPLIES, rid + ".bin"))
                if not rid: return self._send(200, {"reply": "", "note": "nothing heard"})
                data = open(os.path.join(REPLIES, rid + ".bin"), "rb").read()
                return self._send(200, data, "audio/wav" if data[:4] == b"RIFF" else "audio/mpeg")
            except Exception as e: return self._send(500, {"error": str(e)[:200]})
        b = self._json()
        if p == "/voices/delete":
            voicebook().delete(str(b.get("name", ""))); return self._send(200, {"ok": True, "voices": voicebook().listing()})
        if p == "/voices/level":
            voicebook().set_level(str(b.get("name", "")), str(b.get("level", ""))); return self._send(200, {"ok": True, "voices": voicebook().listing()})
        if p == "/feedback":
            with LOCK: jl_append("feedback.jsonl", {"t": b.get("t"), "tag": str(b.get("tag", ""))[:40], "at": now()})
            return self._send(200, {"ok": True})
        if p == "/pron":
            cur = {}
            for k, v in (b.get("map") or {}).items():
                if str(k).strip(): cur[str(k).strip()[:40]] = str(v).strip()[:60]
            json.dump(cur, open(os.path.join(DATA, "pronunciations.json"), "w")); return self._send(200, {"ok": True, "pron": load_pron()})
        if p == "/label":
            if b.get("label") in ("good", "false", "unsure", None):
                with LOCK: jl_append("labels.jsonl", {"id": b.get("id"), "label": b.get("label"), "t": now()})
            return self._send(200, {"ok": True})
        if p == "/missed":
            session(q.get("sid", "x")).missed(); return self._send(200, {"ok": True})
        if p == "/ev":
            trace(q.get("sid", "x"), "client", what=str(b.get("what", ""))[:40], info=str(b.get("info", ""))[:120]); return self._send(200, {"ok": True})
        if p == "/played":
            session(q.get("sid", "x")).played(); return self._send(200, {"ok": True})
        if p == "/settings":
            with LOCK:
                for k in ("threshold", "paused", "private", "follow_quiet", "follow_question", "speech_speed", "max_tokens", "tts_model", "silence_end", "barge_in", "stream", "voice_threshold", "ask_unknown"):
                    if k in b:
                        SET[k] = type(DEFAULTS[k])(b[k]) if not isinstance(DEFAULTS[k], bool) else bool(b[k])
                SET["threshold"] = min(0.99, max(0.1, float(SET["threshold"]))); save_settings()
            return self._send(200, {"ok": True, "settings": SET})
        if p == "/end":
            s = session(q.get("sid", "x")); acts = []
            with LOCK: s.close_conv(acts, "you ended it")
            return self._send(200, {"ok": True})
        self._send(404, {"error": "not found"})


class TServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True; allow_reuse_address = True


def janitor():
    while True:
        time.sleep(3600)
        cut = now() - KEEP_DAYS * 86400
        for d in (CLIPS, REPLIES):
            try:
                for f in os.listdir(d):
                    p = os.path.join(d, f)
                    if os.path.getmtime(p) < cut: os.remove(p)
            except OSError: pass
        with LOCK:
            h = sum(x.heard for x in SESS.values()) / 3600.0
            for x in SESS.values(): x.heard = 0.0
            if h: jl_append("hours.jsonl", {"t": now(), "hours": h})


def main():
    global DET
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8099
    DET = make_detector()
    threading.Thread(target=janitor, daemon=True).start()
    print("phone voice on 127.0.0.1:%d | detector: %s | keys: %s | data: %s" % (port, DET.name if DET else "NONE", sorted(load_keys().keys()), DATA), flush=True)
    TServer(("127.0.0.1", port), H).serve_forever()


if __name__ == "__main__":
    main()
