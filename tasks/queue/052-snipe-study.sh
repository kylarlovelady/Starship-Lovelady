#!/bin/bash
# QUEUE-OK
# Read-only sniping study on the recorded per-second Kalshi data (does not trade). Output: memory/inbox/snipe-study.md
python3 ~/starship/markets/snipe_study.py 5 2>&1 | tail -70
