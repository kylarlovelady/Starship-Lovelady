#!/bin/bash
# QUEUE-OK
# Read-only: what the agent has learned (small json files) and how its practice fills compare with real ones.
D=~/market-data
for f in learn_report.json exit_rules.json entry_stats.json patterns.json; do echo "== $f"; head -c 1300 $D/$f 2>&1; echo; done
echo "== config (keys with plain values only)"; python3 -c "
import json,os
d=json.load(open(os.path.expanduser('~/market-data/config.json')))
print({k:v for k,v in d.items() if isinstance(v,(bool,int,float)) or (isinstance(v,str) and len(v)<24 and 'key' not in k.lower() and 'token' not in k.lower())})" 2>&1 | head -c 1500
echo "== real (live) order slippage notes, last 8"; grep -h slip_cents $D/live_orders.jsonl 2>/dev/null | tail -8 | cut -c1-220
