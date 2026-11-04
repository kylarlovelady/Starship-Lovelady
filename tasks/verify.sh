#!/bin/bash
# Read-only: is the newest market-agent code on this Pi, and is the agent running it?
cd ~/starship || exit 1
git pull -q 2>&1 | tail -1
echo "commit:  $(git log --oneline | head -1)"
echo "marker:  $(sed -n 2p markets/collector.py)"
chk() { if grep -q "$2" "markets/$1"; then echo "  OK       $3"; else echo "  MISSING  $3"; fi; }
chk sim.py "UNPROVEN_CAP = " "stake cap until proven (\$50 per round)"
chk sim.py "ODDS_MARGIN = 0.04" "odds-sell margin 4c"
chk sim.py "v_mood_flip" "mood / flow flip tests"
chk sim.py "def load_dynamic" "live experiments (innovator) loader"
chk sim.py "FLOOR = 5.0" "\$5 minimum bet"
chk sim.py "MIN_PROFIT_USD = 5.0" "\$5 minimum profit to sell a winner"
chk sim.py "STOP_SMALL = " "smart loss cut"
chk collector.py "trend_24h" "separate trend signals"
chk supervisor.py "innovate.main" "supervisor runs the innovator"
test -f markets/innovate.py && echo "  OK       innovate.py present" || echo "  MISSING  innovate.py"
echo
echo "agent restarts (newest 3):"; journalctl -u market-agent --since "6 hours ago" 2>/dev/null | grep -i "collector updated" | tail -3
python3 - <<'PY'
import json, os, time
D = os.path.expanduser("~/market-data")
try:
    c = json.load(open(os.path.join(D, "config.json")))
    print("settings in use: cap", c.get("cap"), "| unproven_cap", c.get("unproven_cap", "50 (default)"), "| min_bet", c.get("min_bet"))
except Exception as e:
    print("config.json:", e)
n = 0; small = 0; big = 0; last = None
try:
    for l in open(os.path.join(D, "trades.jsonl")):
        try: r = json.loads(l)
        except ValueError: continue
        if r.get("a") == "BUY" and not r.get("live") and (r.get("t") or 0) > time.time() - 1800:
            d = r["c"] * r["px"]; n += 1; small += d < 4.99; big = max(big, d)
except OSError: pass
print("buys in the last 30 min: %d | under $5: %d | biggest: $%.0f" % (n, small, big))
for f, lab in (("variants.json", "live experiments"), ("innovations.jsonl", "innovator log")):
    p = os.path.join(D, f)
    print("%s: %s" % (lab, ("updated %d min ago" % ((time.time() - os.path.getmtime(p)) / 60)) if os.path.exists(p) else "not created yet (appears after the next hourly check)"))
PY
