#!/bin/bash
# QUEUE-OK
cd ~/hub-dashboard || exit 0
echo "== index.html lines 1-40 (cut 330)"; sed -n 1,40p index.html | cut -c1-330
echo "== theme.html"; cat theme.html | cut -c1-400
echo "== how theme.html is used"; grep -n "theme.html" server.py *.py 2>/dev/null | cut -c1-160 | head -5
echo "== settings.json (colors/fonts/sizes only)"; python3 -c "
import json;d=json.load(open('settings.json'))
print({k:v for k,v in d.items() if any(x in k.lower() for x in ('color','font','size','bg','weight','style','glass','blur'))})
print('all keys:',sorted(d.keys()))"
