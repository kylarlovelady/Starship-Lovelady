#!/usr/bin/env python3
"""TAKE-PROFIT BACKTEST (read-only, practice data). Kylar 2026-11-07: bet early and sell as soon as the bet is up X%, else hold to the end.
For every recorded round (second-by-second Kalshi book) and every entry time, buy ONE contract of a side at the ask (15c to 80c only), then each second check if it could
be sold at the bid net of fee for X% more than we paid (incl. fee); if so we sell, otherwise we hold to the Kalshi result. Compared with plain hold on the same entries.
Sides: UP, DOWN, FAV (the side priced above 50c at entry) and DOG (the side below 50c). Shows profit per $ staked, win rate, how often the take-profit triggered,
a bootstrap 90% range, and older half vs newer half (a rule only counts if both halves agree). python3 take_profit_study.py [days=6]"""
import os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exit_learn as X, hindsight as Hs
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
def fee(p): return 0.07 * p * (1 - p)
ENTRIES = (30, 60, 120, 180, 300, 420)
TAKES = (0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.75, 1.0, None)


def run_round(rows, side, t_in, take):
    """rows sorted by time; returns (cost, pnl, took) or None."""
    k = None
    for i, (t, b, a, left, _) in enumerate(rows):
        if 900 - left >= t_in:
            k = i; break
    if k is None: return None
    t0, b, a = rows[k][0], rows[k][1], rows[k][2]
    px = a if side == "UP" else 1 - b
    if not 0.15 <= px <= 0.80: return None
    cost = px + fee(px)
    if take is not None:
        for (t, b2, a2, left, _) in rows[k + 1:]:
            if left < 3: break
            sp = b2 if side == "UP" else 1 - a2
            net = sp - fee(sp)
            if net >= cost * (1 + take):
                return cost, net - cost, True
    return cost, None, False


def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    res = X.outcomes(D); rows = Hs._rows(D, days)
    rs = sorted([(rows[tk][0][0], tk) for tk in rows if tk in res and len(rows[tk]) > 600])
    print("# Take-profit backtest (practice data, last %d days)\n" % days)
    print("Rounds with a full recording and a result: **%d**. One contract per entry, fees included, entry price 15c to 80c, sell only at the bid.\n" % len(rs))
    random.seed(7)
    out = []
    for t_in in ENTRIES:
        for rule in ("UP", "DOWN", "FAV", "DOG"):
            for take in TAKES:
                recs = []
                for (t0, tk) in rs:
                    r = rows[tk]; r = sorted(r, key=lambda z: z[0])
                    # decide the side at entry
                    k = next((i for i, z in enumerate(r) if 900 - z[3] >= t_in), None)
                    if k is None: continue
                    mid = (r[k][1] + r[k][2]) / 2.0
                    side = rule if rule in ("UP", "DOWN") else (("UP" if mid >= 0.5 else "DOWN") if rule == "FAV" else ("DOWN" if mid >= 0.5 else "UP"))
                    o = run_round(r, side, t_in, take)
                    if not o: continue
                    cost, pnl, took = o
                    win = res[tk] == side
                    if pnl is None: pnl = (1.0 if win else 0.0) - cost
                    recs.append((t0, cost, pnl, took, win))
                if len(recs) < 30: continue
                tot_c = sum(x[1] for x in recs); ppd = sum(x[2] for x in recs) / tot_c
                half = len(recs) // 2
                def pp(a): c = sum(x[1] for x in a); return (sum(x[2] for x in a) / c) if c else 0.0
                bs = []
                for _ in range(300):
                    s = [random.choice(recs) for _ in recs]; bs.append(pp(s))
                bs.sort()
                out.append((t_in, rule, take, len(recs), ppd, sum(1 for x in recs if x[3]) / len(recs), sum(1 for x in recs if x[4]) / len(recs), bs[15], bs[285], pp(recs[:half]), pp(recs[half:])))
    print("| enter at (s in) | side | take profit | bets | profit per $ | take triggered | won at end | 90% range | older half | newer half |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for t_in, rule, take, n, ppd, tk_, wn, lo, hi, o1, o2 in out:
        print("| %d | %s | %s | %d | %+.1f%% | %d%% | %d%% | %+.0f%% to %+.0f%% | %+.0f%% | %+.0f%% |" % (t_in, rule, ("+%d%%" % round(take * 100)) if take else "hold", n, ppd * 100, tk_ * 100, wn * 100, lo * 100, hi * 100, o1 * 100, o2 * 100))
    pos = [x for x in out if x[4] > 0 and x[7] > 0 and x[9] > 0 and x[10] > 0]
    print("\nRules positive in the whole sample, in BOTH halves, and with a 90%% range above zero: **%d** of %d (with this many rules tried, a couple would pass by luck alone)." % (len(pos), len(out)))
    for x in pos: print("- enter %ds, %s, take %s: %+.1f%% per $ on %d bets" % (x[0], x[1], x[2], x[4] * 100, x[3]))
    tk = {}
    for x in out:
        if x[2] is not None: tk.setdefault(x[2], []).append(x[4])
    base = [x[4] for x in out if x[2] is None]
    print("\nAverage over every entry time and side: hold %+.1f%%; " % (100 * sum(base) / max(1, len(base))) + "; ".join("take +%d%% %+.1f%%" % (round(k * 100), 100 * sum(v) / len(v)) for k, v in sorted(tk.items())) + ".")
    print("\nReading: if take-profit rows beat the 'hold' row of the same entry and side in both halves, the idea helps; if not, it is just selling winners early and paying the fee twice.")

main()
