#!/bin/bash
# QUEUE-OK
# read-only: how the home mic is read and whether a mute switch already exists (no keys printed)
echo "== run-hub.sh"; grep -v -i -E 'key|token|secret|pass' ~/wyoming-satellite/run-hub.sh | head -30
echo "== hub-mic.py"; wc -l ~/hub-mic.py; grep -v -i -E 'key|token|secret|pass' ~/hub-mic.py | head -70
echo "== mute mentions"; grep -n -i -E 'mute|muted' ~/hub-voice/voiced.py /usr/local/bin/hub-*.py ~/hub-mic.py ~/wyoming-satellite/run-hub.sh 2>/dev/null | cut -c1-200 | head -30
echo "== mixer Mic"; amixer -c 3 sget Mic 2>&1 | head -12
echo "== what listens on 8097"; ss -ltnp 2>/dev/null | grep -E ':8097|:8098' | cut -c1-160
echo "== wake clips per hour (last 24 h) and conversations"; python3 - <<'PY'
import glob,os,time,collections
c=collections.Counter()
for p in glob.glob(os.path.expanduser("~/voice-data/home-mic/**/*-wake.wav"),recursive=True):
    c[time.strftime("%m-%d %H",time.localtime(os.path.getmtime(p)))]+=1
for k in sorted(c)[-30:]: print(k,c[k])
print("total wake clips",sum(c.values()))
PY
echo "== conversations.jsonl keys of last row"; tail -1 ~/voice-data/conversations.jsonl | python3 -c "import sys,json;d=json.loads(sys.stdin.read());print(list(d.keys()))"
echo "== trace.jsonl last 3 rows (trimmed)"; tail -3 ~/voice-data/trace.jsonl | cut -c1-300
