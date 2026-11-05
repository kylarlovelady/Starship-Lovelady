#!/bin/bash
# QUEUE-OK
# Where does the home-screen clock/weather theme live? Read-only search (names and line counts only).
echo "== kiosk / chromium command"; ps aux | grep -i -E "chromium|kiosk" | grep -v grep | cut -c1-260 | head -3
echo "== ports 8080/8081"; ss -ltnp 2>/dev/null | grep -E ":(8080|8081|8089)\b" | cut -c1-140
echo "== hub files"; ls -l /usr/local/bin/hub-dashboard.py 2>&1 | cut -c1-100; ls -d /opt/hub* ~/hub* ~/dashboard* ~/ha-home* 2>/dev/null | head
echo "== files mentioning clock+weather"; grep -l -i -E "clock" -r /usr/local/bin ~/crew-web ~/hub* /opt 2>/dev/null | grep -v -E "\.bak|node_modules|\.pyc|/proc" | head -12
echo "== theme words"; grep -rl -i -E "snow|cabin|fireplace" /usr/local/bin ~/hub* /opt ~/crew-web 2>/dev/null | grep -v -E "\.bak|\.pyc" | head -8
echo "== nocursor"; grep -rl "nocursor" /usr/local/bin ~/hub* /opt ~/crew-web 2>/dev/null | head -5
