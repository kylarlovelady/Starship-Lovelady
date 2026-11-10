#!/bin/bash
# QUEUE-OK
# Read-only: are the two new forward-test wallets buying, and does the BUY log now include the book depth (sz)?
cd ~/market-data 2>/dev/null || exit 1
echo "agent: $(systemctl is-active market-agent)  now: $(date '+%H:%M')"
for k in v_hold_s250 v_hold_s250_cheap100 v_hold_s250_agree; do echo "$k buys: $(grep -c "\"s\": \"$k\", \"a\": \"BUY\"" trades.jsonl)"; done
grep '"a": "BUY"' trades.jsonl | grep -e v_hold_s250_cheap100 -e v_hold_s250_agree -e '"s": "v_hold_s250"' | tail -6 | cut -c1-330
echo "buys with sz logged: $(grep -c '"sz"' trades.jsonl)"
