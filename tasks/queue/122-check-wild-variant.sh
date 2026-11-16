#!/bin/bash
# read-only: did the agent restart on v10.2 and is the wild-day variant making rounds? live must stay off.
cd ~/starship/markets 2>/dev/null || exit 0
echo "== $(date) =="
git log --oneline | head -2
systemctl is-active market-agent 2>&1
journalctl -u market-agent -n 15 --no-pager 2>&1 | tail -15
grep -c v_hold_s250_wild ~/market-data/trades.jsonl 2>/dev/null
tail -n 400 ~/market-data/trades.jsonl 2>/dev/null | grep v_hold_s250_wild | tail -3 | cut -c1-300
