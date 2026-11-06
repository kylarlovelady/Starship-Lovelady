#!/bin/bash
# QUEUE-OK
# hindsight/oracle study: best possible trade per recorded round + which signals predicted it (read-only)
nohup python3 ~/starship/markets/oracle_study.py 7 > /tmp/oracle-study.out 2>&1 &
sleep 100
cd ~/starship && bash tasks/memory_sync.sh >/dev/null 2>&1
head -c 5500 /tmp/oracle-study.out
