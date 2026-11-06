#!/bin/bash
# QUEUE-OK
# stricter maker (resting order) study: read-only, 2 GB cap, lowest priority
(ulimit -v 2500000; nohup nice -n 19 python3 ~/starship/markets/maker_study2.py 4 > /tmp/maker-study2.out 2>&1 &)
for i in $(seq 1 27); do sleep 10; pgrep -f maker_study2.py >/dev/null || break; done
head -c 4500 /tmp/maker-study2.out
