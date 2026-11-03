"""SIGNAL SCAN (read-only). Tries many ideas, each in BOTH directions (with the signal and against it), on the second-by-second rounds
the agent recorded. Signals include the SPEED of Bitcoin, the SPEED of the Kalshi price ticker, slowing down, distance from target,
and the hour trend. Every buy uses the real Kalshi ask for that side, fees included, one buy per round per idea, nothing from the future.
It lists ideas that were positive (or consistently negative = flip candidates) in BOTH the older and the newer rounds.
Usage: python3 signals.py [days=14]"""
import bisect, math, os, sys, json, time, itertools
from hypothesis import fee

STEP, FIRST, LAST = 10, 60, 720          # look every 10 s between minute 1 and minute 12

def qat(rows, ts, t, maxage=20):
    i = bisect.bisect_right(ts, t)
    return (rows[i - 1][1], rows[i - 1][2]) if i and t - ts[i - 1] <= maxage else None

def extras(days):
    """Every extra feed the recorder keeps, as (times, values): the second exchange, trade flow, open interest, and the Kalshi book depth."""
    import glob, exit_learn as X
    D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
    cut = time.time() - days * 86400
    E = {k: ([], []) for k in ("kraken", "flow", "oi", "book")}
    def put(k, t, v):
        if v is not None and (not E[k][0] or t - E[k][0][-1] >= 2.0):
            E[k][0].append(t); E[k][1].append(v)
    sz = lambda arr: sum(float(x[1]) for x in (arr or [])[-3:] if isinstance(x, (list, tuple)) and len(x) > 1)
    for pth in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
        for r in X._lines(pth):
            t = r.get("t")
            if not t or t < cut: continue
            x = r.get("x") or {}
            if x.get("kraken"): put("kraken", t, float(x["kraken"]))
            f = r.get("flow")
            if f and (f.get("buy_usd", 0) + f.get("sell_usd", 0)) > 0:
                put("flow", t, (f["buy_usd"] - f["sell_usd"]) / float(f["buy_usd"] + f["sell_usd"]))
            o = r.get("oi")
            if o and o.get("oi_usd"): put("oi", t, float(o["oi_usd"]))
            ob = r.get("ob") or {}
            y, n = sz(ob.get("yes") or ob.get("yes_dollars")), sz(ob.get("no") or ob.get("no_dollars"))
            if y + n > 0: put("book", t, (y - n) / (y + n))
    return E

def eat(E, k, t, maxage=30):
    ts, vs = E[k]
    i = bisect.bisect_right(ts, t)
    return vs[i - 1] if i and t - ts[i - 1] <= maxage else None

def eavg(E, k, t, span=15):
    ts, vs = E[k]
    i, j = bisect.bisect_right(ts, t), bisect.bisect_right(ts, t - span)
    return sum(vs[j:i]) / (i - j) if i - j >= 2 else None

def build(use, cand, btc, E=None):
    """One row per round and moment with every signal score and what it would have cost / paid."""
    out = []
    for r in use:
        tk, o, cl, strike = r["ticker"], r["open"], r["close"], float(r["strike"])
        c = cand[tk]; cts = [x[0] for x in c]
        for el in range(FIRST, LAST + 1, STEP):
            t = o + el
            q = qat(c, cts, t)
            b = btc.at(t); b10, b30, b60, b120, b180, bh = (btc.at(t - k) for k in (10, 30, 60, 120, 180, 3600))
            if q is None or None in (b, b10, b30, b60, b120, b180, bh) or q[1] < q[0]:
                continue
            q30, q60, q120 = qat(c, cts, t - 30), qat(c, cts, t - 60), qat(c, cts, t - 120)
            if None in (q30, q60, q120):
                continue
            m = lambda x: (x[0] + x[1]) / 2
            rets = []
            for k in range(0, 15):
                a, bb = btc.at(t - 60 * k), btc.at(t - 60 * (k + 1))
                if a and bb: rets.append(math.log(a / bb))
            if len(rets) < 10: continue
            vol = math.sqrt(sum(x * x for x in rets) / len(rets)) or 1e-5
            sig = vol * b * math.sqrt(max(cl - t, 30) / 60.0)
            qe = qat(c, cts, t + 60)
            v30, vprev = abs(b - b30) / 30.0, abs(b30 - b120) / 90.0
            S = {"bmom60": (b - b60) / b * 1e4, "bmom180": (b - b180) / b * 1e4, "bmom10": (b - b10) / b * 1e4,
                 "kmom30": 100 * (m(q) - m(q30)), "kmom60": 100 * (m(q) - m(q60)),
                 "z": max(-4, min(4, (b - strike) / sig)), "hr": (b / bh - 1) * 1e4,
                 # slowing: it was moving (prior 90 s) and has now nearly stopped; the score is the direction it WAS moving
                 "bslow": (b30 - b120) / b * 1e4 if v30 < 0.4 * vprev else 0.0,
                 "kslow": 100 * (m(q30) - m(q120)) if abs(m(q) - m(q30)) < 0.4 * abs(m(q30) - m(q120)) / 3 else 0.0}
            if E:
                kr = eat(E, "kraken", t, 20)
                if kr: S["xdiv"] = (b - kr) / b * 1e4                    # Coinbase vs Kraken, in basis points: who is ahead
                fl = eavg(E, "flow", t, 15)
                if fl is not None: S["flow"] = fl * 100                   # recent buying minus selling, as a percent of volume
                o1, o0 = eat(E, "oi", t, 90), eat(E, "oi", t - 300, 90)
                if o1 and o0: S["oichg"] = (o1 / o0 - 1) * 1e4           # open interest change over 5 minutes
                bk = eavg(E, "book", t, 10)
                if bk is not None: S["bookimb"] = bk * 100               # Kalshi book: more size waiting on Up (+) or Down (-)
            out.append({"open": o, "el": el, "S": S, "ask": q[1], "bid": q[0], "res": r["result"],
                        "bid60": qe[0] if qe else None, "ask60": qe[1] if qe else None})
    return out

