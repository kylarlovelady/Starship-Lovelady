#!/usr/bin/env python3
"""FORWARD REVIEW (read-only, practice money): compares strategies round by round from trades.jsonl, fees included.
1) forward tests since a start time vs their baseline (same rounds, paired), 2) luck check: profit without the best rounds, by day, first vs second half.
  python3 forward_review.py [start=2026-11-11]"""
import json, math, os, sys, time, statistics as st
from collections import defaultdict
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wallet_curve import outcomes, fee_total, hm

def rounds_for(res, who_set):
    ev = defaultdict(lambda: defaultdict(list))
    for l in open(os.path.join(D, "trades.jsonl")):
        try: r = json.loads(l)
        except ValueError: continue
        s = r.get("s")
        if s not in who_set or r.get("live") or r.get("a") not in ("BUY", "SELL") or not r.get("c") or not r.get("px"): continue
        ev[s][r.get("ticker")].append(r)
    out = {}
    for s, d in ev.items():
        rows = {}
        for tk, rs in d.items():
            if tk not in res: continue
            rs.sort(key=lambda r: r["t"]); pos = {"UP": 0, "DOWN": 0}; cash = 0.0; stake = 0.0
            for r in rs:
                c, p, sd = int(r["c"]), float(r["px"]), r["side"]
                if r["a"] == "BUY": cash -= c * p + fee_total(c, p); stake += c * p; pos[sd] += c
                else:
                    c = min(c, pos[sd])
                    if c > 0: cash += c * p - fee_total(c, p); pos[sd] -= c
            end = sum(pos[sd] * (1.0 if res[tk] == sd else 0.0) for sd in pos)
            rows[tk] = {"t": rs[0]["t"], "pnl": cash + end, "stake": stake}
        out[s] = rows
    return out

def summ(rows):
    v = [r["pnl"] for r in rows]
    if not v: return "no rounds"
    w = sum(1 for x in v if x > 0)
    return "%3d rounds | profit %+9.2f | win %3.0f%% | avg/round %+8.2f | median round %+7.2f | stake/round %.0f" % (len(v), sum(v), 100.0 * w / len(v), sum(v) / len(v), st.median(v), sum(r["stake"] for r in rows) / len(rows))

def main():
    start = time.mktime(time.strptime(sys.argv[1] if len(sys.argv) > 1 else "2026-11-11", "%Y-%m-%d"))
    names = ["v_hold_s250", "v_hold_s250_cheap100", "v_hold_s250_agree", "v_hold_s100", "hold", "v_edge10_s100", "v_hold_s500"]
    res = outcomes(); R = rounds_for(res, set(names))
    print("FORWARD REVIEW (pretend money, after fees). Start %s. Run %s\n" % (hm(start), time.strftime("%a %d %H:%M")))
    print("A) SINCE START, every strategy on its own rounds:")
    for n in names: print("  %-22s %s" % (n, summ([r for r in R.get(n, {}).values() if r["t"] >= start])))
    base = R.get("v_hold_s250", {})
    print("\nB) PAIRED vs v_hold_s250 (same rounds only; positive = the test beat the baseline):")
    for n in ("v_hold_s250_cheap100", "v_hold_s250_agree", "v_hold_s100", "hold", "v_edge10_s100"):
        t = R.get(n, {}); shared = [k for k in t if k in base and t[k]["t"] >= start]
        if len(shared) < 5: print("  %-22s only %d shared rounds" % (n, len(shared))); continue
        d = [t[k]["pnl"] - base[k]["pnl"] for k in shared]; m = sum(d) / len(d); se = (st.pstdev(d) / math.sqrt(len(d))) or 1e-9
        print("  %-22s %3d shared | total diff %+9.2f | avg %+7.2f/round | t-score %+.2f | better in %d, worse in %d, same in %d" % (n, len(d), sum(d), m, m / se, sum(1 for x in d if x > 0.005), sum(1 for x in d if x < -0.005), sum(1 for x in d if abs(x) <= 0.005)))
    print("   (t-score: about 2 or more = probably real, under 1 = could easily be luck)")
    print("\nC) LUCK CHECK, all history:")
    for n in ("v_edge10_s100", "v_hold_s250_cheap100", "v_hold_s250", "v_hold_s500"):
        rows = sorted(R.get(n, {}).values(), key=lambda r: r["t"])
        if len(rows) < 10: print("  %s: only %d rounds" % (n, len(rows))); continue
        v = [r["pnl"] for r in rows]; tot = sum(v); sv = sorted(v, reverse=True)
        print("  %s: %d rounds, total %+.2f" % (n, len(v), tot))
        print("     without best 3 rounds %+.2f | without best 5 %+.2f | without best 10%% (%d rounds) %+.2f" % (tot - sum(sv[:3]), tot - sum(sv[:5]), max(1, len(v) // 10), tot - sum(sv[:max(1, len(v) // 10)])))
        h = len(rows) // 2; a, b = sum(v[:h]), sum(v[h:])
        print("     first half %+.2f (%s to %s) | second half %+.2f (to %s)" % (a, hm(rows[0]["t"]), hm(rows[h - 1]["t"]), b, hm(rows[-1]["t"])))
        days = defaultdict(float)
        for r in rows: days[time.strftime("%a %d", time.localtime(r["t"]))] += r["pnl"]
        pos = sum(1 for x in days.values() if x > 0)
        print("     by day: " + "  ".join("%s %+.0f" % (k, x) for k, x in days.items()) + "  -> %d of %d days positive" % (pos, len(days)))
main()
