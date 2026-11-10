#!/usr/bin/env python3
"""SIZE RULES REPLAY (read-only, practice money). Takes the 186+ recorded rounds of the hold-to-end $500 test (same entries) and re-sizes each round
under different rules, to see which sizing rule would have done best on the SAME rounds. Includes Kylar's rule (bigger when the signals agree).
Each round's profit per dollar staked is kept; only the stake changes. Fees are inside that per-dollar number. Small samples: treat as hints.
  python3 size_rules.py [strategy=v_hold_s500]"""
import json, math, os, sys
from collections import defaultdict
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
def fee_total(c, p): return math.ceil(0.07 * c * p * (1 - p) * 100 - 1e-9) / 100.0
def outcomes():
    res = {}
    try:
        import exit_learn as X; res.update(X.outcomes(D))
    except Exception as e: print("(outcomes: %s)" % e)
    for p in (os.path.join(D, "history", "rounds.jsonl"), os.path.join(D, "rounds.jsonl")):
        try:
            for ln in open(p):
                try: r = json.loads(ln); res.setdefault(r["ticker"], r["result"])
                except Exception: pass
        except OSError: pass
    return res
who = sys.argv[1] if len(sys.argv) > 1 else "v_hold_s500"
res = outcomes(); ev = defaultdict(list)
for l in open(os.path.join(D, "trades.jsonl")):
    try: r = json.loads(l)
    except ValueError: continue
    if r.get("live") or r.get("s") != who or r.get("a") != "BUY" or not r.get("c") or not r.get("px"): continue
    ev[r["ticker"]].append(r)
R = []
for tk, rs in ev.items():
    if tk not in res: continue
    rs.sort(key=lambda r: r["t"]); f = rs[0].get("f") or {}; side = rs[0]["side"]
    cost = sum(r["c"] * r["px"] + fee_total(int(r["c"]), r["px"]) for r in rs); n = sum(r["c"] for r in rs)
    pnl = (n if res[tk] == side else 0) - cost
    sc = f.get("score"); agree = None if not isinstance(sc, (int, float)) or sc == 0 else ((sc > 0) == (side == "UP"))
    R.append({"t": rs[0]["t"], "ppd": pnl / cost, "px": sum(r["c"] * r["px"] for r in rs) / n, "agree": agree, "a": abs(sc or 0), "cost": cost, "pnl": pnl})
R.sort(key=lambda r: r["t"])
RULES = {
 "A. as recorded (about $5 or $480)":          lambda r: r["cost"],
 "B. flat $250 every round":                    lambda r: 250,
 "C. flat $100 every round":                    lambda r: 100,
 "D. cheap side (<40c) capped at $100, rest $250": lambda r: 100 if r["px"] < .40 else 250,
 "E. KYLAR: $250 if signals agree, $100 if split, $50 if disagree": lambda r: 250 if r["agree"] is True else 100 if r["agree"] is None else 50,
 "F. KYLAR strong: $400 agree and |score|>=10, $200 agree, $75 split, $25 disagree": lambda r: 400 if (r["agree"] is True and r["a"] >= 10) else 200 if r["agree"] is True else 75 if r["agree"] is None else 25,
 "G. opposite of Kylar: $250 if signals DISAGREE, $100 if agree": lambda r: 250 if r["agree"] is False else 100,
 "H. size by price: $50 under 40c, $250 40-60c, $400 over 60c":  lambda r: 50 if r["px"] < .40 else 250 if r["px"] < .60 else 400,
}
print("SIZE RULES REPLAY on %d settled %s rounds (same entries, new stakes). Treat as hints, not proof.\n" % (len(R), who))
print("%-84s %10s %9s %10s %8s" % ("rule", "profit", "worst drop", "avg stake", "profit/$"))
for nm, fn in RULES.items():
    cum = pk = mdd = st = 0.0
    for r in R:
        s = fn(r); p = r["ppd"] * s; cum += p; st += s
        if cum > pk: pk = cum
        mdd = max(mdd, pk - cum)
    print("%-84s %+10.0f %9.0f %10.0f %+7.1f%%" % (nm, cum, mdd, st / len(R), 100 * cum / st))
half = len(R) // 2
print("\nSAME RULES, FIRST HALF vs SECOND HALF of the rounds (does the ranking hold on rounds it did not see?)")
for nm, fn in list(RULES.items())[1:]:
    a = sum(r["ppd"] * fn(r) for r in R[:half]); b = sum(r["ppd"] * fn(r) for r in R[half:])
    print("  %-80s first %+8.0f   second %+8.0f" % (nm[:80], a, b))
