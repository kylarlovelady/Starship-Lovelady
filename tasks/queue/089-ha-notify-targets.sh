#!/bin/bash
# QUEUE-OK
# read-only: which phones Home Assistant can notify, and which automations/scripts send notifications (so alerts go to Kylar only)
ENVF=$HOME/market-data/env
TOKEN=$(grep -a '^HA_TOKEN=' $ENVF | cut -d= -f2-); URL=$(grep -a '^HA_URL=' $ENVF | cut -d= -f2-); URL=${URL:-http://127.0.0.1:8123}
[ -z "$TOKEN" ] && { echo "no HA_TOKEN on the Pi"; exit 0; }
echo "== phones HA can notify (notify.mobile_app_...)"
curl -s -m 10 -H "Authorization: Bearer $TOKEN" $URL/api/services | python3 -c "
import sys,json
for d in json.load(sys.stdin):
    if d.get('domain')=='notify':
        print(' '.join(sorted(s for s in d.get('services',{}) if s.startswith('mobile_app_'))) or 'none')"
echo "== persons and their phones (device trackers)"
curl -s -m 10 -H "Authorization: Bearer $TOKEN" $URL/api/states | python3 -c "
import sys,json
for e in json.load(sys.stdin):
    i=e['entity_id']
    if i.startswith('person.') or (i.startswith('device_tracker.') and 'phone' in i or 'iphone' in i): print(i, e['state'], e['attributes'].get('friendly_name',''))" | head -20
echo "== current alert_phone.txt"; cat $HOME/market-data/alert_phone.txt 2>/dev/null || echo "(none yet: alerts go to every phone)"
echo "== automations and scripts that mention notify (names only)"
cd $HOME && grep -rIl "notify\." ~/homeassistant ~/ha ~/config /opt/homeassistant 2>/dev/null | head -10
docker ps --format '{{.Names}}' | head -10
