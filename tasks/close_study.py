#!/usr/bin/env python3
"""Close study (Kylar 21:21): (1) how fast BTC moves per second, (2) does Kalshi ever close a round EARLY (status/close_time from the recorder 'ks' field, since 20:13),
(3) when does the favourite stop being buyable below 99c, and what 'distance in standard deviations' (z = gap / (sigma_per_s * sqrt(seconds left))) is the market at then,
(4) for a z-rule of our own (z >= 2, 2.5, 3, 3.5, 4): how many seconds before the close it triggers, what the ask is, whether $ is buyable, win rate and profit per $.
Practice analysis only. Writes memory/inbox/close-study.md."""
import glob, gzip, json, os, math, statistics as st, collections
HOME = os.path.expanduser("~"); D = HOME + "/market-data"; OUT = HOME + "/starship/memory/inbox/close-study.md"
R = {}
try:
    for l in open(D + "/history/rounds.jsonl"):
        try: r = json.loads(l); R[r.get("ticker")] = r.get("result")
        except ValueError: pass
except OSError: pass
rounds = collections.defaultdict(dict)       # tk -> {left: (px, strike, bid_y, bid_n, yb_levels, nb_levels)}
early = []; ccount = collections.Counter(); ct = collections.defaultdict(set)
def lv(x, sc):
    o = []
    for a in x or []:
        try: o.append((float(a[0]) / sc, float(a[1])))
        except Exception: pass
    return o
for p in sorted(glob.glob(D + "/ticks-*.jsonl*")):
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: r = json.loads(l)
                except ValueError: continue
                k = r.get("k") or {}; tk = k.get("ticker"); s = r.get("left"); px = r.get("px")
                ks = r.get("ks") or {}
                cur = ks.get("cur") or {}
                if cur.get("tk"):
                    ct[cur["tk"]].add(cur.get("close_time")); ccount["ks_rows"] += 1
                    if cur.get("can_close_early"): ccount["can_close_early"] += 1
                    if cur.get("status") not in (None, "active", "open") and s is not None and s > 3: early.append((cur["tk"], cur.get("status"), s))
                if tk is None or s is None or px is None or s < 0 or s > 899: continue
                ob = r.get("ob") or {}; yl, nl = ob.get("yes_dollars") or ob.get("yes"), ob.get("no_dollars") or ob.get("no")
                both = list(yl or []) + list(nl or [])
                sc = 1.0 if both and max(float(a[0]) for a in both) <= 1.0 else 100.0
                rounds[tk][s] = (float(px), k.get("floor_strike"), lv(yl, sc), lv(nl, sc))
    except OSError: continue
L = ["# Close study (auto)", "", "Rounds with ticks: %d; rounds with a real settled result: %d" % (len(rounds), sum(1 for t in rounds if R.get(t))), ""]
# (1) per-second movement
d = []
for tk, rr in rounds.items():
    ss = sorted(rr, reverse=True)
    for a, b in zip(ss, ss[1:]):
        if a - b == 1: d.append(rr[b][0] - rr[a][0])
if d:
    ad = sorted(abs(x) for x in d); n = len(ad)
    L += ["## 1. How fast BTC moves per second (Coinbase, USD)", "", "- %d one-second changes: average size $%.2f, typical (std) $%.2f, 90th percentile $%.2f, 99th $%.2f, 99.9th $%.2f, biggest $%.2f." % (n, sum(ad) / n, st.pstdev(d), ad[int(.9 * n)], ad[int(.99 * n)], ad[int(.999 * n)], ad[-1]),
          "- So in 60 s BTC typically wanders about $%.0f (std), and in 10 s about $%.0f; the sqrt-of-time rule is what the z formula below uses." % (st.pstdev(d) * math.sqrt(60), st.pstdev(d) * math.sqrt(10)), ""]
# (2) early close
L += ["## 2. Does Kalshi close rounds early?", "", "- Recorder status rows since 20:13: %d; rows where can_close_early was true: %d." % (ccount["ks_rows"], ccount["can_close_early"]),
      "- Rounds whose reported close_time CHANGED during the round: %d of %d. Rounds seen with a non-active status more than 3 s before the 15:00 close: %d %s" % (sum(1 for v in ct.values() if len(v) > 1), len(ct), len(early), early[:5]), ""]
