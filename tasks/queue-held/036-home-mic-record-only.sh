#!/bin/bash
# QUEUE-OK
# Home speaker: switch on mic recording only (no noise suppression yet), restart, and ROLL BACK automatically if it does not come up healthy.
cd ~/wyoming-satellite || exit 1
mkdir -p ~/voice-data/home-mic
[ -f run-hub.sh.bak-good ] || cp run-hub.sh run-hub.sh.bak-good
python3 - <<'PY'
p="run-hub.sh"; s=open(p).read()
if "--debug-recording-dir" not in s:
    s=s.replace("--name 'main hub' \\\n","--name 'main hub' \\\n--debug-recording-dir '/home/kylarlovelady/voice-data/home-mic' \\\n",1); open(p,"w").write(s); print("recording flag added")
else: print("already set")
PY
bash -n run-hub.sh || { cp run-hub.sh.bak-good run-hub.sh; echo "syntax bad, restored"; exit 1; }
pkill -f "wyoming_satellite"; sleep 14
ok=1; [ "$(systemctl is-active hub-satellite)" = "active" ] || ok=0
journalctl -u hub-satellite --since "20 seconds ago" --no-pager 2>&1 | grep -q -E "Traceback|Error" && ok=0
journalctl -u hub-satellite --since "20 seconds ago" --no-pager 2>&1 | grep -q "Waiting for wake word" || ok=0
if [ $ok = 1 ]; then echo "HEALTHY with recording on"; else cp run-hub.sh.bak-good run-hub.sh; pkill -f "wyoming_satellite"; sleep 10; echo "NOT healthy: rolled back"; fi
systemctl is-active hub-satellite; journalctl -u hub-satellite -n 3 --no-pager 2>&1 | cut -c1-150
