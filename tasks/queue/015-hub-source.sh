#!/bin/bash
# QUEUE-OK
# Read-only: show the Hub page and its API so the two sites can be merged into one.
cd ~/hub-dashboard 2>/dev/null || exit 1
echo "== hub_api.py"; cat hub_api.py
echo "== hub.html (tabs and script, trimmed)"; sed -e 's/[[:space:]]\+/ /g' hub.html | cut -c1-400 | head -80
echo "== routers"; ls *_api.py
echo "== market.json run wallet"; python3 - <<'PY'
import json,os
d=json.load(open(os.path.expanduser("~/crew-web/market.json")))
r=(d.get("sim") or {}).get("run") or {}
print({k:r.get(k) for k in ("bal","pnl","windows","strategy","start","active")})
PY
echo "== collector live"; curl -s -m 5 http://100.105.140.126:8097/live | head -c 300
