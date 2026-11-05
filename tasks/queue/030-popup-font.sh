#!/bin/bash
# QUEUE-OK
# Read-only: where does the home screen show Jarvis replies in a pop-up, and what font styling reaches it?
cd ~/hub-dashboard || exit 1
echo "== files"; ls -la --time-style=+%m-%d_%H:%M | grep -v -E "venv|pycache" | awk '{print $5,$6,$7}' | head -30
echo "== settings (font/theme keys only)"; python3 -c "
import json;d=json.load(open('settings.json'));print({k:v for k,v in d.items() if any(s in k.lower() for s in ('font','glass','theme','size','bubble','reply','text'))})" 2>&1 | cut -c1-600
echo "== reply popup code in index.html"; grep -n -i -E "reply|popup|pop-up|overlay|modal|assist|jarvis|transcript|answer" index.html | cut -c1-200 | head -25
echo "== font rules in theme.html / index.html"; grep -n -i -E "font-family|font-size|\\.glass|backdrop-filter|--font" theme.html index.html 2>/dev/null | cut -c1-200 | head -30
