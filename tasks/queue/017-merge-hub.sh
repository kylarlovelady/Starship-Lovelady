#!/bin/bash
# QUEUE-OK
# One site: add an "Overview" tab (first, default) to the Hub page that shows the Jarvis front door in embed mode. Backup first, safe to run twice.
cd ~/hub-dashboard || exit 1
[ -f hub.html.bak-merge ] || cp hub.html hub.html.bak-merge
python3 - <<'PY'
p="hub.html"; s=open(p,encoding="utf-8").read()
if 'id="overview"' in s: print("already merged"); raise SystemExit
URL="https://loveladymainaihub.taild703ca.ts.net/home?embed=1"
s=s.replace('<nav><button data-t="status" class="on">Status</button>','<nav><button data-t="overview" class="on">Overview</button><button data-t="status">Status</button>',1)
s=s.replace('<main id="status" class="pane on">','<iframe id="overview" class="pane on" src="%s" allow="microphone"></iframe><main id="status" class="pane">'%URL,1)
open(p,"w",encoding="utf-8").write(s); print("merged:", 'id="overview"' in s and 'data-t="overview"' in s)
PY
grep -o 'data-t="overview"[^>]*>' hub.html | head -2
echo "(hub.html is read fresh on every request, no restart needed)"
