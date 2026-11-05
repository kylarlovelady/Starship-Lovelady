#!/usr/bin/env python3
"""Home speaker mic report (stats only, no audio leaves the Pi). Reads the satellite's debug recordings in ~/voice-data/home-mic and writes
memory/inbox/home-mic-report.md: for each recent clip the time, length, loudness, background-noise floor, how much of it was speech, and how long the
quiet at the end was (end-of-speech detection needs that quiet). Also lists the satellite restarts the watchdog made. Never raises."""
import array, glob, math, os, subprocess, time, wave
H = os.path.expanduser("~"); D = os.path.join(H, "voice-data", "home-mic"); R = os.path.join(H, "starship")
def stats(p):
    try:
        w = wave.open(p, "rb"); n = w.getnframes(); sr = w.getframerate(); ch = w.getnchannels(); sw = w.getsampwidth()
        if sw != 2: return None
        a = array.array("h"); a.frombytes(w.readframes(n))
        if ch > 1: a = a[::ch]
        fr = int(sr * 0.03); rms = []
        for i in range(0, len(a) - fr, fr):
            seg = a[i:i + fr]; rms.append(math.sqrt(sum(x * x for x in seg) / fr))
        if not rms: return None
        s = sorted(rms); floor = s[max(0, len(s) // 10)]; thr = max(floor * 3, 400)
        speech = [r > thr for r in rms]; tail = 0
        for v in reversed(speech):
            if v: break
            tail += 1
        return {"secs": round(n / float(sr), 1), "peak": max(abs(x) for x in a), "avg": int(sum(rms) / len(rms)), "floor": int(floor),
                "speech_pct": int(100 * sum(speech) / len(speech)), "tail_quiet": round(tail * 0.03, 1)}
    except Exception:
        return None
rows = []
for p in sorted(glob.glob(os.path.join(D, "**", "*.wav"), recursive=True), key=os.path.getmtime)[-40:]:
    st = stats(p)
    if st: rows.append((os.path.getmtime(p), os.path.relpath(p, D), st))
md = ["# Home speaker mic report (auto, stats only; audio stays on the Pi)", "",
      "floor = background noise level (16-bit scale, 0 to 32767); speech% = share of the clip louder than 3x the floor; tail quiet = seconds of quiet at the end (end-of-speech needs about 1 s).", ""]
if not rows: md.append("No clips yet: the satellite recording folder is empty or recording is not switched on.")
else:
    md += ["| time | clip | secs | peak | avg | floor | speech% | tail quiet |", "|---|---|---|---|---|---|---|---|"]
    for t, rel, s in rows[-30:]:
        md.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (time.strftime("%a %H:%M:%S", time.localtime(t)), rel[-40:], s["secs"], s["peak"], s["avg"], s["floor"], s["speech_pct"], s["tail_quiet"]))
    fl = [s["floor"] for _, _, s in rows]; md += ["", "Median background noise floor: %d. Clips with less than 0.8 s of tail quiet: %d of %d." % (sorted(fl)[len(fl) // 2], sum(1 for _, _, s in rows if s["tail_quiet"] < 0.8), len(rows))]
wd = subprocess.run("journalctl -u hub-watchdog --since '24 hours ago' --no-pager 2>/dev/null | grep -i 'stuck' | tail -12", shell=True, capture_output=True, text=True).stdout.strip()
md += ["", "## Satellite restarts by the watchdog (last 24 h)", wd or "none"]
try: open(os.path.join(R, "memory", "inbox", "home-mic-report.md"), "w").write("\n".join(md) + "\n")
except OSError: pass
print("\n".join(md))
