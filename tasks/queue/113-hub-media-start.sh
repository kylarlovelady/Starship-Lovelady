#!/bin/bash
# QUEUE-OK
# Keep the Hub media library server (port 8110) running by starting it from crew-update.sh, which already runs every 3 minutes. Also starts it now and copies the new Hub page.
S=$HOME/starship/hub2/media_server.py
grep -q "hub2/media_server.py" ~/crew-update.sh || echo "pgrep -f hub2/media_server.py >/dev/null || nohup python3 \$HOME/starship/hub2/media_server.py >/dev/null 2>&1 &" >> ~/crew-update.sh
mkdir -p ~/crew-web/hub2 && cp -r ~/starship/hub2/. ~/crew-web/hub2/
pgrep -f hub2/media_server.py >/dev/null || nohup python3 "$S" >/dev/null 2>&1 &
sleep 2
curl -s -m 5 http://127.0.0.1:8110/api/state | cut -c1-200; echo
ls -la ~/crew-web/hub2 | cut -c1-90
echo "free space:"; df -h ~ | tail -1 | awk '{print $4" free of "$2}'
