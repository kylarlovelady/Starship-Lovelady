#!/bin/bash
# QUEUE-OK
# read-only: backtest Kylar's take-profit idea (bet early, sell at +X%) on the recorded rounds; practice data only
cd ~/starship/markets || exit 1
timeout 270 python3 take_profit_study.py 6 > ~/starship/memory/inbox/take-profit-study.md 2>&1
tail -4 ~/starship/memory/inbox/take-profit-study.md | cut -c1-300
wc -l ~/starship/memory/inbox/take-profit-study.md
