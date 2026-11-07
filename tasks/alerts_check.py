#!/usr/bin/env python3
"""One alert channel. Runs every 5 minutes from cron (tasks/pi_update.sh installs it). Checks the Pi, services, markets data, Jarvis, Pi-hole,
and dated to-dos, and sends ONE phone alert per problem through Home Assistant (markets/alerts.py). Re-alerts every 6 h while a problem lasts and
says when it clears. Writes ~/starship/hub-alerts.json for the Starship page (git-ignored). Never raises. Keys stay on the Pi."""
import glob, json, os, re, subprocess, sys, time, urllib.request
H = os.path.expanduser("~"); R = os.path.join(H, "starship"); now = time.time()
sys.path.insert(0, os.path.join(R, "markets"))
try: import alerts as A
except Exception: A = None
STATE = os.path.join(H, "hub-alerts-state.json")
def sh(c, t=6):
    try: return subprocess.run(c, shell=True, capture_output=True, text=True, timeout=t).stdout.strip()
    except Exception: return ""
def age_h(p):
    try: return (now - os.path.getmtime(p)) / 3600.0
    except OSError: return None
try: st = json.load(open(STATE))
except Exception: st = {}
problems = {}      # key -> message
# services
for svc in ("market-agent", "phone-voice", "tailscaled", "docker", "hub-dashboard", "hub-watchdog"):
    if sh("systemctl list-unit-files %s.service --no-legend" % svc) and sh("systemctl is-active %s" % svc) != "active":
        problems["svc:" + svc] = "Service %s is not running." % svc
# Pi health
t = re.sub(r"[^\d.]", "", sh("vcgencmd measure_temp") or "")
if t and float(t) > 80: problems["temp"] = "Pi is hot: %s C." % t
m = re.search(r"(\d+)%", sh("df -h / | awk 'NR==2{print $5}'"))
if m and int(m.group(1)) > 90: problems["disk"] = "Pi disk is %s%% full." % m.group(1)
# markets data fresh
a = age_h(os.path.join(H, "crew-web", "market.json"))
if a is not None and a > 0.5: problems["markets"] = "Kalshi agent data is %.1f hours old (agent may be stuck)." % a
# Jarvis errors in the last 15 min
try:
    errs = 0
    for l in open(os.path.join(H, "voice-data", "trace.jsonl")):
        try: r = json.loads(l)
        except ValueError: continue
        if r.get("kind") == "error" and r.get("t", 0) > now - 900: errs += 1
    if errs >= 2: problems["jarvis"] = "Jarvis had %d errors in the last 15 minutes." % errs
except OSError: pass
# containers (Pi-hole, Home Assistant, voice helpers)
ups = {l.split()[0]: l for l in sh("docker ps --format '{{.Names}} {{.Status}}'").splitlines() if l.strip()}
if sh("docker ps -a --format '{{.Names}}'"):
    for c in ("pihole", "homeassistant", "whisper", "piper", "openwakeword"):
        if c not in ups: problems["ctr:" + c] = "Container %s is not running." % c
        elif "unhealthy" in ups[c]: problems["ctr:" + c] = "Container %s is unhealthy." % c
# repo copy stuck (cron pull failing)
last = sh("cd %s && git log -1 --format=%%ct" % R)
if last.isdigit() and now - int(last) > 3 * 86400 and sh("cd %s && git fetch -q 2>&1; git status -sb | head -1" % R).find("behind") >= 0: problems["pull"] = "The Pi has not pulled new code for 3 days."
# dated to-dos from memory/todo.md (Open section): lines like "- 2026-11-09: ..."
try:
    sec = open(os.path.join(R, "memory", "todo.md")).read().split("## Done")[0]
    today = time.strftime("%Y-%m-%d"); tom = time.strftime("%Y-%m-%d", time.localtime(now + 86400))
    for l in sec.splitlines():
        mm = re.match(r"^- (\d{4}-\d\d-\d\d)[^:]*:\s*(.+)$", l)
        if mm and mm.group(1) in (today, tom): problems["todo:" + mm.group(1) + mm.group(2)[:20]] = ("Today: " if mm.group(1) == today else "Tomorrow: ") + mm.group(2)[:140]
except OSError: pass
sent = []
PUSH = ("svc:", "temp", "disk", "ctr:", "pull")      # Kylar 2026-11-06: phone alerts ONLY when the Pi itself has a problem. Everything else stays on the Starship page.
for k, msg in problems.items():
    last = st.get(k, 0)
    if now - last > 6 * 3600:
        if not k.startswith(PUSH):
            st[k] = now; continue
        ok = A._send("Pi problem", msg) if A else False
        sent.append((k, ok)); st[k] = now if ok or not A else last
for k in [k for k in st if k not in problems and st[k]]:
    st.pop(k)
json.dump(st, open(STATE, "w"))
json.dump({"time": now, "active": list(problems.values())}, open(os.path.join(R, "hub-alerts.json"), "w"))
print("alerts: %d active, %d sent" % (len(problems), len(sent)))
try:
    import subprocess; subprocess.run(["python3", os.path.join(R, "tasks", "crew_report.py")], timeout=30, capture_output=True)
except Exception: pass
