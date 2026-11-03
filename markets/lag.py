"""KALSHI LAG TEST (read-only). When Bitcoin jumps over a few seconds, how long does Kalshi's price take to follow, and is the gap bigger than what trading costs?
Uses the second-by-second recording (real order-book prices). Events: Bitcoin moves by more than a threshold in the last 10 s (one event per round per 45 s).
For each event: buy the side the jump favours at the real ask, then look again after 5-120 s. MOVE = how far the mid moved your way (cents, before cost).
NET = sell at the real bid after that wait, minus both fees. The agent may not sell within 30 s of a buy, so the 30 s+ columns are the ones it could use.
Usage: python3 lag.py [days=14]"""
import bisect, math, sys, time, json
from hypothesis import fee

HZ = (5, 10, 20, 30, 60, 120)


def qat(rows, ts, t, maxage=8):
    i = bisect.bisect_right(ts, t)
    return (rows[i - 1][1], rows[i - 1][2]) if i and t - ts[i - 1] <= maxage else None


def mean_t(v):
    n = len(v)
    if n < 8: return (0.0, 0.0, n)
    m = sum(v) / n; sd = (sum((x - m) ** 2 for x in v) / (n - 1)) ** 0.5 or 1e-9
    return (m, m / (sd / n ** 0.5), n)


def events(use, cand, btc, span=10, step=5):
    out = []
    for r in use:
        tk, o, cl = r["ticker"], r["open"], r["close"]
        c = cand[tk]; cts = [x[0] for x in c]
        last_ev = 0
        for t in range(o + 60, cl - 150, step):
            b, b0 = btc.at(t), btc.at(t - span)
            if b is None or b0 is None: continue
            out.append({"tk": tk, "t": t, "o": o, "mv": b - b0, "c": c, "cts": cts, "res": r["result"], "cl": cl})
    return out


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    import replay
    use, cand, btc = replay.load_ticks(days)
    ev = events(use, cand, btc)
    if len(use) < 20 or not ev:
        print("Only %d fully recorded rounds so far. Let it record longer." % len(use)); return
    absmv = sorted(abs(e["mv"]) for e in ev)
    cut_t = sorted(r["open"] for r in use)[int(len(use) * 0.6)]
    print("%d recorded rounds, %d moments checked. Bitcoin move over the last 10 s: median $%.1f, top 5%% above $%.1f, top 2%% above $%.1f.\n" % (len(use), len(ev), absmv[len(absmv) // 2], absmv[int(len(absmv) * .95)], absmv[int(len(absmv) * .98)]))
    out = {}
    for label, q in (("top 10% jumps", .90), ("top 5% jumps", .95), ("top 2% jumps", .98)):
        thr = absmv[int(len(absmv) * q)]
        print("%s (Bitcoin moved more than $%.0f in 10 s), first one per round per 45 s:" % (label, thr))
        print("  wait     MOVE cents (t)        NET cents (t)       n     | older NET | newer NET")
        for h in HZ:
            seen, M, N, No, Nn = {}, [], [], [], []
            for e in ev:
                if abs(e["mv"]) < thr or e["t"] - seen.get(e["tk"], 0) < 45: continue
                if e["t"] + h > e["cl"] - 30: continue
                q0, q1 = qat(e["c"], e["cts"], e["t"]), qat(e["c"], e["cts"], e["t"] + h)
                if not q0 or not q1: continue
                up = e["mv"] > 0
                pin = q0[1] if up else 1 - q0[0]
                pout = q1[0] if up else 1 - q1[1]
                if not .05 <= pin <= .95: continue
                seen[e["tk"]] = e["t"]
                mv = ((q1[0] + q1[1]) / 2 - (q0[0] + q0[1]) / 2) * (1 if up else -1)
                net = pout - fee(pout) - pin - fee(pin)
                M.append(100 * mv); N.append(100 * net); (No if e["o"] < cut_t else Nn).append(100 * net)
            m, n = mean_t(M), mean_t(N)
            print("  %3d s   %+6.2f (t %+5.1f)    %+6.2f (t %+5.1f)   %4d  |  %+6.2f   |  %+6.2f" % (h, m[0], m[1], n[0], n[1], n[2], mean_t(No)[0], mean_t(Nn)[0]))
            out.setdefault(label, {})[h] = {"move": m, "net": n}
        print()
    print("How to read it: if MOVE is clearly positive at 5-30 s but NET is below zero, Kalshi lags Bitcoin but the cost (about 3 cents) is bigger than the lag. NET above zero in BOTH older and newer rounds is the lag edge.")
    json.dump({"made": int(time.time()), "rounds": len(use), "res": out}, open(__import__("os").path.join(__import__("os").path.expanduser("~"), "market-data", "history", "lag.json"), "w"))


if __name__ == "__main__":
    main()
