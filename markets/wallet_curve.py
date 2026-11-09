#!/usr/bin/env python3
"""WALLET CURVE (read-only, practice money): replays one strategy's trades round by round from trades.jsonl and prints the running profit,
the peak, the worst drop, the latest rounds and what drove the swings. Fees included.
  python3 wallet_curve.py [strategy=v_hold_s500] [last_rounds=30]"""
import json, math, os, sys, time
from collections import defaultdict
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def fee_total(c, p): return math.ceil(0.07 * c * p * (1 - p) * 100 - 1e-9) / 100.0
def hm(t): return time.strftime("%a %d %H:%M", time.localtime(t))

def outcomes():
    res = {}
    try:
        import exit_learn as X
        res.update(X.outcomes(D))
    except Exception as e:
        print("(exit_learn outcomes unavailable: %s)" % e)
    for p in (os.path.join(D, "history", "rounds.jsonl"), os.path.join(D, "rounds.jsonl")):
        try:
            for ln in open(p):
                try: r = json.loads(ln); res.setdefault(r["ticker"], r["result"])
                except Exception: pass
        except OSError: pass
    return res

def main():
    who = sys.argv[1] if len(sys.argv) > 1 else "v_hold_s500"
    last = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    res = outcomes(); ev = defaultdict(list)
    for l in open(os.path.join(D, "trades.jsonl")):
        try: r = json.loads(l)
        except ValueError: continue
        if r.get("live") or r.get("s") != who or r.get("a") not in ("BUY", "SELL") or not r.get("c") or not r.get("px"): continue
        ev[r.get("ticker")].append(r)
    rows = []; unsettled = 0
    for tk, rs in ev.items():
        if tk not in res: unsettled += 1; continue
        rs.sort(key=lambda r: r["t"]); pos = {"UP": 0, "DOWN": 0}; cash = 0.0; stake = 0.0; t0 = rs[0]["t"]; side = rs[0]["side"]; cs = 0; ps = 0.0
        for r in rs:
            c, p, sd = int(r["c"]), float(r["px"]), r["side"]
            if r["a"] == "BUY": cash -= c * p + fee_total(c, p); stake += c * p; pos[sd] += c; cs += c; ps += c * p
            else:
                c = min(c, pos[sd])
                if c > 0: cash += c * p - fee_total(c, p); pos[sd] -= c
        end = sum(pos[sd] * (1.0 if res[tk] == sd else 0.0) for sd in pos)
        rows.append({"t": t0, "tk": tk, "side": side, "c": cs, "avg": (ps / cs if cs else 0), "stake": stake, "res": res[tk], "pnl": cash + end})
    rows.sort(key=lambda r: r["t"])
    if not rows: print("no settled rounds for", who); return
    cum = 0.0; peak = 0.0; peak_t = rows[0]["t"]; mdd = 0.0; mdd_from = None; mdd_to = None; curve = []
    for r in rows:
        cum += r["pnl"]; r["cum"] = cum; curve.append(cum)
        if cum > peak: peak = cum; peak_t = r["t"]
        if peak - cum > mdd: mdd = peak - cum; mdd_from = peak_t; mdd_to = r["t"]
    w = [r for r in rows if r["pnl"] > 0]; l = [r for r in rows if r["pnl"] <= 0]
    print("WALLET CURVE %s (pretend money, after fees): %d settled rounds, %s to %s, %d unsettled skipped" % (who, len(rows), hm(rows[0]["t"]), hm(rows[-1]["t"]), unsettled))
    print("  profit now %+.2f | peak %+.2f (%s) | worst drop %.2f (%s -> %s) | drop right now %.2f from the peak" % (cum, peak, hm(peak_t), mdd, hm(mdd_from) if mdd_from else "-", hm(mdd_to) if mdd_to else "-", peak - cum))
    print("  wins %d (%.0f%%), avg win %+.2f, avg loss %+.2f, avg stake %.2f, avg entry price %.1f c" % (len(w), 100.0 * len(w) / len(rows), sum(r["pnl"] for r in w) / max(1, len(w)), sum(r["pnl"] for r in l) / max(1, len(l)), sum(r["stake"] for r in rows) / len(rows), 100 * sum(r["avg"] for r in rows) / len(rows)))
    for lo, hi in ((0, .40), (.40, .60), (.60, .80), (.80, 1.01)):
        b = [r for r in rows if lo <= r["avg"] < hi]
        if b: print("  entry price %2d-%3d c: %3d rounds, won %3.0f%%, profit %+9.2f" % (lo * 100, min(hi, 1) * 100, len(b), 100.0 * sum(1 for r in b if r["pnl"] > 0) / len(b), sum(r["pnl"] for r in b)))
    byside = {s: [r for r in rows if r["side"] == s] for s in ("UP", "DOWN")}
    for s, b in byside.items():
        if b: print("  bet %-4s: %3d rounds, won %3.0f%%, profit %+9.2f" % (s, len(b), 100.0 * sum(1 for r in b if r["pnl"] > 0) / len(b), sum(r["pnl"] for r in b)))
    top = sorted(rows, key=lambda r: -r["pnl"])[:5]; bot = sorted(rows, key=lambda r: r["pnl"])[:5]
    print("  5 best rounds: " + ", ".join("%+.0f" % r["pnl"] for r in top) + "  (= %.0f%% of total profit)" % (100.0 * sum(r["pnl"] for r in top) / cum if cum else 0))
    print("  5 worst rounds: " + ", ".join("%+.0f" % r["pnl"] for r in bot))
    run = mx = 0
    for r in rows: run = run + 1 if r["pnl"] <= 0 else 0; mx = max(mx, run)
    print("  longest losing streak: %d rounds" % mx)
    # by hour of day (local time)
    hrs = defaultdict(lambda: [0, 0.0]);
    for r in rows: h = time.localtime(r["t"]).tm_hour; hrs[h][0] += 1; hrs[h][1] += r["pnl"]
    print("  by hour (local): " + "  ".join("%02d:%+.0f(%d)" % (h, hrs[h][1], hrs[h][0]) for h in sorted(hrs)))
    print("\nLATEST %d ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)" % last)
    for r in rows[-last:]:
        print("  %s  %-4s %4d @%3.0fc  stake %6.0f  result %-4s  %+8.2f  total %+9.2f" % (hm(r["t"]), r["side"], r["c"], 100 * r["avg"], r["stake"], r["res"], r["pnl"], r["cum"]))
    print("\nRUNNING TOTAL every 10 rounds: " + ", ".join("%+.0f" % curve[i] for i in range(9, len(curve), 10)))
main()
