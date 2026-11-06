#!/bin/bash
# QUEUE-OK
# catalogue every Kalshi 15-minute crypto series and compare how predictable each is (read-only, polite request rate, ~30 min, runs in the background)
cd ~/starship || exit 1
(nohup nice -n 19 bash -c 'python3 ~/starship/markets/series_catalog.py 3 35 > /tmp/series-catalog.out 2>&1; bash ~/starship/tasks/memory_sync.sh >/dev/null 2>&1' >/dev/null 2>&1 &)
sleep 20
echo "started; progress so far:"; cat /tmp/series-catalog.out 2>/dev/null | tail -5
