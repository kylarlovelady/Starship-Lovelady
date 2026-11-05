#!/bin/bash
# QUEUE-OK
# Read-only: is the new Kalshi code (cap 25, evidence-gated Auto) actually running? What config overrides it?
cd ~/market-data 2>/dev/null || exit 1
echo "== collector process"; ps -eo pid,lstart,cmd | grep "[c]ollector.py" | cut -c1-160
echo "== repo head on Pi"; (cd ~/starship && git log -1 --format='%h %cr %s' | cut -c1-120)
echo "== config files (numbers only)"; for f in config.json control.json; do [ -f $f ] && { echo "-- $f"; python3 -c "import json,sys;d=json.load(open('$f'));print({k:v for k,v in d.items() if not any(s in k.lower() for s in ('key','token','pass','secret'))})" | cut -c1-900; }; done
echo "== auto log and pick"; python3 - <<'PY'
import json,os
d=json.load(open(os.path.expanduser("~/crew-web/market.json"))); s=d.get("sim") or {}
print("auto_pick:",s.get("auto_pick"))
for x in (s.get("autolog") or [])[-6:]: print(x)
print("cap shown:", d.get("cap"), (d.get("config") or {}).get("cap"), (d.get("config") or {}).get("unproven_cap"))
r=s.get("run") or {}; print("run keys:",sorted(r.keys())[:30])
PY
