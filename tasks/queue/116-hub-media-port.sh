#!/bin/bash
# QUEUE-OK
# Port 8097 was already in use on the Pi, so the media server moved to 8110. Show what holds 8097, then start the server detached.
S=$HOME/starship/hub2/media_server.py
echo "-- who holds 8097:"; ss -ltnp 2>/dev/null | grep ":8097 " | cut -c1-160
cp -r ~/starship/hub2/. ~/crew-web/hub2/
pgrep -f hub2/media_server.py >/dev/null && pkill -f hub2/media_server.py; sleep 1
setsid nohup python3 "$S" >"$HOME/hub-media.log" 2>&1 < /dev/null &
sleep 3
echo "-- running:"; pgrep -af "hub2/media_server.py" | cut -c1-100
echo "-- state:"; curl -s -m 5 http://127.0.0.1:8110/api/state | cut -c1-160; echo
head -4 "$HOME/hub-media.log"