def evaluate(rows, name, thr, lo, hi, dr):
    seen, L = set(), []
    for d in rows:
        if d["open"] in seen or not (lo <= d["el"] < hi): continue
        s = d["S"].get(name)
        if s is None or abs(s) < thr: continue
        side = "UP" if (s > 0) == (dr > 0) else "DOWN"
        px = d["ask"] if side == "UP" else 1 - d["bid"]
        if not .05 <= px <= .95: continue
        won = (d["res"] == "UP") == (side == "UP")
        ex = None
        if d["bid60"] is not None:
            s60 = d["bid60"] if side == "UP" else 1 - d["ask60"]; ex = s60 - fee(s60) - px - fee(px)
        seen.add(d["open"]); L.append({"hold": (1.0 if won else 0.0) - px - fee(px), "exit": ex, "px": px, "won": won})
    return L

def avg(L, k="hold"):
    v = [x[k] for x in L if x[k] is not None]
    return sum(v) / len(v) if v else 0.0

def _out():
    from hypothesis import H
    os.makedirs(H, exist_ok=True)
    return os.path.join(H, "signals.json")

def scan(use, cand, btc, E=None):
    rows = build(use, cand, btc, E)
    if len({d["open"] for d in rows}) < 60: print("Only %d recorded rounds with an hour of Bitcoin before them; need ~60+. Let it record longer." % len({d['open'] for d in rows})); return
    opens = sorted({d["open"] for d in rows}); cut = opens[int(len(opens) * 0.6)]
    tr = [d for d in rows if d["open"] < cut]; te = [d for d in rows if d["open"] >= cut]
    names = sorted({k for d in rows for k in d["S"]})
    results = []
    for nm in names:
        vals = sorted(abs(d["S"][nm]) for d in tr if d["S"].get(nm))
        if len(vals) < 200: continue
        for pct in (0.6, 0.8, 0.93):
            thr = vals[int(len(vals) * pct)]
            for lo, hi in ((FIRST, 360), (360, LAST + 1)):
                for dr in (1, -1):
                    A, B = evaluate(tr, nm, thr, lo, hi, dr), evaluate(te, nm, thr, lo, hi, dr)
                    if len(A) < 30 or len(B) < 15: continue
                    results.append((nm, pct, thr, lo, hi, dr, A, B))
    print("%d recorded rounds (%d older to choose / %d newer to check), %d ideas tried. Cents per contract after fees, held to the end.\n" % (len(opens), len({d['open'] for d in tr}), len({d['open'] for d in te}), len(results)))
    hdr = "%-8s %-4s %-12s %-7s | OLDER n win%% hold exit | NEWER n win%% hold exit"
    def line(r):
        nm, pct, thr, lo, hi, dr, A, B = r
        f = lambda L: "%3d %3.0f %+5.1f %+5.1f" % (len(L), 100 * sum(x["won"] for x in L) / len(L), 100 * avg(L), 100 * avg(L, "exit"))
        return "%-8s %-4s %-12s %-7s | %s | %s" % (nm, "top%d%%" % round(100 * (1 - pct)), "min %d-%d" % (lo // 60, hi // 60), "WITH" if dr > 0 else "AGAINST", f(A), f(B))
    print(hdr % ("signal", "size", "when", "bet"))
    good = [r for r in results if avg(r[6]) > 0.01 and avg(r[7]) > 0.01]
    good.sort(key=lambda r: -min(avg(r[6]), avg(r[7])))
    print("\nWINNERS (positive after fees in BOTH older and newer):")
    for r in good[:8]: print(" ", line(r))
    if not good: print("  none")
    # losers worth flipping: the OTHER side of a clearly losing idea is evaluated directly above (dir=-1 is the flip), so just show the worst
    bad = sorted(results, key=lambda r: max(avg(r[6]), avg(r[7])))
    print("\nCONSISTENT LOSERS (negative in both halves; the opposite direction is listed above as its own idea):")
    for r in bad[:6]: print(" ", line(r))
    exp = max(1, round(len(results) * 0.05))
    print("\n%d ideas were tried, so by pure luck about %d would look like winners. A real one should also keep winning as new rounds arrive. Check again tomorrow." % (len(results), exp))
    json.dump({"made": int(time.time()), "rounds": len(opens), "ideas": len(results), "winners": [{"sig": r[0], "pct": r[1], "lo": r[3], "hi": r[4], "dir": r[5], "older": avg(r[6]), "newer": avg(r[7]), "n": [len(r[6]), len(r[7])]} for r in good[:8]]}, open(_out(), "w"))

if __name__ == "__main__":
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    import replay
    use, cand, btc = replay.load_ticks(days)
    scan(use, cand, btc, extras(days))
