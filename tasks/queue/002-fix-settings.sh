#!/bin/bash
# QUEUE-OK
# Jarvis had OLD waits saved in his settings file, which override the new defaults (that is why he could still hang up). Set the new ones, then read-only facts.
curl -s -X POST localhost:8099/settings -H 'Content-Type: application/json' -d '{"follow_quiet":25,"follow_question":40,"silence_end":1.3}' | head -c 300; echo
echo "== market-data newest files"; ls -lt ~/market-data | head -14 | cut -c1-90
echo "== crew-web market file"; ls -l ~/crew-web/market.json 2>&1 | cut -c1-90
echo "== run.json keys"; python3 -c "import json,os;d=json.load(open(os.path.expanduser('~/market-data/run.json')));print({k:(v if isinstance(v,(bool,int,float)) or k in ('halted','detail') else '...') for k,v in d.items()})" 2>&1 | head -3
echo "== pihole"; docker exec pihole pihole -v 2>&1 | head -4
echo "== ha logs (jarvis_hub)"; docker logs homeassistant 2>&1 | grep -i -E "jarvis|custom integration" | tail -4 | cut -c1-200
echo "== jarvis conversations today"; python3 -c "
import json,os,time
n=0
for l in open(os.path.expanduser('~/voice-data/trace.jsonl')):
    r=json.loads(l)
    if r.get('t',0)>time.time()-86400 and r['kind'] in ('hangup','error','noise_blip','nothing_heard'): print(time.strftime('%H:%M:%S',time.localtime(r['t'])),r['kind'],r.get('why') or r.get('text') or r.get('count') or r.get('secs'))
" 2>&1 | tail -12
