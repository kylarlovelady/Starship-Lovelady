#!/bin/bash
# Pulls ALL the Kalshi data the agents need onto the Pi, automatically, and writes a coverage report for Claude.
#   1. old rounds + Kalshi minute prices + Bitcoin minutes (markets/backfill.py: resumable, only fetches what is missing, read-only)
#   2. YOUR real Kalshi fills (markets/my_trades.py: read-only; skipped quietly if the Kalshi key is not set up)
#   3. coverage report -> memory/inbox/kalshi-data-status.md (counts and date ranges only, no keys, no balances)
# Install the daily run (4:10 am) with:  bash ~/starship/tasks/kalshi_data_sync.sh install
# Run now:                               bash ~/starship/tasks/kalshi_data_sync.sh
if [ "$1" = "install" ]; then
  ( crontab -l 2>/dev/null | grep -v kalshi-data-sync; echo "10 4 * * * flock -n /tmp/kalshi_sync.lock bash \$HOME/starship/tasks/kalshi_data_sync.sh >> \$HOME/market-data/kalshi_sync.log 2>&1 # kalshi-data-sync" ) | crontab -
  echo "Installed: Kalshi data sync runs every day at 4:10 am. Log: ~/market-data/kalshi_sync.log"; exit 0
fi
cd ~/starship/markets 2>/dev/null || exit 1
mkdir -p ~/market-data
echo "=== $(date '+%F %T') Kalshi data sync ==="
echo "-- old rounds and prices (30 days, up to 20 min)"; timeout 1500 python3 backfill.py 30 1200 2>&1 | tail -6
echo "-- your real fills"; timeout 300 python3 my_trades.py 2>&1 | tail -4
echo "-- daily digest for Claude and Jarvis (practice results only)"
{ echo "# Kalshi practice agent digest (auto, daily, last 24 h; practice money only)"; echo; timeout 180 python3 review.py 24 2>&1 | grep -v -i -E "balance|key|token|secret" | head -70; } > ~/starship/memory/inbox/kalshi-digest.md
python3 - <<'PY'
import glob, gzip, json, os, time
D = os.path.expanduser("~/market-data"); H = os.path.join(D, "history"); R = os.path.expanduser("~/starship/memory/inbox")
def rows(p):
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: yield json.loads(l)
                except ValueError: pass
    except OSError: return
def span(path, key):
    n = 0; lo = hi = None
    for r in rows(path):
        n += 1; v = r.get(key)
        if isinstance(v, (int, float)): lo = v if lo is None else min(lo, v); hi = v if hi is None else max(hi, v)
    return n, lo, hi
d = lambda t: time.strftime("%Y-%m-%d %H:%M", time.localtime(t)) if t else "-"
L = ["# Kalshi data on the Pi (auto, counts only)", ""]
for name, key in (("rounds.jsonl", "close_ts"), ("candles.jsonl", "t"), ("btc1m.jsonl", "t")):
    p = os.path.join(H, name); n, lo, hi = span(p, key) if os.path.exists(p) else (0, None, None)
    L.append("- history/%s: %d rows%s" % (name, n, (", %s to %s" % (d(lo), d(hi))) if lo and lo > 1e9 else ""))
for name in ("snapshots.jsonl", "sim_windows.jsonl", "calls.jsonl", "live_orders.jsonl"):
    p = os.path.join(D, name); n = sum(1 for _ in rows(p)) if os.path.exists(p) else 0
    L.append("- %s: %d rows, last written %s" % (name, n, d(os.path.getmtime(p)) if os.path.exists(p) else "never"))
tk = sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*")))
L.append("- per-second recordings: %d day files, %s to %s" % (len(tk), os.path.basename(tk[0]) if tk else "-", os.path.basename(tk[-1]) if tk else "-"))
mt = os.path.join(D, "my_trades.json")
try:
    j = json.load(open(mt)); L.append("- your real fills file: updated %s (%s)" % (d(os.path.getmtime(mt)), ", ".join("%s=%s" % (k, len(v) if isinstance(v, (list, dict)) else v) for k, v in list(j.items())[:4])))
except Exception: L.append("- your real fills file: not available yet (needs the Kalshi key; see memory/kalshi-ai.md)")
du = os.popen("du -sh %s 2>/dev/null | cut -f1" % D).read().strip(); df = os.popen("df -h / | awk 'NR==2{print $4\" free\"}'").read().strip()
L += ["- market-data size: %s; Pi disk: %s" % (du, df), "", "Agents and Claude can use all of this: replay.py, hypothesis.py, lab.py, review.py read from these files."]
open(os.path.join(R, "kalshi-data-status.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
PY
