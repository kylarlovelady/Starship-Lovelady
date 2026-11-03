#!/bin/bash
# Read-only review of the LAST live session (found from the alerts log): Kalshi's own fills, balance, and the agent's reasons.
cd ~/starship/markets && python3 - <<'PY'
import json, os, re, sys, time
sys.path.insert(0, ".")
D = os.path.expanduser("~/market-data")
hm = lambda t: time.strftime("%H:%M:%S", time.localtime(t))
# 1. when did the last live session start and end?
start = end = None
for l in open(os.path.join(D, "alerts.log")):
    m = re.match(r"(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) \S+ .*?: (.*)", l)
    if not m: continue
    t = time.mktime(time.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")); s = m.group(2).lower()
    if "live started" in s or "live session started" in s: start, end = t, None
    elif start and end is None and ("live ended" in s or "live stopped" in s or "live session ended" in s or "kill switch" in s): end = t
if not start:
    print("no live session found in the alerts log"); raise SystemExit
end = end or time.time()
print("LIVE SESSION %s to %s (%.0f minutes)" % (hm(start), hm(end), (end - start) / 60))
import kalshi_trade as K, my_trades as M
c = K.Kalshi()
st, b = c.balance()
bal = float(b.get("balance_dollars") if b.get("balance_dollars") is not None else float(b.get("balance", 0)) / 100)
print("Kalshi balance now: $%.2f   (it started the session at $239.17)" % bal)
# 2. Kalshi's own fills inside the window
fl = [M.one(r) for r in M.fills(c, 3)]
fl = [x for x in fl if start - 30 <= x["t"] <= end + 120 and (x["ticker"] or "").startswith("KXBTC15M")]
print("\nKALSHI FILLS in the window: %d" % len(fl))
for x in sorted(fl, key=lambda x: x["t"]):
    print("  %s %-4s %-3s %5.1f @ %2d cents  fee %.2f  %s" % (hm(x["t"]), x["act"], x["side"], x["n"], round(x["px"] * 100), x["fee"], (x["ticker"] or "")[-8:]))
# 3. what the agent logged
def jl(n):
    out = []
    try:
        for l in open(os.path.join(D, n)):
            try: out.append(json.loads(l))
            except Exception: pass
    except OSError: pass
    return out
lo = [o for o in jl("live_orders.jsonl") if start - 30 <= o.get("t", 0) <= end + 120]
orders = [o for o in lo if "action" in o and "status" in o]
slips = [o["slip_cents"] for o in lo if "slip_cents" in o]
print("\nAGENT ORDERS: sent %d, rejected %d, avg slippage %.2f cents, worst %.1f" % (len(orders), len([o for o in orders if o["status"] not in (200, 201)]), sum(slips) / max(1, len(slips)), max(slips or [0])))
rounds = [r for r in jl("run_log.jsonl") if start - 900 <= r["t"] <= end + 60]
prac = {x["t"]: x for x in jl("sim_windows.jsonl") if x.get("strat") == "signals"}
for r in rounds:
    p = prac.get(r["t"])
    print("\n== round %s  result %s  pnl %+.2f  (practice same round: %s)  staked $%s" % (time.strftime("%H:%M", time.localtime(r["t"])), r["outcome"], r["pnl"], ("%+.2f" % p["pnl"]) if p else "n/a", r.get("staked")))
    print("   odds of Up at open: %s" % r.get("p_open"))
    for m in (r.get("moves") or []):
        print("   %4ds %-4s %-4s $%-6s @%2dc  %s" % (m["t"] - r["t"], m["a"], m["side"], m["d"], round(m["px"] * 100), (m.get("why") or "")[:100]))
    print("   -> " + (r.get("why") or "")[:200])
if not rounds: print("\n(no finished rounds were logged for this session)")
try:
    L = json.load(open(os.path.join(D, "learn_report.json")))
    print("\nLEARNER: %s rounds scored" % L.get("scored"))
    for n in (L.get("notes") or [])[:4]: print(" -", n[:150])
except Exception: pass
PY
