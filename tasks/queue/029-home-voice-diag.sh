#!/bin/bash
# QUEUE-OK
# Read-only: why does Jarvis at home misbehave? Services, recent errors, Jarvis Hub in Home Assistant, containers.
echo "== services"; for s in hub-satellite hub-voice phone-voice hub-dashboard hub-watchdog; do echo "$s: $(systemctl is-active $s)"; done
echo "== containers"; docker ps --format '{{.Names}} {{.Status}}' 2>/dev/null
echo "== hub-satellite log (last 25)"; journalctl -u hub-satellite -n 25 --no-pager 2>&1 | cut -c1-200 | tail -25
echo "== hub-voice log (last 15)"; journalctl -u hub-voice -n 15 --no-pager 2>&1 | cut -c1-200 | tail -15
echo "== phone-voice errors today"; journalctl -u phone-voice --since "2 hours ago" --no-pager 2>&1 | grep -i -E "error|traceback|fail|exception" | tail -8 | cut -c1-220
echo "== HA log, jarvis/assist/wake lines"; docker logs --since 2h homeassistant 2>&1 | grep -i -E "jarvis|assist|wyoming|conversation|satellite|wake" | tail -15 | cut -c1-240
echo "== jarvis trace, last 14 events"; tail -14 ~/voice-data/trace.jsonl 2>/dev/null | python3 -c "
import sys,json,time
for l in sys.stdin:
    try: r=json.loads(l)
    except: continue
    print(time.strftime('%H:%M:%S',time.localtime(r.get('t',0))),r.get('kind'),str({k:v for k,v in r.items() if k not in ('t','kind')})[:130])"
