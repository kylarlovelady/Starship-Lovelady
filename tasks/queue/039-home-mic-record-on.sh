#!/bin/bash
# QUEUE-OK
# Home speaker: turn mic recording on and KEEP it if healthy (038 showed it works; 037 misjudged because the old process's shutdown trace matched "Error"). Rolls back if unhealthy.
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
pkill -f "wyoming_satellite"; sleep 45
LOG=$(journalctl -u hub-satellite -n 60 --no-pager 2>&1 | awk '/Started hub-satellite/{buf=""} {buf=buf"\n"$0} END{print buf}')
ok=1; [ "$(systemctl is-active hub-satellite)" = "active" ] || ok=0
echo "$LOG" | grep -q "Waiting for wake word" || ok=0
echo "$LOG" | grep -q "Recording audio" || ok=0
if [ $ok = 1 ]; then echo "HEALTHY with recording on"; else cp run-hub.sh.bak-good run-hub.sh; pkill -f "wyoming_satellite"; sleep 12; echo "NOT healthy: rolled back"; fi
systemctl is-active hub-satellite
echo "$LOG" | tail -5 | cut -c1-150
