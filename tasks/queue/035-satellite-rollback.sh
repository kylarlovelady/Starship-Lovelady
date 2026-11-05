#!/bin/bash
# QUEUE-OK
# Roll the home satellite back to its working settings and show why the new flags failed.
cd ~/wyoming-satellite || exit 1
echo "== why it failed (last error lines)"; journalctl -u hub-satellite --since "10 minutes ago" --no-pager 2>&1 | grep -v "^-- " | grep -i -E "error|no module|import|noise|webrtc|recording|usage|invalid" | sort -u | tail -8 | cut -c1-220
[ -f run-hub.sh.bak-mic ] && cp run-hub.sh.bak-mic run-hub.sh && echo "restored working run-hub.sh"
pkill -f "wyoming_satellite"; sleep 10
echo "== satellite now"; systemctl is-active hub-satellite; journalctl -u hub-satellite -n 5 --no-pager 2>&1 | cut -c1-150
