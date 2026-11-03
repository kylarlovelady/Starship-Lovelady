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
shown = [0]
print("session started", hm(start) if start else "?")
n_ord = n_slip = n_fill = 0
for l in open(os.path.join(D, "live_orders.jsonl")):
    try: o = json.loads(l)
    except Exception: continue
    if "slip_cents" in o: n_slip += 1
    if "action" not in o or not start or o["t"] < start - 30: continue
    n_ord += 1
    if o.get("action") == "sell" and float((o.get("reply") or {}).get("fill_count") or 0) == 0 and shown[0] < 2:
        shown[0] += 1
        print("  FULL SELL ORDER + KALSHI REPLY:", json.dumps({k: o.get(k) for k in ("count", "price", "book_side", "quote_ask", "quote_bid")}), json.dumps(o.get("reply"))[:420])
    n_fill += 1 if float((o.get("reply") or {}).get("fill_count") or 0) > 0 else 0
    r = o.get("reply") or {}
    print("%s %-4s %-4s want %s @%.2f  status %s  filled %s of %s  %s" % (hm(o["t"]), o["action"], o.get("side"), o.get("count"), o.get("price") or 0, o.get("status"),
          r.get("fill_count"), r.get("count") or o.get("count"), (r.get("error") or r.get("message") or "")[:60]))
print("\nTOTAL: %d order lines, %d with at least one contract filled (the file also holds %d slippage notes, which are not orders)" % (n_ord, n_fill, n_slip))
try:
    c = json.load(open(os.path.join(D, "config.json")))
    print("config.json last written", time.strftime("%m-%d %H:%M:%S", time.localtime(os.path.getmtime(os.path.join(D, "config.json")))), "in", D)
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
try:
    xr = json.load(open(os.path.join(D, "exit_rules.json")))
    print("\nTAKE-PROFIT RULE: %s | sells once up %s c per contract and then falls %s c from the best point | source: %s (%s rounds studied)" % (
        "ON" if xr.get("enabled", True) else "OFF", xr.get("peak"), xr.get("drop"), xr.get("source"), xr.get("rounds")))
    if xr.get("audit"): print("  ", xr["audit"])
    if xr.get("exits_checked"): print("  real early exits checked:", xr["exits_checked"], "| average vs holding to the end: %+.1f c per contract" % (100 * xr.get("exit_vs_hold", 0)))
    for t in (xr.get("table") or [])[:3]: print("   tested peak %s / drop %s: %+.1f c better than holding (+/-%.1f), %s rounds" % (t["peak"], t["drop"], 100 * t["gain"], 100 * t["se"], t["rounds"]))
    if xr.get("note"): print("  ", xr["note"])
except Exception as e:
    print("take-profit rule: no file yet", e)
try:
    pt = json.load(open(os.path.join(D, "patterns.json")))
    print("\nHINDSIGHT PATTERNS (%d finished rounds studied)%s" % (pt.get("rounds", 0), (" | " + pt["note"]) if pt.get("note") else ""))
    if pt.get("baseline"): print("  an average entry after fees: train %+.1f c, test %+.1f c" % (100 * pt["baseline"]["train"], 100 * pt["baseline"]["test"]))
    for tag in ("bad", "good"):
        for r in pt.get(tag, [])[:6]: print("  %s: %s = %s  train %+.1f c, later rounds %+.1f c (%d/%d rounds)" % (tag.upper(), r["feature"], r["bucket"], 100 * r["train"], 100 * r["test"], r["n_train"], r["n_test"]))
    mem = sum(1 for _ in open(os.path.join(D, "hindsight.jsonl")))
    print("  hindsight memory: %d rounds stored" % mem)
except Exception as e:
    print("hindsight patterns: not built yet (%s)" % str(e)[:60])
try:
    import sys; sys.path.insert(0, os.path.expanduser("~/starship/markets")); import exit_learn
    ls = exit_learn.review(D)
    if ls: print("\nLOOK-BACK ON YOUR REAL POSITIONS:"); [print("  " + l) for l in ls]
except Exception as e:
    print("look-back unavailable:", e)
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
echo; echo "=== BACKTEST ON OLD ROUNDS ==="
cd ~/starship/markets 2>/dev/null && python3 replay.py --show 2>&1 | head -40

echo; echo "=== SIGNAL SCAN (second-by-second rounds) ==="
(cd "$(dirname "$0")/../markets" 2>/dev/null && python3 signals.py 2>&1 | tail -40)
