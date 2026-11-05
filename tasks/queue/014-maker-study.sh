#!/bin/bash
# QUEUE-OK
# Read-only: does a resting (maker) buy beat paying the ask, counting orders that never fill? Uses the last 3 days of the agent's own per-second recordings.
cd ~/starship/markets && timeout 250 python3 maker_study.py 3 2>&1 | head -c 5000
