#!/bin/bash
# QUEUE-OK
# check on the oracle study (read-only)
pgrep -af oracle_study | head -3
ls -la /tmp/oracle-study.out ~/starship/memory/inbox/oracle-study.md 2>&1
du -sh ~/market-data 2>&1 | tail -1
ls ~/market-data | head -20
head -c 4500 /tmp/oracle-study.out
