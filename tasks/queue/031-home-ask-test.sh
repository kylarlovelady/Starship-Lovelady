#!/bin/bash
# QUEUE-OK
# Read-only-ish: how long does Jarvis take to answer a home (text) question, and what did the last home asks get back?
echo "== last 10 text asks (home/Siri) from the log"; python3 - <<'PY'
import json,os,time
rows=[]
for l in open(os.path.expanduser("~/voice-data/conversations.jsonl")):
    try: r=json.loads(l)
    except ValueError: continue
    if r.get("sid")=="siri": rows.append(r)
for r in rows[-10:]:
    print(time.strftime("%H:%M:%S",time.localtime(r.get("t",0))),"secs",r.get("secs"),"|",str(r.get("heard"))[:60],"->",str(r.get("reply"))[:90],"| times",str(r.get("times"))[:80])
PY
echo "== live timing test"
for q in "What time is it" "What do you know about Sheree"; do
  s=$(date +%s.%N)
  out=$(curl -s -m 60 -X POST http://127.0.0.1:8099/ask -H 'Content-Type: application/json' -d "{\"format\":\"json\",\"text\":\"$q\",\"audio\":false,\"source\":\"home\"}")
  e=$(date +%s.%N); printf "%s -> %.1fs: %s\n" "$q" "$(echo "$e - $s" | bc)" "$(echo "$out" | cut -c1-260)"
done
echo "== HA jarvis_hub warnings (6h)"; docker logs --since 6h homeassistant 2>&1 | grep -i -E "jarvis_hub|could not reach|brain" | tail -6 | cut -c1-240
echo "== watchdog log (satellite restarts)"; journalctl -u hub-watchdog -n 12 --no-pager 2>&1 | cut -c1-200
