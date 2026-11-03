#!/bin/bash
# Read-only: what the swing strategy actually did on practice, move by move, with its own reasons.
python3 - <<'PY'
import json, os, time
D = os.path.expanduser("~/market-data")
rows = []
for l in open(os.path.join(D, "trades.jsonl")):
    try: r = json.loads(l)
    except Exception: continue
    if r.get("s") in ("swing", "run") and r.get("a") in ("BUY", "SELL"): rows.append(r)
print("last moves of the swing strategy (time, action, contracts, price, why):")
for r in rows[-30:]:
    print("%s %-4s %-4s %4dx @%2d c  %s" % (time.strftime("%H:%M:%S", time.localtime(r["t"])), r["a"], r["side"], r.get("c") or 0, round(100 * (r.get("px") or 0)), (r.get("why") or "")[:150]))
try:
    sw = [json.loads(l) for l in open(os.path.join(D, "swings.jsonl"))]
    n = len(sw); ok = sum(1 for x in sw if x["profit_pc"] > 0)
    print("\nswing sales so far: %d, avg profit %+.1f c per contract after fees, took %d s on average" % (n, 100 * sum(x["profit_pc"] for x in sw) / max(1, n), sum(x.get("took", 0) for x in sw) / max(1, n)))
except Exception as e:
    print("no swing sales logged yet")
PY
