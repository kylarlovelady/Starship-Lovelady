#!/bin/bash
# QUEUE-OK
# keep the 15-minute markets study running: install the nightly run (4:40 am) and start the first catch-up now in the background; then the BTC lag-1 check on the whole round history
bash ~/starship/tasks/series_catalog_daily.sh install
(nohup bash -c 'flock -n /tmp/series_catalog.lock bash $HOME/starship/tasks/series_catalog_daily.sh > /tmp/series-first.out 2>&1' >/dev/null 2>&1 &)
echo "== BTC lag-1 check"
python3 ~/starship/tasks/lag1_btc.py 2>&1 | head -30
