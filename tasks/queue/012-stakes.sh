#!/bin/bash
# QUEUE-OK
python3 - <<'PY'
import json, os, time
rows = []
for l in open(os.path.expanduser("~/market-data/run_log.jsonl")):
    try: r = json.loads(l)
    except ValueError: continue
    rows.append(r)
print("rows:", len(rows))
for r in rows[-24:]:
    print(time.strftime("%a %H:%M", time.localtime(r.get("t", 0))), "staked $%s" % r.get("staked"), "pnl", r.get("pnl"), r.get("outcome"), "strat", r.get("strat"), "trades", r.get("trades"))
print("max staked, last 14h: $%s" % max([float(r.get("staked") or 0) for r in rows if r.get("t", 0) > time.time() - 14 * 3600] or [0]))
PY
