#!/usr/bin/env python3
"""PHONE VOICE (runs on the Pi, reached from the phone over Tailscale HTTPS). Everything here answers ONLY to the phone that is talking: the reply audio goes back to that phone,
nothing is played on the home speakers and nothing is shown on the Pi screen.
Phase 1: always-listening wake-word logger. The phone page streams 16 kHz audio; every wake-word candidate is logged with a short clip so you can mark it good / false / missed and tune the threshold.
Phase 2: conversation. After the wake word it records one utterance, transcribes (OpenAI), answers (OpenAI chat), speaks (ElevenLabs), then stays open for follow-ups
         (10 s of quiet, 20 s if its last reply was a question; "that's all" / "goodbye" ends it; a soft tone marks the close).
Phase 3 (voice ID) plugs into speaker_check() below; until a voiceprint model is installed everything is treated as the owner and logged as "unverified".
Audio is kept only as short clips around wake-word candidates (never continuous). Stdlib + numpy; openwakeword/onnxruntime for the real detector.
  python3 phone_voice.py [port=8099]"""
import http.server, io, json, math, os, re, socketserver, struct, sys, threading, time, urllib.request, uuid, wave
import numpy as np

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
def jl_read(name):
    out = []
    try:
        for l in open(os.path.join(DATA, name)):
            try: out.append(json.loads(l))
            except ValueError: pass
    except OSError: pass
    return out


# ------------------------------------------------------------------ settings
DEFAULTS = {"threshold": 0.6, "paused": False, "private": False, "models": ["hey_jarvis"], "follow_quiet": 10.0, "follow_question": 20.0, "voice_id": "Brian", "max_utter": 20.0}
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
def _post(url, headers, body, timeout=60):
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    return urllib.request.urlopen(req, timeout=timeout).read()


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


def prompt_text():
    try: return open(os.path.join(DATA, "prompt.txt")).read().strip()
    except OSError:
        return ("You are the Lovelady family's home assistant, talking to the owner through his phone and earbuds. Be blunt and honest, say when you do not know, "
                "keep answers short enough to listen to, and ask a short question back only when you really need the answer.")


def chat(history):
    if MOCK: return "It is a mock reply. Anything else?"
    key = load_keys().get("OPENAI_API_KEY")
    body = json.dumps({"model": "gpt-4o-mini", "messages": [{"role": "system", "content": prompt_text()}] + history[-12:], "max_tokens": 300}).encode()
    r = _post("https://api.openai.com/v1/chat/completions", {"Authorization": "Bearer " + key, "Content-Type": "application/json"}, body)
    return json.loads(r)["choices"][0]["message"]["content"].strip()


