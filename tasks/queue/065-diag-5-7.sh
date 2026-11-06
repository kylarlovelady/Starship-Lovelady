#!/bin/bash
# QUEUE-OK
# read-only: (5) sniper log + agent restarts around the missed round, (7) where the home screen pop-up font is set
echo "== sniper log tail"; tail -4 ~/market-data/snipe_log.jsonl | cut -c1-300
echo "== agent restarts"; journalctl -u market-agent --since "23:40" --no-pager 2>/dev/null | grep -i "restart\|started\|Traceback\|Error" | tail -8 | cut -c1-200
echo "== hub-dashboard files"; ls -l ~/hub-dashboard | head -20
echo "== font settings"; grep -n "font" ~/hub-dashboard/settings.json 2>/dev/null | head -5
grep -n -i "font-family\|Great Vibes\|--font\|var(--" ~/hub-dashboard/theme.html 2>/dev/null | head -20 | cut -c1-200
echo "== popup/reply markup in index.html"; grep -n -i "reply\|bubble\|popup\|pop-up\|toast\|#you\|id=\"you" ~/hub-dashboard/index.html 2>/dev/null | head -30 | cut -c1-200
