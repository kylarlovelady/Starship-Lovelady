#!/usr/bin/env python3
"""HOME JARVIS WAKE WATCHER (Kylar 2026-11-07). Cron every 5 minutes on the Pi. Looks at every wake-up the satellite recorded (~/voice-data/home-mic/*-wake.wav and the *-stt.wav
that follows it) and labels it from the AUDIO STATS only (no audio leaves the Pi, nothing is transcribed here):
  empty   = after the wake-up there was hardly any speech (TV hum, a noise, a cough, or the wake word model fired on nothing) -> a false wake-up
  talk    = people were already talking right before the trigger AND the listening clip is long -> probably us talking to each other (false wake-up)
  command = anything else (a short real request)
Writes ~/voice-data/wake-log.jsonl (one row per wake-up), ~/crew-web/jarvis-wake.json (for the Starship board) and memory/inbox/jarvis-wake-report.md (for Claude's reviews).
Also records the current wake word threshold and every tuning change (~/voice-data/tune-log.jsonl). Never raises."""
import array, glob, json, math, os, re, subprocess, time, wave
H = os.path.expanduser("~"); D = os.path.join(H, "voice-data", "home-mic"); LOG = os.path.join(H, "voice-data", "wake-log.jsonl"); R = os.path.join(H, "starship")
OUT = os.path.join(H, "crew-web", "jarvis-wake.json")


def stats(p):
    try:
        w = wave.open(p, "rb"); n = w.getnframes(); sr = w.getframerate(); ch = w.getnchannels()
        if w.getsampwidth() != 2 or n == 0: return None
        a = array.array("h"); a.frombytes(w.readframes(n))
        if ch > 1: a = a[::ch]
        fr = int(sr * 0.03); rms = [math.sqrt(sum(x * x for x in a[i:i + fr]) / fr) for i in range(0, len(a) - fr, fr)]
        if not rms: return None
        s = sorted(rms); floor = s[max(0, len(s) // 10)]; thr = max(floor * 3, 400); sp = [r > thr for r in rms]
        tail = sp[-int(2.0 / 0.03):] if len(sp) > 10 else sp           # the last 2 s before the trigger
        return {"secs": round(n / float(sr), 1), "speech": round(100.0 * sum(sp) / len(sp)), "near": round(100.0 * sum(tail) / max(1, len(tail))), "floor": int(floor)}
    except Exception:
        return None


def known():
    k = set()
    try:
        for l in open(LOG): k.add(json.loads(l).get("id"))
    except Exception: pass
    return k


def label(wk, st):
    if not st or st["speech"] < 8: return "empty"
    if wk and wk["near"] >= 60 and st["secs"] >= 8: return "talk"
    return "command"


def thr_now():
    try:
        o = subprocess.run("docker inspect openwakeword --format '{{join .Args \" \"}}'", shell=True, capture_output=True, text=True, timeout=10).stdout
        m = re.search(r"--threshold\s+([0-9.]+)", o); return float(m.group(1)) if m else None
    except Exception: return None


def main():
    seen = known(); new = []
    for wp in glob.glob(os.path.join(D, "**", "*-wake.wav"), recursive=True):
        i = os.path.basename(wp).replace("-wake.wav", "")
        if i in seen: continue
        t = os.path.getmtime(wp)
        if time.time() - t < 90: continue          # wait for the listening clip to finish
        sp = os.path.join(os.path.dirname(wp), i + "-stt.wav"); wk = stats(wp); st = stats(sp) if os.path.exists(sp) else None
        new.append({"id": i, "t": t, "label": label(wk, st), "wake": wk, "stt": st})
    if new:
        with open(LOG, "a") as f:
            for r in new: f.write(json.dumps(r) + "\n")
    rows = []
    try:
        for l in open(LOG):
            try: rows.append(json.loads(l))
            except ValueError: pass
    except OSError: pass
    now = time.time(); d1 = [r for r in rows if now - r["t"] < 86400]; d7 = [r for r in rows if now - r["t"] < 7 * 86400]
    def cnt(a, k): return sum(1 for r in a if r["label"] == k)
    byh = {}
    for r in d7:
        h = time.localtime(r["t"]).tm_hour; byh.setdefault(h, {"empty": 0, "talk": 0, "command": 0})[r["label"]] += 1
    tune = []
    try:
        for l in open(os.path.join(H, "voice-data", "tune-log.jsonl")): tune.append(json.loads(l))
    except Exception: pass
    out = {"updated": now, "threshold": thr_now(), "wakes24": len(d1), "empty24": cnt(d1, "empty"), "talk24": cnt(d1, "talk"), "command24": cnt(d1, "command"),
           "wakes7d": len(d7), "false7d": cnt(d7, "empty") + cnt(d7, "talk"), "by_hour": byh, "tune": tune[-5:],
           "last": [{"t": r["t"], "label": r["label"], "secs": (r.get("stt") or {}).get("secs"), "near": (r.get("wake") or {}).get("near")} for r in rows[-10:]]}
    try:
        tmp = OUT + ".tmp"; json.dump(out, open(tmp, "w")); os.replace(tmp, OUT)
    except Exception: pass
    md = ["# Home Jarvis wake-up report (auto, audio stats only)", "", "Updated %s. Wake word threshold now: %s. Mic muted now: %s." % (time.strftime("%a %H:%M"), out["threshold"], os.path.exists(os.path.join(H, "hub-dashboard", "muted"))), "",
          "Last 24 h: **%d** wake-ups: %d empty, %d probably us talking, %d real commands. Last 7 days: %d wake-ups, %d false." % (out["wakes24"], out["empty24"], out["talk24"], out["command24"], out["wakes7d"], out["false7d"]), "",
          "| hour | empty | talk | command |", "|---|---|---|---|"]
    for h in sorted(byh): md.append("| %02d:00 | %d | %d | %d |" % (h, byh[h]["empty"], byh[h]["talk"], byh[h]["command"]))
    md += ["", "## Recent tuning changes"] + (["- %s: %s -> %s (%s)" % (time.strftime("%a %H:%M", time.localtime(x.get("t", 0))), x.get("from"), x.get("to"), x.get("why", "")) for x in tune[-8:]] or ["none yet"])
    try: open(os.path.join(R, "memory", "inbox", "jarvis-wake-report.md"), "w").write("\n".join(md) + "\n")
    except Exception: pass


try: main()
except Exception as e: print("jarvis_watch error:", e)
