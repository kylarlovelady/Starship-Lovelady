#!/bin/bash
# QUEUE-OK
# Home speaker: record what the mic hears (clips stay on the Pi), turn on mild noise suppression, then restart the satellite. Backup first; safe to run twice.
cd ~/wyoming-satellite || exit 1
mkdir -p ~/voice-data/home-mic
echo "== options present?"; script/run --help 2>/dev/null | grep -E "debug-recording-dir|mic-noise-suppression" | cut -c1-120
echo "== hub-mic.py (gain/level lines)"; grep -n -i -E "vol|gain|mult|rate|ratecv|audioop|\*" ~/hub-mic.py | cut -c1-160 | head -14
[ -f run-hub.sh.bak-mic ] || cp run-hub.sh run-hub.sh.bak-mic
python3 - <<'PY'
p="run-hub.sh"; s=open(p).read(); add=[]
if "--debug-recording-dir" not in s: add.append("--debug-recording-dir '/home/kylarlovelady/voice-data/home-mic' \\")
if "--mic-noise-suppression" not in s: add.append("--mic-noise-suppression 2 \\")
if add:
    s=s.replace("--name 'main hub' \\\n","--name 'main hub' \\\n"+"\n".join(add)+"\n",1); open(p,"w").write(s); print("added:",add)
else: print("already set")
PY
bash -n run-hub.sh && echo "syntax ok" || { cp run-hub.sh.bak-mic run-hub.sh; echo "syntax bad, restored"; exit 1; }
pkill -f "wyoming_satellite" ; sleep 8
echo "== satellite now"; systemctl is-active hub-satellite; journalctl -u hub-satellite -n 4 --no-pager 2>&1 | cut -c1-160
python3 ~/starship/tasks/home_mic_report.py 2>&1 | head -8
