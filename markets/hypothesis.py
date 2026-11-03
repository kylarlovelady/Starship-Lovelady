"""Tests Kylar's way of reading a round on the old Kalshi rounds, read-only (nothing here touches the agent):
  buy AGAINST the long trend (hour-long move stretched one way), when the last few minutes are SLOWING, while BTC is still close to the
  target and there is plenty of time left. Then ask: did that beat just paying the price? Judged after fees, on older rounds first and
  then on newer rounds the choice was never tuned on.
Uses only what was known at the moment of the decision. Needs history from backfill.py (minute resolution).
Usage: python3 hypothesis.py [days=14]"""
import bisect, json, math, os, sys, time, itertools

HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
H = os.path.join(DIR, "history")


def fee(p):
    return 0.07 * p * (1 - p)


def load(days):
    cut = time.time() - days * 86400
    rounds = {}
    for ln in open(os.path.join(H, "rounds.jsonl")):
        r = json.loads(ln)
        if r["close"] >= cut and r.get("strike"):
            rounds[r["ticker"]] = r
    cand = {}
    for ln in open(os.path.join(H, "candles.jsonl")):
        r = json.loads(ln)
        if r["ticker"] in rounds and len(r["c"]) >= 8:
            cand[r["ticker"]] = sorted(r["c"])
    bt = {}
    for ln in open(os.path.join(H, "btc1m.jsonl")):
        for t, c in json.loads(ln)["r"]:
            bt[t + 60] = c
    ts = sorted(bt)
    use = sorted([r for r in rounds.values() if r["ticker"] in cand], key=lambda r: r["open"])
    return use, cand, ts, [bt[t] for t in ts]


def last(ts, vs, t, maxage=150):
    i = bisect.bisect_right(ts, t)
    return vs[i - 1] if i and t - ts[i - 1] <= maxage else None


def quote(c, t):
    i = bisect.bisect_right([x[0] for x in c], t)
    return (c[i - 1][1], c[i - 1][2]) if i and t - c[i - 1][0] <= 150 else None


def decisions(use, cand, ts, vs):
    """One row per round and decision minute, with everything known at that moment and what happened after."""
    out = []
    for r in use:
        o, cl, strike, c = r["open"], r["close"], float(r["strike"]), cand[r["ticker"]]
        for m in range(2, 13):
            t = o + 60 * m
            px = last(ts, vs, t); p5 = last(ts, vs, t - 300); p2 = last(ts, vs, t - 120); p4 = last(ts, vs, t - 240); p60 = last(ts, vs, t - 3600); p15 = last(ts, vs, t - 900)
            q = quote(c, t)
            if None in (px, p5, p2, p4, p60, p15) or q is None or q[1] < q[0]:
                continue
            q5 = quote(c, t + 300)
            out.append({"open": o, "m": m, "left": 900 - 60 * m, "dist": px - strike, "hr": px / p60 - 1, "q15": px / p15 - 1,
                        "v_now": (px - p2) / 2.0, "v_prev": (p2 - p4) / 2.0, "bid": q[0], "ask": q[1], "res": r["result"],
                        "bid5": q5[0] if q5 else None, "ask5": q5[1] if q5 else None})
    return out


def result(d, side):
    """Profit per contract after fees: buy at the ask, hold to the end; and buy, sell 5 minutes later at the bid."""
    px = d["ask"] if side == "UP" else 1 - d["bid"]
    if not (0.03 <= px <= 0.97):
        return None
    cost = px + fee(px)
    won = (d["res"] == "UP") == (side == "UP")
    hold = (1.0 if won else 0.0) - cost
    ex = None
    if d["bid5"] is not None:
        s5 = d["bid5"] if side == "UP" else 1 - d["ask5"]
        ex = s5 - fee(s5) - cost
    return {"px": px, "hold": hold, "exit5": ex, "won": won}


def pick(rows, thr, dist, slow, maxm, side_rule="against"):
    """First moment in each round that matches the rule (one entry per round, so rounds are not counted twice)."""
    chosen, seen = [], set()
    for d in rows:
        if d["open"] in seen or d["m"] > maxm:
            continue
        hr = d["hr"]
        if abs(hr) < thr or abs(d["dist"]) > dist:
            continue
        side = "DOWN" if hr > 0 else "UP"                    # against the hour-long trend
        fade = abs(d["v_now"]) < 0.5 * abs(d["v_prev"]) if abs(d["v_prev"]) > 0 else True
        if slow and not fade:
            continue
        if slow and (d["v_prev"] * hr) < 0:                  # the last few minutes were not even moving with the trend
            continue
        r = result(d, side)
        if r is None:
            continue
        seen.add(d["open"]); chosen.append(dict(r, side=side, open=d["open"]))
    return chosen


