"""ENDGAME TEST (read-only). Kalshi settles a 15-minute round on the AVERAGE of the index over the last 60 seconds compared with the average of the 60 seconds before the round opened.
So with 50 s left, 10 s of the final average is already fixed; with 20 s left, 40 s of it is. A model that tracks the fixed part and only guesses the rest should know the answer better than a
quote that treats Bitcoin as a single price. Test: from the per-second recording, at 50, 40, 30, 20 and 10 seconds left, compute the probability that the final average ends above the target,
compare to the real Kalshi ask, and buy the side the model likes when it beats the price plus fee by a margin. Hold to the end (so no exit cost). Real prices, real fees, older vs newer rounds.
Coinbase is not exactly Kalshi's index, so one offset (dollars) is fitted on the OLDER rounds only. Usage: python3 endgame.py [days=14]"""
import bisect, math, sys, time, json
from hypothesis import fee

LEFTS = (50, 40, 30, 20, 10)
OFFSET_SD = 6.0          # dollars of unavoidable mismatch between Coinbase and Kalshi's index


def ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def qat(rows, ts, t, maxage=8):
    i = bisect.bisect_right(ts, t)
    return (rows[i - 1][1], rows[i - 1][2]) if i and t - ts[i - 1] <= maxage else None


def model(btc, close, t, strike, off):
    """Probability the final 60 s average (plus offset) ends above the target, given what is known at time t."""
    t0 = close - 60
    known = [btc.at(s) for s in range(t0, t + 1)]
    if any(v is None for v in known): return None
    n = close - t - 1                       # seconds still to come
    b = known[-1]
    inc = []
    for s in range(t - 300, t, 5):
        a, c = btc.at(s), btc.at(s + 5)
        if a is not None and c is not None: inc.append(c - a)
    if len(inc) < 20: return None
    sig = math.sqrt(sum(x * x for x in inc) / len(inc) / 5.0) or 0.5          # dollars per sqrt(second)
    mean = (sum(known) + n * b) / 60.0
    var = sig * sig * (n * (n + 1) * (2 * n + 1) / 6.0) / 3600.0 + OFFSET_SD ** 2
    return ncdf((mean + off - strike) / math.sqrt(var))


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    import replay
    use, cand, btc = replay.load_ticks(days)
    use = [r for r in use if r.get("result") in ("UP", "DOWN")]
    if len(use) < 20:
        print("Only %d fully recorded rounds with results. Let it record longer." % len(use)); return
    use.sort(key=lambda r: r["open"]); cut = use[int(len(use) * 0.6)]["open"]
    older = [r for r in use if r["open"] < cut]
    best = None
    for off in range(-40, 41, 4):                          # fit the offset on OLDER rounds: which shift makes the final average call the right side most often
        ok = tot = 0
        for r in older:
            p = model(btc, r["close"], r["close"] - 10, float(r["strike"]), off)
            if p is None: continue
            tot += 1; ok += ((p > .5) == (r["result"] == "UP"))
        if tot and (best is None or ok / tot > best[0]): best = (ok / tot, off)
    off = best[1] if best else 0
    print("%d recorded rounds (%d older to fit one offset, %d newer). Fitted Coinbase-to-Kalshi offset: %+d dollars (calls the right side %.0f%% of the time with 10 s left).\n" % (len(use), len(older), len(use) - len(older), off, 100 * best[0] if best else 0))
    out = {}
    for margin in (0.03, 0.06, 0.10):
        print("buy when the model beats the real price plus fee by %d cents or more, hold to the end:" % round(100 * margin))
        print("  left   trades  win%  avg price | NET cents per contract  (t)  | older  | newer")
        for L in LEFTS:
            R = []
            for r in use:
                t = r["close"] - L
                q = qat(cand[r["ticker"]], [x[0] for x in cand[r["ticker"]]], t)
                p = model(btc, r["close"], t, float(r["strike"]), off)
                if q is None or p is None or q[1] < q[0]: continue
                for side, px, pw in (("UP", q[1], p), ("DOWN", 1 - q[0], 1 - p)):
                    if not .03 <= px <= .97: continue
                    if pw - px - fee(px) >= margin:
                        won = (r["result"] == "UP") == (side == "UP")
                        R.append((r["open"], px, won, 100 * ((1.0 if won else 0.0) - px - fee(px)))); break
            n = len(R)
            if n < 5: print("  %3d s   %4d   (too few)" % (L, n)); continue
            v = [x[3] for x in R]; m = sum(v) / n; sd = (sum((x - m) ** 2 for x in v) / (n - 1)) ** 0.5 or 1e-9
            o = [x[3] for x in R if x[0] < cut]; nw = [x[3] for x in R if x[0] >= cut]
            print("  %3d s   %4d   %3.0f   %4.0fc    | %+6.2f  (t %+4.1f) | %+6.2f | %+6.2f" % (L, n, 100 * sum(1 for x in R if x[2]) / n, 100 * sum(x[1] for x in R) / n, m, m / (sd / n ** 0.5), (sum(o) / len(o)) if o else 0, (sum(nw) / len(nw)) if nw else 0))
            out.setdefault(str(margin), {})[L] = {"n": n, "net": m}
        print()
    print("How to read it: NET above zero in BOTH older and newer, with enough trades (t above 2), would be a real edge from the averaging rule. Kalshi's price may already include it, in which case NET is near or below zero.")
    json.dump({"made": int(time.time()), "rounds": len(use), "offset": off, "res": out}, open(__import__("os").path.join(__import__("os").path.expanduser("~"), "market-data", "history", "endgame.json"), "w"))


if __name__ == "__main__":
    main()
