#!/bin/bash
# QUEUE-OK
# Kalshi practice wallet: fresh start (soft reset, same as the Fresh start button): new $1,000 run record, keeps everything the agent learned. Practice money only; refuses if a live session is active.
R=$(curl -s -m 10 -X POST -H "X-Crew: 1" -H "Content-Type: application/json" -d '{"confirm":true,"soft":true}' http://127.0.0.1:8097/reset)
echo "reset reply: $R"
sleep 5
curl -s -m 10 http://127.0.0.1:8097/live > /tmp/live-after.json
python3 -c "import json;d=json.load(open('/tmp/live-after.json'));print({k:d.get(k) for k in list(d)[:12]})"
cat ~/market-data/run.json 2>/dev/null
