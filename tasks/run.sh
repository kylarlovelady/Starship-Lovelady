#!/bin/bash
# Read-only: every order the agent sent in the last live session, and what Kalshi answered. Also your Smallest-bet setting.
python3 - <<'PY'
import json, os, re, time
D = os.path.expanduser("~/market-data")
hm = lambda t: time.strftime("%H:%M:%S", time.localtime(t))
start = None
for l in open(os.path.join(D, "alerts.log")):
    m = re.match(r"(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) ", l)
    if m and "live started" in l.lower(): start = time.mktime(time.strptime(m.group(1), "%Y-%m-%d %H:%M:%S"))
print("session started", hm(start) if start else "?")
n_ord = n_slip = n_fill = 0
for l in open(os.path.join(D, "live_orders.jsonl")):
    try: o = json.loads(l)
    except Exception: continue
    if "slip_cents" in o: n_slip += 1
    if "action" not in o or not start or o["t"] < start - 30: continue
    n_ord += 1
    n_fill += 1 if float((o.get("reply") or {}).get("fill_count") or 0) > 0 else 0
    r = o.get("reply") or {}
    print("%s %-4s %-4s want %s @%.2f  status %s  filled %s of %s  %s" % (hm(o["t"]), o["action"], o.get("side"), o.get("count"), o.get("price") or 0, o.get("status"),
          r.get("fill_count"), r.get("count") or o.get("count"), (r.get("error") or r.get("message") or "")[:60]))
print("\nTOTAL: %d order lines, %d with at least one contract filled (the file also holds %d slippage notes, which are not orders)" % (n_ord, n_fill, n_slip))
try:
    c = json.load(open(os.path.join(D, "config.json")))
    print("\nconfig.json:", {k: c.get(k) for k in ("min_bet", "cap", "floor", "aggression")})
except Exception as e:
    print("no config.json (defaults in use)")
try:
    es = json.load(open(os.path.join(D, "entry_stats.json")))
    print("\nENTRY EVIDENCE (buy either side at the price shown, hold to the end, after fees) from %d finished rounds:" % es["rounds"])
    for k, v in es["price"].items():
        print("  %-7s c: %5d samples, %3d rounds, win %2d%%, avg %+5.1f c per contract" % (k, v["n"], v["rounds"], round(100 * v["win"]), 100 * v["avg"]))
    print("  blocked price ranges:", es["block"] or "none yet (needs 25+ rounds per range)")
    hs = es.get("hours") or {}
    if hs: print("  by hour of day (local, 35-80c entries):", ", ".join("%sh %+.1fc" % (h, 100 * v["avg"]) for h, v in sorted(hs.items(), key=lambda x: int(x[0]))))
    cal = json.load(open(os.path.join(D, "calendar.json")))
    print("  news calendar: %d big US events this week%s" % (len(cal.get("events", [])), (" (fetch failed: %s)" % cal["err"]) if cal.get("err") else ""))
except Exception as e:
    print("entry evidence not built yet:", e)
import glob
fs = sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*")))
if fs:
    last = fs[-1]; print("recorder: %d files, newest %s (%.1f MB), updated %d s ago" % (len(fs), os.path.basename(last), os.path.getsize(last) / 1e6, time.time() - os.path.getmtime(last)))
else:
    print("recorder: no tick files yet")
try:
    import subprocess
    tail = subprocess.run("tail -n 1 " + last, shell=True, capture_output=True, text=True).stdout
    row = json.loads(tail)
    print("latest tick, errors:", row.get("err"), "| Kalshi:", row.get("k"), "| book:", row.get("ob"))
except Exception as e:
    print("tick sample unavailable:", e)
PY
cd ~/starship/markets 2>/dev/null && python3 ticks_report.py 2>&1 | head -40
