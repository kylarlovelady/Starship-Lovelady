#!/bin/bash
# Read-only: your real Kalshi BTC trading style, then the voice setup. Places no orders.
cd ~/starship/markets && python3 my_trades.py 2>&1 | tail -30
echo
echo "################ VOICE SETUP ################"
echo "-- microphones"; arecord -l 2>&1 | grep -E "^card|no soundcards" | cut -c1-110
echo "-- speakers"; aplay -l 2>&1 | grep -E "^card" | cut -c1-110
echo "-- satellite launch script"; grep -v -i -E "token|key|pass|secret" ~/wyoming-satellite/run-hub.sh 2>&1 | head -30
echo "-- wake word"; ps aux | grep -i openwakeword | grep -v grep | sed 's/.*wyoming_openwakeword/wyoming_openwakeword/' | cut -c1-200
