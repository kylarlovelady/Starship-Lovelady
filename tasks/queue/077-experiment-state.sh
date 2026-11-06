#!/bin/bash
# QUEUE-OK
# read-only: what the practice wallet and experiments are doing now (no secrets)
echo "== run.json"; python3 - <<'PY'
import json, os
try:
    r = json.load(open(os.path.expanduser("~/market-data/run.json")))
    print({k: r.get(k) for k in ("active", "live", "strategy", "start", "id", "halted")})
except Exception as e:
    print("run.json:", e)
PY
echo "== sniper switch file"; ls -l ~/market-data/sniper.on 2>&1 | head -1
echo "== review 12h"; python3 ~/starship/markets/review.py 12 2>&1 | head -55 | cut -c1-200
