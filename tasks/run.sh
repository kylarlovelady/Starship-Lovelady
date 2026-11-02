#!/bin/bash
# Adds a "Markets" tab to the Hub that shows the Live View. Makes a backup first. Safe to run twice.
cd ~/hub-dashboard || exit 1
python3 - <<'PY'
p="hub.html";t=open(p).read()
if 'data-t="markets"' in t:
    print("Markets tab is already there. Nothing changed.");raise SystemExit
a='<button data-t="crew">Control Room</button>'
b='<iframe id="crew" class="pane" data-src="http://loveladymainaihub.taild703ca.ts.net:8095/"></iframe>'
if t.count(a)!=1 or t.count(b)!=1:
    print("Hub layout is not what I expected. Nothing changed.");raise SystemExit
import shutil;shutil.copy(p,p+".bak-markets")
t=t.replace(a,a+'<button data-t="markets">Markets</button>')
t=t.replace(b,b+'<iframe id="markets" class="pane" data-src="http://loveladymainaihub.taild703ca.ts.net:8095/live.html"></iframe>')
open(p,"w").write(t);print("Added the Markets tab. Backup: hub.html.bak-markets")
PY
grep -c 'data-t="markets"' hub.html
echo "== how tabs load their pages"; grep -n "data-src" hub.html | grep -v "<iframe" | head -5
echo "Now refresh the Hub page."
