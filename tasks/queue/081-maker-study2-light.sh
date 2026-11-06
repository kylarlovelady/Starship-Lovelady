#!/bin/bash
# QUEUE-OK
# stricter maker (resting order) study, memory-light rerun (first 5 minutes of each round only), 3.5 GB cap, lowest priority
free -m | sed -n 2p
(ulimit -v 3500000; nohup nice -n 19 python3 ~/starship/markets/maker_study2.py 3 > /tmp/maker-study2.out 2>&1 &)
for i in $(seq 1 27); do sleep 10; pgrep -f maker_study2.py >/dev/null || break; done
head -c 4500 /tmp/maker-study2.out
