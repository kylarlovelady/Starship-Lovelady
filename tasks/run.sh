#!/bin/bash
# Read-only review of the last LIVE session: what it did, why, what it cost, and what it learned.
python3 - <<'PY'
import json, os, time
D = os.path.expanduser("~/market-data")
def jl(n):
    out = []
    try:
        for l in open(os.path.join(D, n)):
            try: out.append(json.loads(l))
            except Exception: pass
    except OSError: pass
    return out
hm = lambda t: time.strftime("%H:%M", time.localtime(t))
orders = [o for o in jl("live_orders.jsonl") if "action" in o and "status" in o]
slips = [o["slip_cents"] for o in jl("live_orders.jsonl") if "slip_cents" in o]
if not orders:
    print("no live orders found"); raise SystemExit
t0, t1 = orders[0]["t"], orders[-1]["t"]
print("LIVE SESSION %s to %s" % (hm(t0), hm(t1)))
ok = [o for o in orders if o["status"] in (200, 201) and float((o.get("reply") or {}).get("fill_count") or 0) >= 1]
print("orders sent %d, filled %d, rejected %d, avg slippage %.2f cents (worse than quote), worst %.1f" % (
    len(orders), len(ok), len([o for o in orders if o["status"] not in (200, 201)]), sum(slips) / max(1, len(slips)), max(slips or [0])))
rounds = [r for r in jl("run_log.jsonl") if t0 - 900 <= r["t"] <= t1 + 60]
prac = {}
for x in jl("sim_windows.jsonl"):
    if x.get("strat") == "signals": prac[x["t"]] = x
tot = 0
for r in rounds:
    tot += r["pnl"]
    p = prac.get(r["t"])
    print("\n== round %s  result %s  pnl %+.2f  (practice 'signals' same round: %s)  staked $%s  trades %s" % (
        hm(r["t"]), r["outcome"], r["pnl"], ("%+.2f" % p["pnl"]) if p else "n/a", r.get("staked"), r.get("trades")))
    print("   its odds of Up at open: %s" % r.get("p_open"))
    for m in (r.get("moves") or []):
        print("   %4ds %-4s %-4s $%-6s @%2dc  %s" % (m["t"] - r["t"], m["a"], m["side"], m["d"], round(m["px"] * 100), (m.get("why") or "")[:95]))
    print("   -> " + (r.get("why") or "")[:230])
print("\nTOTAL over %d rounds: %+.2f" % (len(rounds), tot))
print("\n== WHAT IT LEARNED (latest learner notes)")
try:
    L = json.load(open(os.path.join(D, "learn_report.json")))
    print("rounds scored", L.get("scored"))
    for n in (L.get("notes") or [])[:6]: print(" -", n[:160])
    for k, g in (L.get("signals") or {}).items():
        print("   %-9s trust %-5s right %-5s of %-3s %s" % (k, g.get("trust"), g.get("pct"), g.get("n"), g.get("verdict")))
except Exception as e:
    print("no report", e)
PY
