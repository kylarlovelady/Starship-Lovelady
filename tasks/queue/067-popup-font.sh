#!/bin/bash
# QUEUE-OK
# home screen: the reply pop-up (You / Alexa lines) uses the normal font, not the clock font
F=~/hub-dashboard/index.html
[ -f "$F.bak-popupfont" ] || cp "$F" "$F.bak-popupfont"
python3 - <<'PY'
import os
p = os.path.expanduser("~/hub-dashboard/index.html"); s = open(p).read()
rule = '#you,#ai,.lbl{font-family:"Segoe UI",system-ui,sans-serif!important}'
if rule in s: print("already patched")
elif "#ai{" in s: open(p, "w").write(s.replace("#ai{", rule + "#ai{", 1)); print("patched: pop-up text now uses the normal font")
else: print("could not find #ai rule")
PY
grep -c 'Segoe UI",system-ui,sans-serif!important' "$F"
