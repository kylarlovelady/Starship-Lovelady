#!/usr/bin/env python3
"""SIGNAL CHECK (read-only, practice money). For the hold-to-end $500 test: do the agent's signals agree with its bets, and does agreement predict wins?
Also shows why some rounds are $5 and others about $480. Uses the first BUY of each round with its recorded features (f) and reason (why).
  python3 signal_check.py [strategy=v_hold_s500]"""
import json, math, os, sys, time
from collections import defaultdict, Counter
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
rows = []
for tk, rs in ev.items():
    if tk not in res: continue
    rs.sort(key=lambda r: r["t"]); f = rs[0].get("f") or {}; side = rs[0]["side"]
    cost = sum(r["c"] * r["px"] + fee_total(int(r["c"]), r["px"]) for r in rs); n = sum(r["c"] for r in rs)
    pnl = (n if res[tk] == side else 0) - cost
    rows.append({"t": rs[0]["t"], "side": side, "f": f, "why": rs[0].get("why"), "cost": cost, "pnl": pnl, "px": sum(r["c"] * r["px"] for r in rs) / n, "win": res[tk] == side})
rows.sort(key=lambda r: r["t"])
print("SIGNAL CHECK %s: %d settled rounds with a BUY" % (who, len(rows)))
print("feature keys seen:", Counter(k for r in rows for k in r["f"]).most_common(12))
big = [r for r in rows if r["cost"] >= 50]; small = [r for r in rows if r["cost"] < 50]
print("\nSIZE: %d big rounds (stake >= $50), %d small (< $50)" % (len(big), len(small)))
for nm, b in (("big", big), ("small", small)):
    if b: print("  %-5s won %3.0f%%, avg price %.0fc, profit per $ staked %+.1f%%" % (nm, 100.0 * sum(r["win"] for r in b) / len(b), 100 * sum(r["px"] for r in b) / len(b), 100.0 * sum(r["pnl"] for r in b) / sum(r["cost"] for r in b)))
print("  reasons logged on big rounds :", Counter((r["why"] or "?")[:50] for r in big).most_common(4))
print("  reasons logged on small rounds:", Counter((r["why"] or "?")[:50] for r in small).most_common(4))
sc = [r for r in rows if isinstance(r["f"].get("score"), (int, float))]
print("\nSIGNAL SCORE vs the bet (score > 0 leans Up). %d rounds have a score" % len(sc))
def line(nm, b):
    if b: print("  %-34s %3d rounds, won %3.0f%%, profit per $ %+6.1f%%, total at the real stakes %+9.2f" % (nm, len(b), 100.0 * sum(r["win"] for r in b) / len(b), 100.0 * sum(r["pnl"] for r in b) / max(1e-9, sum(r["cost"] for r in b)), sum(r["pnl"] for r in b)))
ag = lambda r: (r["f"]["score"] > 0) == (r["side"] == "UP") if r["f"]["score"] != 0 else None
line("signals AGREE with the bet", [r for r in sc if ag(r) is True]); line("signals DISAGREE with the bet", [r for r in sc if ag(r) is False]); line("score exactly 0", [r for r in sc if ag(r) is None])
for lo, hi in ((0, 10), (10, 25), (25, 50), (50, 101)):
    line("|score| %d-%d, agree" % (lo, hi), [r for r in sc if ag(r) is True and lo <= abs(r["f"]["score"]) < hi]); line("|score| %d-%d, disagree" % (lo, hi), [r for r in sc if ag(r) is False and lo <= abs(r["f"]["score"]) < hi])
print("\nCHEAP SIDE (under 40c) by agreement:")
line("cheap, signals agree", [r for r in sc if r["px"] < .4 and ag(r) is True]); line("cheap, signals disagree", [r for r in sc if r["px"] < .4 and ag(r) is False])
print("\nTIME INTO THE ROUND of the first buy:", Counter(int(r["f"].get("sec", r["f"].get("el", -1)) // 60) for r in rows).most_common(6))
