#!/bin/bash
# QUEUE-OK
# Read-only: what is the "run" wallet actually following, and did the cap change take effect?
python3 - <<'PY'
import json,os,time
d=json.load(open(os.path.expanduser("~/crew-web/market.json")));r=(d.get("sim") or {}).get("run") or {}
print("strategy:",r.get("strategy"),"| using:",r.get("using"),"| status:",r.get("status"),"| halt:",r.get("halt"))
for x in (r.get("autolog") or [])[-6:]: print("autolog",x)
print("cap in config shown:",d.get("config",{}).get("cap") if isinstance(d.get("config"),dict) else None)
for x in (r.get("rounds") or [])[-6:]: print(time.strftime("%H:%M",time.localtime(x.get("t") or 0)),x.get("staked"),x.get("pnl"))
PY
ps -eo lstart,cmd | grep "[c]ollector.py" | cut -c1-120