def tts(text, path):
    if MOCK:
        pcm = (np.sin(2 * np.pi * 440 * np.arange(SR // 4) / SR) * 3000).astype("<i2")
        open(path, "wb").write(wav_bytes(pcm)); return "audio/wav"
    k = load_keys(); key = k.get("ELEVENLABS_API_KEY"); vid = k.get("ELEVENLABS_VOICE_ID")
    if not key or not vid: raise RuntimeError("no ELEVENLABS_API_KEY / ELEVENLABS_VOICE_ID in %s/keys.env" % DATA)
    body = json.dumps({"text": text, "model_id": "eleven_turbo_v2_5"}).encode()
    audio = _post("https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=mp3_44100_64" % vid, {"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"}, body)
    open(path, "wb").write(audio); return "audio/mpeg"


def speaker_check(pcm):
    """Phase 3 hook: returns (who, confidence). With no voiceprint model installed everyone is 'owner (unverified)'."""
    return ("owner", None)


END_RE = re.compile(r"\b(that'?s all|that is all|goodbye|good bye|never ?mind|stop listening|thanks,? that'?s it|we'?re done)\b", re.I)


# ------------------------------------------------------------------ the session: one per phone page
class Session:
    def __init__(self, sid):
        self.sid = sid; self.det = None; self.ring = np.zeros(0, dtype=np.int16); self.buf = np.zeros(0, dtype=np.int16)
        self.hist = []; self.state = "idle"; self.t_state = now(); self.floor = 300.0
        self.ep = None; self.pending = []; self.scores = []; self.heard = 0.0; self.started = now(); self.last_seen = now()
        self.utt = []; self.speech_t = None; self.last_voice = now(); self.hold_until = 0.0; self.follow_for = 10.0
        self.ew = None; self.discard_until = 0.0

    def det_ok(self):
        if self.det is None: self.det = DET
        return self.det is not None

    def set_state(self, s):
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
        self.utt = []; self.speech_t = None; self.last_voice = now() + 0.6; self.follow_for = 6.0; self.discard_until = now() + 0.5
        self.set_state("listening")
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
        elif silent_for > 1.0 or utter > SET["max_utter"]:
            self.respond(np.concatenate(self.utt), acts)

    def close_conv(self, acts, why):
        if self.ep: self.close_ep()
        acts.append({"type": "tone_end", "why": why}); self.hist = []; self.set_state("idle")
        if self.det and hasattr(self.det, "reset"): self.det.reset()

    def begin_follow(self, acts):
        self.utt = []; self.speech_t = None; self.last_voice = now(); self.ew = None; self.discard_until = now() + 0.3
        self.set_state("follow")
        if self.ep: self.close_ep()

    def respond(self, pcm, acts):
        self.set_state("thinking")
        threading.Thread(target=self._think, args=(pcm,), daemon=True).start()

    def _think(self, pcm):
        out = []
        try:
            who, conf = speaker_check(pcm)
            text = stt(pcm)
            t0 = now()
            jl_append("conversations.jsonl", {"t": t0, "sid": self.sid, "who": who, "who_conf": conf, "heard": text})
            if not text or len(text) < 2:
                with LOCK: out.append({"type": "tone_end", "why": "nothing heard"}); self.hist = []; self.set_state("idle")
            elif END_RE.search(text):
                with LOCK: out.append({"type": "say", "text": text}); out.append({"type": "tone_end", "why": "you ended it"}); self.hist = []; self.set_state("idle")
            else:
                self.hist.append({"role": "user", "content": text})
                reply = chat(self.hist); self.hist.append({"role": "assistant", "content": reply})
                rid = uuid.uuid4().hex[:10]; ext = "mp3"
                mime = tts(reply, os.path.join(REPLIES, rid + ".bin"))
                jl_append("conversations.jsonl", {"t": now(), "sid": self.sid, "heard": text, "reply": reply, "secs": round(now() - t0, 1)})
                self.follow_for = float(SET["follow_question"] if reply.rstrip().endswith("?") else SET["follow_quiet"])
                with LOCK:
                    out.append({"type": "say", "text": text}); out.append({"type": "play", "url": "/reply/%s.bin" % rid, "mime": mime, "text": reply})
                    self.ew = "waiting_played"; self.set_state("speaking"); self.hold_until = now() + 600
        except Exception as e:
            print("conversation error:", repr(e), flush=True)
            with LOCK: out.append({"type": "error", "text": str(e)[:160]}); out.append({"type": "tone_end", "why": "error"}); self.set_state("idle")
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


def ask_text(text, want_audio=True, host=None):
    """Text in, answer out, for the Siri Shortcut. Keeps a short running conversation (resets after 3 minutes of quiet)."""
    text = (text or "").strip()
    if len(text) < 2: return {"reply": "", "end": True, "followup": False}
    t0 = now()
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
    jl_append("conversations.jsonl", {"t": now(), "sid": "siri", "who": "owner", "heard": text, "reply": reply, "secs": round(now() - t0, 1)})
    return out


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
        if p == "/state": return self._send(200, state_json(q.get("sid")))
        m = re.match(r"^/clip/([0-9a-f]+)\.wav$", p)
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
        b = self._json()
        if p == "/ask":
            try: return self._send(200, ask_text(b.get("text", ""), b.get("audio", True), self.headers.get("Host")))
            except Exception as e: return self._send(500, {"error": str(e)[:200]})
        if p == "/label":
            if b.get("label") in ("good", "false", "unsure", None):
                with LOCK: jl_append("labels.jsonl", {"id": b.get("id"), "label": b.get("label"), "t": now()})
            return self._send(200, {"ok": True})
        if p == "/missed":
            session(q.get("sid", "x")).missed(); return self._send(200, {"ok": True})
        if p == "/played":
            session(q.get("sid", "x")).played(); return self._send(200, {"ok": True})
        if p == "/settings":
            with LOCK:
                for k in ("threshold", "paused", "private", "follow_quiet", "follow_question"):
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
