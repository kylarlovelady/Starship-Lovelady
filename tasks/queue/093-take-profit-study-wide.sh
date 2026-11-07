#!/bin/bash
# QUEUE-OK
# read-only: take-profit backtest with many sell percentages (+5% to +100%) on the recorded rounds; practice data only
cd ~/starship/markets || exit 1
timeout 280 python3 take_profit_study.py 6 > ~/starship/memory/inbox/take-profit-study.md 2>&1
tail -6 ~/starship/memory/inbox/take-profit-study.md | cut -c1-300
