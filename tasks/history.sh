#!/bin/bash
# One command to pull your whole Kalshi history, fetch the old prices, and replay every strategy on it. Read-only: places no orders.
# Safe to run while the agent is running (it uses its own sandbox). Run it again later to continue where it stopped.
cd ~/starship && git pull -q
cd markets
echo "=== 1/3 your Kalshi fills ==="; python3 my_trades.py 2>&1 | tail -30
echo; echo "=== 2/3 old prices (Kalshi minutes + Bitcoin minutes) ==="; python3 backfill.py ${1:-14} 1500
echo; echo "=== 3/3 replay ==="; python3 replay.py ${1:-14}
