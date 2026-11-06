#!/bin/bash
# QUEUE-OK
# Kalshi pricing study (implied volatility, calibration, spreads): read-only, 2 GB cap, lowest priority
(ulimit -v 2500000; nohup nice -n 19 python3 ~/starship/markets/implied_vol_study.py 4 > /tmp/implied-vol-study.out 2>&1 &)
for i in $(seq 1 27); do sleep 10; pgrep -f implied_vol_study.py >/dev/null || break; done
head -c 5000 /tmp/implied-vol-study.out