def stats(ch):
    if not ch:
        return None
    n = len(ch)
    avg = lambda k: sum(x[k] for x in ch if x[k] is not None) / max(1, sum(1 for x in ch if x[k] is not None))
    return {"n": n, "win": 100.0 * sum(1 for x in ch if x["won"]) / n, "hold": avg("hold"), "exit5": avg("exit5"), "px": avg("px"),
            "roi": avg("hold") / max(1e-9, avg("px"))}


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    use, cand, ts, vs = load(days)
    rows = decisions(use, cand, ts, vs)
    if len(use) < 60 or not rows:
        print("Not enough history (%d rounds with an hour of Bitcoin data before them). Run backfill.py first." % len(use)); return
    cut = use[int(len(use) * 0.7)]["open"]
    tr = [d for d in rows if d["open"] < cut]; te = [d for d in rows if d["open"] >= cut]
    print("YOUR READING OF A ROUND, tested on %d old rounds (older 70%% to choose, newer 30%% to check)" % len(use))
    print("rule: buy AGAINST the hour-long trend, only if BTC is within $D of the target, early enough (first M minutes), optionally only when the last 2 minutes are slower than the 2 before")
    print("results are cents per contract after fees, win rate, and return on the money staked")
    base = []
    for d in rows:
        if d["m"] in (3, 5):
            for side in ("UP", "DOWN"):
                r = result(d, side)
                if r: base.append(r)
    b = stats(base)
    print("baseline (buy either side at minute 3 or 5, no rule): hold %+.1fc, 5-minute exit %+.1fc, win %.0f%% over %d buys\n" % (100 * b["hold"], 100 * b["exit5"], b["win"], b["n"]))
    print("  hour-trend  within   slowing  last-min |  OLDER rounds: n  win%%  hold  exit5  ROI |  NEWER rounds: n  win%%  hold  exit5  ROI")
    res = []
    for thr, dist, slow, maxm in itertools.product((0.001, 0.002, 0.003), (40, 80, 150), (False, True), (7,)):
        a, c = stats(pick(tr, thr, dist, slow, maxm)), stats(pick(te, thr, dist, slow, maxm))
        if not a or a["n"] < 15 or not c:
            continue
        res.append((a["hold"], thr, dist, slow, maxm, a, c))
    res.sort(key=lambda x: -x[0])
    f = lambda s: "%3d %4.0f %+5.1f %+5.1f %+5.0f%%" % (s["n"], s["win"], 100 * s["hold"], 100 * s["exit5"], 100 * s["roi"])
    for _, thr, dist, slow, maxm, a, c in res[:8]:
        print("  >=%.1f%%    $%-4d  %-7s  m<=%d    | %s | %s" % (100 * thr, dist, "yes" if slow else "no", maxm, f(a), f(c)))
    if res:
        print("\nworst:")
        for _, thr, dist, slow, maxm, a, c in res[-2:]:
            print("  >=%.1f%%    $%-4d  %-7s  m<=%d    | %s | %s" % (100 * thr, dist, "yes" if slow else "no", maxm, f(a), f(c)))
    # price view: where does the money come from?
    allp = []
    for thr, dist, slow, maxm in ((0.002, 80, True, 7),):
        for d in (pick(tr, thr, dist, slow, maxm) + pick(te, thr, dist, slow, maxm)):
            allp.append(d)
    if allp:
        print("\nfor the rule (>=0.2%% trend, within $80, slowing, first 7 minutes), by the price paid, all %d rounds:" % len(allp))
        for lo, hi in ((0, 30), (30, 45), (45, 60), (60, 100)):
            g = [x for x in allp if lo <= x["px"] * 100 < hi]
            s = stats(g)
            if s: print("   %2d-%3dc: %3d buys, win %3.0f%%, hold %+5.1fc per contract, return %+4.0f%% on the stake" % (lo, hi, s["n"], s["win"], 100 * s["hold"], 100 * s["roi"]))
    print("\nread this carefully: a rule that wins on the older rounds but not on the newer ones was luck. Only a rule that is positive on BOTH counts, and even then it takes more rounds to be sure.")
    json.dump({"made": int(time.time()), "rounds": len(use), "baseline": b, "top": [{"thr": r[1], "dist": r[2], "slow": r[3], "older": r[5], "newer": r[6]} for r in res[:8]]}, open(os.path.join(H, "hypothesis.json"), "w"))


if __name__ == "__main__":
    main()
