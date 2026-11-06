#!/bin/bash
# QUEUE-OK
# oracle study, memory-light rerun (3 days, capped at 2 GB, lowest priority)
free -m | head -2
(ulimit -v 2500000; nohup nice -n 19 python3 ~/starship/markets/oracle_study.py 3 > /tmp/oracle-study.out 2>&1 &) 
for i in $(seq 1 24); do sleep 10; pgrep -f oracle_study.py >/dev/null || break; done
free -m | sed -n 2p
head -c 4800 /tmp/oracle-study.out
