#!/bin/bash
# QUEUE-OK
# read-only Kalshi practice review over 72 h and 7 days (practice money only), top and bottom of the table plus the run breakdown
cd ~/starship/markets || exit 1
for h in 72 168; do
  echo "=== review last $h hours"
  timeout 120 python3 review.py $h 2>&1 | cut -c1-230 | head -45
done
echo "=== config now"
python3 - <<'PY'
import json,os
D=os.path.expanduser("~/market-data")
for f in ("run.json","config.json"):
    p=os.path.join(D,f)
    try: print(f, json.dumps(json.load(open(p)))[:700])
    except Exception as e: print(f, "n/a", e)
PY
