#!/bin/bash
# QUEUE-OK
# Read-only: are the cap 25 and the new Auto rule running?
head -2 ~/starship/markets/collector.py | tail -1 | cut -c1-60
(cd ~/starship && git log -1 --format='Pi repo: %h %cr')
python3 - <<'PY'
import json,os,time
d=json.load(open(os.path.expanduser("~/crew-web/market.json")));r=(d.get("sim") or {}).get("run") or {}
print("using:",r.get("using"),"| status:",r.get("status"))
for x in (r.get("autolog") or [])[-3:]: print("autolog",time.strftime("%H:%M",time.localtime(x["t"])),x["to"],"-",x["why"][:90])
for x in (r.get("rounds") or [])[-5:]: print(time.strftime("%H:%M",time.localtime(x.get("t") or 0)),"staked",x.get("staked"),"pnl",x.get("pnl"))
PY
