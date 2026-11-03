"""Learns P(UP) from past rounds (distance-to-target scaled by volatility and time left, hour trend, recent speed, time left, market price)
and trades only when the model's probability beats the price plus fee by a margin. Strictly walk-forward: each block of rounds is
scored by a model trained ONLY on earlier rounds. Read-only. Usage: python3 walkforward.py [days=14]"""
import math, os, sys, json, bisect
from hypothesis import load, last, quote, fee, H

def feats(px, strike, left, hr, q15, vnow, vprev, vol, mid, use_mkt):
    sig = max(1e-5, vol) * px * math.sqrt(max(left, 30) / 60.0)
    z = max(-4, min(4, (px - strike) / sig))
    f = [1.0, z, abs(z) * z, hr * 100, q15 * 100, vnow / px * 1e4, vprev / px * 1e4, left / 900.0]
    if use_mkt:
        m = min(.97, max(.03, mid)); f.append(math.log(m / (1 - m)))
    return f

def rows(use, cand, ts, vs, use_mkt):
    out = []
    for r in use:
        o, strike, c = r["open"], float(r["strike"]), cand[r["ticker"]]
        for m in range(1, 14):
            t = o + 60 * m
            px = last(ts, vs, t); q = quote(c, t)
            ps = [last(ts, vs, t - 60 * k) for k in range(0, 16)]
            if q is None or q[1] < q[0] or None in ps or None in (last(ts, vs, t - 3600),): continue
            p60 = last(ts, vs, t - 3600)
            rets = [math.log(ps[k] / ps[k + 1]) for k in range(15)]
            vol = math.sqrt(sum(x * x for x in rets) / 15)
            mid = (q[0] + q[1]) / 2
            f = feats(px, strike, 900 - 60 * m, px / p60 - 1, px / ps[15] - 1, (px - ps[2]) / 2, (ps[2] - ps[4]) / 2, vol, mid, use_mkt)
            out.append({"open": o, "m": m, "f": f, "y": 1 if r["result"] == "UP" else 0, "bid": q[0], "ask": q[1]})
    return out

def train(X, Y, epochs=60, lr=0.05, l2=0.002):
    n = len(X[0]); w = [0.0] * n
    for e in range(epochs):
        for x, y in zip(X, Y):
            z = sum(a * b for a, b in zip(w, x)); p = 1 / (1 + math.exp(-max(-30, min(30, z))))
            g = p - y
            for i in range(n): w[i] -= lr * (g * x[i] + l2 * w[i])
    return w

def prob(w, x):
    z = sum(a * b for a, b in zip(w, x)); return 1 / (1 + math.exp(-max(-30, min(30, z))))

def run(use, cand, ts, vs, use_mkt, margins):
    R = rows(use, cand, ts, vs, use_mkt)
    opens = sorted({d["open"] for d in R}); N = len(opens)
    start = int(N * 0.4); step = max(40, N // 12)
    res = {mg: [] for mg in margins}
    i = start
    while i < N:
        tr = [d for d in R if d["open"] < opens[i]]; te = [d for d in R if opens[i] <= d["open"] < (opens[min(N - 1, i + step)] if i + step < N else 1e18)]
        w = train([d["f"] for d in tr][::2], [d["y"] for d in tr][::2], epochs=25)
        seen = {mg: set() for mg in margins}
        for d in te:
            p = prob(w, d["f"])
            for mg in margins:
                if d["open"] in seen[mg]: continue
                for side, px, pw in (("UP", d["ask"], p), ("DOWN", 1 - d["bid"], 1 - p)):
                    if not (.05 <= px <= .95): continue
                    if pw - px - fee(px) > mg:
                        won = (d["y"] == 1) == (side == "UP")
                        res[mg].append({"px": px, "hold": (1.0 if won else 0.0) - px - fee(px), "won": won, "open": d["open"]})
                        seen[mg].add(d["open"]); break
        i += step
    return res, opens[start]

def show(name, res):
    print(name)
    for mg, L in sorted(res.items()):
        if not L: print("  margin %2.0fc: no trades" % (100 * mg)); continue
        n = len(L); a = sum(x["hold"] for x in L) / n; px = sum(x["px"] for x in L) / n
        half = n // 2; a1 = sum(x["hold"] for x in L[:half]) / max(1, half); a2 = sum(x["hold"] for x in L[half:]) / max(1, n - half)
        print("  margin %2.0fc: %4d trades, win %3.0f%%, avg price %2.0fc, after fees %+5.1fc each (%+4.0f%%) | first half %+5.1fc, second half %+5.1fc" % (100 * mg, n, 100 * sum(x["won"] for x in L) / n, 100 * px, 100 * a, 100 * a / px, 100 * a1, 100 * a2))

if __name__ == "__main__":
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    use, cand, ts, vs = load(days)
    print("%d old rounds. Each block is scored by a model trained only on EARLIER rounds. Results are after fees, per contract, hold to the end.\n" % len(use))
    for um, nm in ((False, "MODEL FROM BTC ONLY (distance/time/trend/speed, ignores the price)"), (True, "MODEL WITH THE MARKET PRICE AS AN INPUT")):
        r, s = run(use, cand, ts, vs, um, (0.03, 0.06, 0.10, 0.15)); show(nm, r); print()
