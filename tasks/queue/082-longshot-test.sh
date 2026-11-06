#!/bin/bash
# QUEUE-OK
# longshot hypothesis test (cheap side 3 to 7 min out): read-only, 3.5 GB cap, lowest priority
(ulimit -v 3500000; nohup nice -n 19 python3 ~/starship/markets/longshot_wf.py 5 > /tmp/longshot-wf.out 2>&1 &)
for i in $(seq 1 27); do sleep 10; pgrep -f longshot_wf.py >/dev/null || break; done
head -c 4800 /tmp/longshot-wf.out
