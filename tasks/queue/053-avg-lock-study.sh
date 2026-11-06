#!/bin/bash
# QUEUE-OK
# Read-only: can the winning side be called late using the partly known 60 s settlement average? Output memory/inbox/avg-lock-study.md
python3 ~/starship/markets/avg_lock_study.py 5 2>&1 | tail -60
