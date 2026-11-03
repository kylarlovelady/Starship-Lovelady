#!/bin/bash
# One-time: run the progress supervisor every hour (read-only), then show it once now.
cd ~/starship/markets 2>/dev/null || exit 1
( crontab -l 2>/dev/null | grep -v market-supervisor; echo "7 * * * * /usr/bin/python3 $HOME/starship/markets/supervisor.py >> $HOME/market-data/supervisor.log 2>&1 # market-supervisor" ) | crontab -
python3 supervisor.py --quiet
echo; echo "Installed. Latest report is always in ~/market-data/progress.txt"