# (3)+(4)
def side_ask(side_yes, yl, nl):
    opp = nl if side_yes else yl
    asks = sorted(((1 - p, q) for p, q in opp), key=lambda x: x[0])
    return asks
def win(tk, rr, side_yes):
    res = R.get(tk)
    if res in ("UP", "DOWN"): return (res == "UP") == side_yes
    s0 = sorted(rr)[:60]
    if len(s0) < 30: return None
    avg = sum(rr[s][0] for s in s0) / len(s0); strike = rr[s0[0]][1]
    if strike is None: return None
    return (avg > strike) == side_yes
L99 = []; zat = []; cross = {z: [] for z in (2, 2.5, 3, 3.5, 4)}
for tk, rr in rounds.items():
    ss = sorted(rr, reverse=True)
    if len(ss) < 200: continue
    # last second the favourite was still buyable below 99c
    last = None
    for s in ss:
        px, strike, yl, nl = rr[s]
        if not yl or not nl: continue
        fy = max(a for a, b in yl) >= max(a for a, b in nl)
        a = side_ask(fy, yl, nl)
        if a and a[0][0] < 0.99: last = s
    if last is not None: L99.append(last)
    # rolling sigma per second from the last 60 s of prices
    pxs = {s: rr[s][0] for s in ss}
    done = set()
    for s in ss:
        if s < 1: continue
        px, strike, yl, nl = rr[s]
        if strike is None: continue
        w = [pxs[x] for x in range(s + 60, s, -1) if x in pxs]
        if len(w) < 40: continue
        dd = [b - a for a, b in zip(w, w[1:])]
        sg = st.pstdev(dd) if len(dd) > 5 else None
        if not sg or sg <= 0: continue
        gap = px - strike; z = abs(gap) / (sg * math.sqrt(s)); sy = gap > 0
        for zt in cross:
            if zt in done or z < zt: continue
            done.add(zt)
            if not yl or not nl: cross[zt].append((s, None, 0.0, win(tk, rr, sy))); continue
            a = side_ask(sy, yl, nl); depth = sum(q * p for p, q in a if p <= 0.99 + 1e-9)
            cross[zt].append((s, a[0][0] if a else 1.0, depth, win(tk, rr, sy)))
if L99:
    q = sorted(L99); n = len(q)
    L += ["## 3. When does the favourite stop being buyable below 99c?", "", "- Last second with an ask under 99c, seconds before the close: median %d, 10th percentile %d, 90th percentile %d (%d rounds). After that moment there is nothing to buy below 99c." % (q[n // 2], q[int(.1 * n)], q[int(.9 * n)], n), ""]
L += ["## 4. Our own z-rule: first moment the model's side is z standard deviations from the target", "", "| z | rounds | median s before close | median ask | share with an ask under 99c | median $ buyable | win rate | profit per $ (ask under 99c only) |", "|---|---|---|---|---|---|---|---|"]
for zt, v in cross.items():
    if not v: continue
    n = len(v); ss = sorted(x[0] for x in v); asks = sorted(x[1] for x in v if x[1] is not None); dp = sorted(x[2] for x in v)
    ok = [x for x in v if x[1] is not None and x[1] < 0.99 and x[3] is not None]
    w = [x for x in v if x[3] is not None]
    wr = 100.0 * sum(1 for x in w if x[3]) / len(w) if w else float("nan")
    pr = float("nan")
    if ok:
        tot = sum(x[1] + 0.07 * x[1] * (1 - x[1]) for x in ok); g = sum(1.0 for x in ok if x[3]); pr = 100.0 * (g - tot) / tot
    L.append("| %.1f | %d | %d | %s | %.0f%% | $%.0f | %.1f%% | %s |" % (zt, n, ss[n // 2], ("%.3f" % asks[len(asks) // 2]) if asks else "-", 100.0 * sum(1 for x in v if x[1] is not None and x[1] < 0.99) / n, dp[n // 2], wr, ("%+.1f%% (%d bets)" % (pr, len(ok))) if ok else "-"))
L += ["", "Win = real settled result when known, otherwise the average of the last 60 Coinbase prices vs the target (stand-in for Kalshi's average)."]
open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L))
