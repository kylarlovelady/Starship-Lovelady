#!/bin/bash
# Home Jarvis wake word THRESHOLD change (used by Claude's reviews and by hand). Usage: bash ~/starship/tasks/jarvis_tune.sh 0.8 "why"
# Recreates ONLY the openwakeword container with the same image and a new --threshold, checks it is listening on 10400 again, and puts the old value back if not.
# Keeps threshold between 0.55 and 0.92. Restarts the satellite (kill; systemd brings it back) so it reconnects. Logs to ~/voice-data/tune-log.jsonl.
NEW="$1"; WHY="${2:-manual}"
python3 -c "import sys;v=float(sys.argv[1]);sys.exit(0 if 0.55<=v<=0.92 else 1)" "$NEW" || { echo "threshold must be 0.55 to 0.92"; exit 1; }
OLD=$(docker inspect openwakeword --format '{{join .Args " "}}' | grep -o -E 'threshold +[0-9.]+' | awk '{print $2}')
echo "old threshold: $OLD new: $NEW"
[ "$OLD" = "$NEW" ] && { echo "no change"; exit 0; }
run_with() { docker rm -f openwakeword >/dev/null 2>&1; docker run -d --name openwakeword --restart unless-stopped -p 127.0.0.1:10400:10400 rhasspy/wyoming-openwakeword --uri tcp://0.0.0.0:10400 --preload-model alexa --threshold "$1" >/dev/null 2>&1; sleep 6; ss -ltn | grep -q ':10400 '; }
if run_with "$NEW"; then
  echo "container up with threshold $NEW"
  python3 - "$OLD" "$NEW" "$WHY" <<'PY'
import json,sys,time,os
open(os.path.expanduser("~/voice-data/tune-log.jsonl"),"a").write(json.dumps({"t":time.time(),"from":sys.argv[1],"to":sys.argv[2],"why":sys.argv[3]})+"\n")
PY
  pkill -f wyoming_satellite; sleep 8; systemctl is-active hub-satellite
else
  echo "FAILED, putting back $OLD"; run_with "${OLD:-0.7}" && echo "restored $OLD" || echo "RESTORE FAILED: run docker ps and tell Claude"
fi
