#!/bin/bash
# QUEUE-OK: v8.9 sniper start check and fresh $1,000 wallet
cd ~/starship && git pull -q --rebase 2>&1 | tail -1
grep -c "sniper" markets/recorder.py
sleep 20
journalctl -u market-agent -n 5 --no-pager 2>/dev/null | tail -5
python3 ~/starship/markets/sniper.py reset
sleep 5
ls -la ~/market-data/snipe* 2>/dev/null
