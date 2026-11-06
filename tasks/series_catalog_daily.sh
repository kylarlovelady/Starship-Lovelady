#!/bin/bash
# Nightly: add the newest settled rounds of every Kalshi 15-minute crypto series to the cache and rewrite memory/inbox/market-catalog.md. Read-only (no orders).
# Install the nightly run (4:40 am) with:  bash ~/starship/tasks/series_catalog_daily.sh install
if [ "$1" = "install" ]; then
  ( crontab -l 2>/dev/null | grep -v series-catalog; echo "40 4 * * * flock -n /tmp/series_catalog.lock bash \$HOME/starship/tasks/series_catalog_daily.sh >> \$HOME/market-data/series_catalog.log 2>&1 # series-catalog" ) | crontab -
  echo "installed: runs every night at 4:40 am"; crontab -l | grep series-catalog; exit 0
fi
nice -n 19 python3 "$HOME/starship/markets/series_catalog.py" 14 40
bash "$HOME/starship/tasks/memory_sync.sh" >/dev/null 2>&1
