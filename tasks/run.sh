#!/bin/bash
# Read-only: shows how the Hub page is built so the Markets tab can be added safely.
echo "== Live view link in crew-update"; grep -c live.html ~/crew-update.sh
cd ~/hub-dashboard 2>/dev/null || { echo "no ~/hub-dashboard"; exit; }
ls
echo "== nav buttons"; grep -n 'data-t=' hub.html | head -20
echo "== panes"; grep -n 'class="pane' hub.html | head -20
echo "== show()"; grep -n 'function show' hub.html
