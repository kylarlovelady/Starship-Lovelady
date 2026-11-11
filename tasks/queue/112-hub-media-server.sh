#!/bin/bash
# QUEUE-OK
# Start the Hub media library server (port 8097, private network only) and keep it running: at boot, and a 5-minute watchdog.
S=$HOME/starship/hub2/media_server.py
[ -f "$S" ] || { echo "media_server.py not in the repo clone yet, retry in 3 min"; exit 0; }
( crontab -l 2>/dev/null | grep -v "hub2/media_server.py"
  echo "@reboot nohup python3 $S >/dev/null 2>&1 &"
  echo "*/5 * * * * pgrep -f hub2/media_server.py >/dev/null || nohup python3 $S >/dev/null 2>&1 &" ) | crontab -
pgrep -f hub2/media_server.py >/dev/null || nohup python3 "$S" >/dev/null 2>&1 &
sleep 2
mkdir -p ~/crew-web/hub2 && cp -r ~/starship/hub2/. ~/crew-web/hub2/
curl -s -m 5 http://127.0.0.1:8097/api/state | cut -c1-200; echo
echo "free space for photos:"; df -h ~ | tail -1 | awk '{print $4" free of "$2}'
