#!/bin/bash
# QUEUE-OK
# Diagnose why 037 judged unhealthy: apply recording flag, wait, dump the log, then ALWAYS roll back to the known-good run-hub.sh.
cd ~/wyoming-satellite || exit 1
mkdir -p ~/voice-data/home-mic
cp run-hub.sh /tmp/run-hub.cur
grep -n "debug-recording\|name 'main hub'" run-hub.sh
python3 - <<'PY'
p="run-hub.sh"; s=open(p).read()
if "--debug-recording-dir" not in s:
    s=s.replace("--name 'main hub' \\\n","--name 'main hub' \\\n--debug-recording-dir '/home/kylarlovelady/voice-data/home-mic' \\\n",1); open(p,"w").write(s)
PY
cat run-hub.sh | cut -c1-160
T=$(date '+%Y-%m-%d %H:%M:%S')
pkill -f "wyoming_satellite"; sleep 40
journalctl -u hub-satellite --since "$T" --no-pager 2>&1 | cut -c1-200 | tail -40
ls -la ~/voice-data/home-mic | head
cp /tmp/run-hub.cur run-hub.sh; pkill -f "wyoming_satellite"; sleep 20
systemctl is-active hub-satellite
journalctl -u hub-satellite -n 3 --no-pager 2>&1 | cut -c1-150
