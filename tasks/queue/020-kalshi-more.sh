#!/bin/bash
# QUEUE-OK
# Read-only: key strategies over 72 h and 24 h, run's recent bet sizes (is the $25 cap working?), real live orders summary.
cd ~/starship/markets || exit 1
for H in 72 12; do echo "=== key strategies, last $H h"; timeout 200 python3 review.py $H 2>&1 | grep -E "^ +(v_hold|hold|run|v_late|v_one_shot|v_cut_loose|v_no_cut|v_cut_tight|v_trail|v_adds|distance|mood|flow|swing|trend|signals) " ; done
echo; echo "=== run, recent rounds (is the cap working?)"; python3 - <<'PY'
import json,os,time
d=json.load(open(os.path.expanduser("~/crew-web/market.json")))
r=(d.get("sim") or {}).get("run") or {}
print({k:r.get(k) for k in ("strategy","bal","pnl","windows","active","live")})
for x in (r.get("rounds") or [])[-14:]: print(time.strftime("%a %H:%M",time.localtime(x.get("t") or 0)) if x.get("t") else "", {k:x.get(k) for k in ("staked","pnl","side","strategy") if k in x})
PY
echo; echo "=== collector restart / version"; systemctl show market-agent -p ActiveEnterTimestamp 2>/dev/null; head -2 collector.py | tail -1 | cut -c1-120
echo; echo "=== real live orders"; python3 - <<'PY'
import json,os,collections
rows=[json.loads(l) for l in open(os.path.expanduser("~/market-data/live_orders.jsonl")) if l.strip()]
print(len(rows),"rows; keys:",sorted(rows[0].keys()))
print(dict(collections.Counter((r.get("action"),r.get("side")) for r in rows)))
for r in rows[:2]+rows[-2:]: print(json.dumps(r)[:330])
PY
echo; echo "=== my real trades"; timeout 60 python3 my_trades.py 2>&1 | head -c 1800
