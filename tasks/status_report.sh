#!/bin/bash
# Writes a plain status snapshot of the Pi: services, health, markets agent, Jarvis (hang-ups, speed), sync, cron.
#   memory/inbox/pi-status.md  -> goes to the repo with the notes sync, so Claude can read it without screenshots (no keys, no IPs, no transcripts)
#   hub-extra.json             -> stays on the Pi (git-ignored); the Starship page reads it for the Mission board
# Run any time: bash ~/starship/tasks/status_report.sh
python3 - <<'PY'
import json, os, re, subprocess, time, glob
H = os.path.expanduser("~"); R = os.path.join(H, "starship"); now = time.time()
def sh(c, t=8):
    try: return subprocess.run(c, shell=True, capture_output=True, text=True, timeout=t).stdout.strip()
    except Exception: return ""
def age(p):
    try: return (now - os.path.getmtime(p)) / 3600.0
    except OSError: return None
def hrs(a): return "no file" if a is None else ("%.1f h ago" % a if a >= 1 else "%d min ago" % (a * 60))
out = {}; md = ["# Pi status (auto, no secrets)", "Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.", ""]
# health
up = sh("uptime -p"); temp = sh("vcgencmd measure_temp").replace("temp=", "") or ""
thr = sh("vcgencmd get_throttled").replace("throttled=", "")
mem = sh("free -m | awk '/Mem:/{printf \"%d%%\", $3*100/$2}'"); disk = sh("df -h / | awk 'NR==2{print $5}'")
out["pi"] = {"uptime": up, "temp": temp, "throttled": thr, "mem": mem, "disk": disk}
md += ["## Pi", "- %s; temp %s; throttled flags %s (0x0 is clean); memory %s; disk %s" % (re.sub(r"\d+ minutes?", "", up) if False else up, temp or "?", thr or "?", mem, disk)]
# services
want = ["market-agent", "phone-voice", "tailscaled", "docker", "hub-dashboard", "hub-devices", "hub-kdp", "hub-lights", "hub-memlog", "hub-oled", "hub-outage", "hub-satellite", "hub-voice", "hub-watchdog"]
sv = {w: sh("systemctl is-active %s" % w) or "unknown" for w in want}; out["services"] = sv
bad = [k for k, v in sv.items() if v != "active"]; failed = sh("systemctl --failed --no-legend | awk '{print $1}'").split()
md += ["", "## Services", "- active: %s" % ", ".join(k for k, v in sv.items() if v == "active"), "- NOT active: %s" % (", ".join("%s (%s)" % (k, sv[k]) for k in bad) or "none"), "- failed units: %s" % (", ".join(failed) or "none")]
dk = sh("docker ps --format '{{.Names}} {{.Status}}' 2>/dev/null"); md += ["- containers: %s" % (dk.replace("\n", "; ") or "none seen")]
# repo / sync / cron
last = sh("cd %s && git log -1 --format='%%h %%cr: %%s'" % R); out["repo"] = last
ms = os.path.join(H, "memory_sync.log"); mls = (sh("tail -1 %s" % ms) if os.path.exists(ms) else "never run")
cron = [re.sub(r"^.*?(\S*(?:/|)([\w.-]+\.(?:sh|py)))\b.*$", r"\2", l) for l in sh("crontab -l").splitlines() if l.strip() and not l.startswith("#")]
md += ["", "## Sync and schedule", "- Pi repo copy at: %s" % last, "- last notes sync result: %s" % mls, "- cron jobs (script names): %s" % (", ".join(cron) or "none")]
out["sync"] = mls; out["cron"] = len(cron)
# markets
md_dir = os.path.join(H, "market-data"); mk = {"data_age": age(os.path.join(md_dir, "market.json"))}
live = None
try:
    c = json.load(open(os.path.join(md_dir, "config.json")))
    live = {k: v for k, v in c.items() if "live" in k.lower() and isinstance(v, (bool, str, int))}
except Exception: pass
mk["live"] = live; out["markets"] = mk
md += ["", "## Markets agent (practice money)", "- data last written: %s; live flags: %s" % (hrs(mk["data_age"]), json.dumps(live) if live is not None else "unreadable")]
pg = os.path.join(md_dir, "progress.txt")
if os.path.exists(pg): md += ["- supervisor report (%s), first lines:" % hrs(age(pg))] + ["    " + l for l in open(pg).read().splitlines()[:25]]
# jarvis
d = os.path.join(H, "voice-data"); tr = []
try:
    for l in open(os.path.join(d, "trace.jsonl")):
        try: tr.append(json.loads(l))
        except ValueError: pass
except OSError: pass
day = [r for r in tr if r.get("t", 0) > now - 86400]
hang = {}
for r in day:
    if r["kind"] == "hangup": hang[r["why"]] = hang.get(r["why"], 0) + 1
first = [r["since_heard"] for r in day if r["kind"] == "sentence" and r.get("n") == 0]
turns = sum(1 for r in day if r["kind"] == "heard"); errs = sum(1 for r in day if r["kind"] == "error"); blips = sum(1 for r in day if r["kind"] == "noise_blip")
lastact = (now - tr[-1]["t"]) / 3600.0 if tr else None
J = {"turns24": turns, "hangups": hang, "errors": errs, "blips": blips, "first_avg": round(sum(first) / len(first), 1) if first else None, "first_max": round(max(first), 1) if first else None, "last_h": lastact}
out["jarvis"] = J
md += ["", "## Jarvis (phone voice), last 24 h", "- turns: %d; errors: %d; ignored blips: %d; last activity: %s" % (turns, errs, blips, hrs(lastact)), "- hang-ups: %s" % (", ".join("%s x%d" % kv for kv in hang.items()) or "none"),
       "- time to first words: %s" % ("avg %.1fs, slowest %.1fs over %d answers" % (J["first_avg"], J["first_max"], len(first)) if first else "no answers logged yet")]
# pi-hole
try:
    import sys; sys.path.insert(0, os.path.join(R, "voice")); import tools
    ph = tools.pihole()
except Exception: ph = "unknown"
out["pihole"] = ph; md += ["", "## Pi-hole", "- " + ph]
# memory notes
nm = len(glob.glob(os.path.join(H, "voice-data", "memory", "*.md"))); md += ["", "## Notes", "- Jarvis note files: %d (synced to memory/inbox)" % nm]
out["time"] = now
open(os.path.join(R, "memory", "inbox", "pi-status.md"), "w").write("\n".join(md) + "\n")
json.dump(out, open(os.path.join(R, "hub-extra.json"), "w"))
print("\n".join(md))
PY
