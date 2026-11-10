#!/bin/bash
# QUEUE-OK
# Read-only: did the practice agent restart cleanly on v9.9 and are the two new forward-test wallets trading?
sleep 240
echo "agent: $(systemctl is-active market-agent)"; journalctl -u market-agent --since "15 min ago" --no-pager 2>/dev/null | grep -i -e "collector updated" -e "error" -e "traceback" | tail -6
cd ~/market-data 2>/dev/null && grep -c "v_hold_s250_agree\|v_hold_s250_cheap100" trades.jsonl 2>/dev/null; tail -c 1500 trades.jsonl | grep -o '"s": "[a-z_0-9]*"' | sort | uniq -c | head
python3 - <<'P'
import json,os
p=os.path.expanduser("~/market-data/sim.json")
try:
    d=json.load(open(p)); acc=d.get("acc",{})
    for k in ("v_hold_s250","v_hold_s250_cheap100","v_hold_s250_agree"): print(k, "present" if k in acc else "MISSING", (acc.get(k) or {}).get("windows"))
except Exception as e: print("sim.json read:", e)
P
