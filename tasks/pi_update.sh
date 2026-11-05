#!/bin/bash
# ONE command to bring the Pi up to date and switch on everything the Starship needs. Safe to run again and again.
#   bash ~/starship/tasks/pi_update.sh          (add  ha  to also install the home-speaker Jarvis:  bash ~/starship/tasks/pi_update.sh ha)
cd ~/starship || exit 1
echo "== 1/6 get the newest code"; git pull -q --rebase && git log -1 --format='   now at %h %s'
echo "== 2/6 restart Jarvis (needs your Pi password once)"; sudo systemctl restart phone-voice && sleep 2 && systemctl is-active phone-voice
echo "== 3/6 alert checker every 5 min"
( crontab -l 2>/dev/null | grep -v starship-alerts; echo "*/5 * * * * /usr/bin/python3 \$HOME/starship/tasks/alerts_check.py >> \$HOME/alerts_check.log 2>&1 # starship-alerts" ) | crontab -
echo "   installed"
echo "== 4/6 daily Kalshi data sync (4:10 am)"; bash tasks/kalshi_data_sync.sh install
echo "== 5/6 task queue (the Pi runs scripts Claude leaves in tasks/queue, every 3 min)"; bash tasks/queue_runner.sh install
echo "== 6/6 status snapshot and notes sync now"; bash tasks/memory_sync.sh
if [ "$1" = "ha" ]; then echo; echo "== home speaker Jarvis"; bash tasks/ha_jarvis_install.sh; fi
echo; echo "Done. Hub front door: https://loveladymainaihub.taild703ca.ts.net/home"
echo "Alerts need HA_TOKEN in ~/market-data/env (already used by the Kalshi alerts). Jarvis can control lights with the same token."
