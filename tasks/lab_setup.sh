#!/bin/bash
# One-time: run the strategy lab every 3 hours overnight (read-only, never touches the agent), then run it once now.
cd ~/starship/markets 2>/dev/null || exit 1
( crontab -l 2>/dev/null | grep -v market-lab; echo "20 */3 * * * /usr/bin/python3 $HOME/starship/markets/lab.py 14 240 >> $HOME/market-data/lab.log 2>&1 # market-lab" ) | crontab -
python3 lab.py 14 240
echo; echo "Installed. Every 3 hours it tries new rules. Every rule tried: ~/market-data/lab_log.jsonl. Best rules: ~/market-data/lab_state.json. Output: ~/market-data/lab.log"
