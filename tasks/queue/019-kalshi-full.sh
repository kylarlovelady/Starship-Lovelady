#!/bin/bash
# QUEUE-OK
# Read-only Kalshi analysis: maker study (fixed), 24 h and 72 h reviews, real live orders summary, agent state.
cd ~/starship/markets || exit 1
echo "=== maker study (3 days)"; timeout 120 python3 maker_study.py 3 2>&1 | head -c 3500
echo; echo "=== review 24h (tail)"; timeout 200 python3 review.py 24 2>&1 | head -c 4500
echo; echo "=== review 72h strategy table"; timeout 200 python3 review.py 72 2>&1 | head -c 3500
echo; echo "=== real live orders (Nov 2)"; python3 - <<'PY'
import json,os,collections
rows=[json.loads(l) for l in open(os.path.expanduser("~/market-data/live_orders.jsonl")) if l.strip()]
print(len(rows),"rows; keys:",sorted(rows[0].keys()) if rows else None)
c=collections.Counter((r.get("action"),r.get("side")) for r in rows); print(dict(c))
for r in rows[:3]+rows[-3:]: print(json.dumps(r)[:380])
PY
echo; echo "=== my_trades"; timeout 60 python3 my_trades.py 2>&1 | head -c 2500
echo; echo "=== agent state"; python3 - <<'PY'
import json,os
d=json.load(open(os.path.expanduser("~/crew-web/market.json")))
r=(d.get("sim") or {}).get("run") or {}
print({k:r.get(k) for k in ("strategy","bal","pnl","windows","wins","active","live")})
print("cap check, last 10 staked:",[x.get("staked") for x in (r.get("rounds") or [])[-10:]])
PY
