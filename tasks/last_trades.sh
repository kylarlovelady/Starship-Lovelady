#!/bin/bash
# Read-only: the last trades of the practice wallet, with the agent's own reason for each, and how each round ended.
python3 - <<'PY'
import json, os, time, sys
D = os.path.expanduser("~/market-data")
sys.path.insert(0, os.path.expanduser("~/starship/markets"))
try:
    import exit_learn as X; res = X.outcomes(D)
except Exception: res = {}
rows = []
for l in open(os.path.join(D, "trades.jsonl")):
    try: r = json.loads(l)
    except Exception: continue
    if r.get("s") == "run" and r.get("a") in ("BUY", "SELL") and not r.get("live"): rows.append(r)
print("last 25 trades of YOUR wallet (time, action, side, contracts, price, why):")
for r in rows[-25:]:
    print("%s %-4s %-4s %4sx @%2d c %s" % (time.strftime("%H:%M:%S", time.localtime(r["t"])), r["a"], r["side"], int(r.get("c") or 0), round(100 * (r.get("px") or 0)), (r.get("why") or "")[:130]))
    tk = r.get("ticker")
print("\nhow those rounds ended:")
seen = []
for r in rows[-25:]:
    tk = r.get("ticker")
    if tk and tk not in seen:
        seen.append(tk); print(" ", tk, "->", res.get(tk, "not settled yet"))
try:
    st = json.load(open(os.path.join(D, "state.json"))); sim = st.get("sim", {})
    print("\nAuto is following:", sim.get("auto_pick"), "| last switches:", [(time.strftime("%H:%M", time.localtime(x["t"])), x["to"]) for x in sim.get("autolog", [])[-3:]])
except Exception as e: print("state not readable", e)
try:
    er = json.load(open(os.path.join(D, "exit_rules.json"))); print("take-profit rule:", {k: er.get(k) for k in ("on", "enabled", "verdict", "reason") if k in er} or list(er)[:6])
except Exception as e: print("exit rules file not readable", e)
PY
