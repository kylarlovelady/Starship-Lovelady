#!/bin/bash
# QUEUE-OK
# Where is the Starship page (crew-web/index.html) actually served? Read-only.
cd ~/hub-dashboard
echo "== routes/mounts in server.py"; grep -n -i -E "crew-web|StaticFiles|mount\(|@app\.(get|post)|include_router|FileResponse" server.py | cut -c1-170 | head -40
echo "== listeners"; ss -ltn 2>/dev/null | awk 'NR>1{print $4}' | sort -u | head -30
echo "== other http servers"; ps aux | grep -E "http.server|crew-web|8082|8083|8090" | grep -v grep | cut -c1-200 | head -6
echo "== tailscale serve"; tailscale serve status 2>&1 | head -12
