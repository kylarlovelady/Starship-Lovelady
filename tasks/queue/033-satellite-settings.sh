#!/bin/bash
# QUEUE-OK
# Read-only: the home satellite's command line (mic, voice detection, wake word) and the watchdog's 'stuck' rule. No keys shown.
echo "== run-hub.sh"; sed -e 's/\(token\|key\|password\)[=:][^ ]*/\1=***/Ig' ~/wyoming-satellite/run-hub.sh | cut -c1-300
echo "== wyoming-satellite version / options"; ls ~/wyoming-satellite | head -20; ~/wyoming-satellite/.venv/bin/python -m wyoming_satellite --help 2>/dev/null | grep -E "^\s+--(vad|mic|wake|debug|snd|awake|done|timer|no-)" | cut -c1-110 | head -40
echo "== watchdog: stuck rule"; grep -n -i -E "stuck|listening|restart|sleep|state" /usr/local/bin/hub-watchdog.py | cut -c1-170 | head -30
echo "== mic device and level"; arecord -l 2>/dev/null | head -6; amixer -c 0 scontents 2>/dev/null | grep -E "Simple|Capture|%" | head -12 | cut -c1-120
