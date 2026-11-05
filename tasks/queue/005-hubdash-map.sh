#!/bin/bash
# QUEUE-OK
# Read-only map of ~/hub-dashboard (not its .venv) to find the home-screen page, its clock/weather/date markup and where themes are stored.
cd ~/hub-dashboard || exit 0
echo "== files"; find . -path ./.venv -prune -o -type f -not -name "*.pyc" -not -path "*/__pycache__/*" -print | head -60 | while read f; do printf "%s %s\n" "$(wc -c < "$f")" "$f"; done
echo "== who serves 8080"; ps -o pid,args -p $(ss -ltnp 2>/dev/null | grep "127.0.0.1:8080" | grep -o "pid=[0-9]*" | head -1 | cut -d= -f2) 2>&1 | cut -c1-200
echo "== clock/weather/date in html (line:text)"; grep -n -i -E "id=\"?(clock|weather|date)|class=\"?[a-z-]*(clock|weather|date)|\.clock|\.weather|\.date|#clock|#weather|#date" *.html 2>/dev/null | cut -c1-170 | head -50
echo "== theme storage"; ls -l *.json themes 2>/dev/null | head; grep -n -i -E "themes?[/_.]|theme_file|\.json" settings_api.py preview_api.py 2>/dev/null | cut -c1-150 | head -20
