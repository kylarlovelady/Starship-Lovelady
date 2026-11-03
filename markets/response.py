"""SIGNAL vs RESPONSE (read-only). Separates two questions that a single win/loss number mixes together:
  1. INFORMATION: after the signal fires, does the Kalshi price move in the signal's direction? (before any trading cost)
  2. RESPONSE: if you trade it, which exit captures that move after the spread and fees: sell after 1 min, 2 min, 5 min, or hold to the end?
If the price moves your way but every response loses, the signal is good and the cost or timing is the problem.
Uses minute data (all downloaded rounds) for the signals that only need it. Usage: python3 response.py [days=14]"""
import sys, time, json
import signals as G, replay, hypothesis
from hypothesis import fee

NM = {"bmom60": "Bitcoin speed, 1 min", "bmom180": "Bitcoin speed, 3 min", "z": "Distance from target", "hr": "Trend, 1 hour", "tr15m": "Trend, 15 min",
      "tr4h": "Trend, 4 hours", "tr24h": "Trend, 24 hours", "tr7d": "Trend, 7 days"}
HZ = (("1 min", "bid60", "ask60", 60), ("2 min", "bid120", "ask120", 120), ("5 min", "bid300", "ask300", 300))


def mean_sd(v):
    n = len(v)
    if n < 5: return 0.0, 0.0, n
    m = sum(v) / n; sd = (sum((x - m) ** 2 for x in v) / (n - 1)) ** 0.5 or 1e-9
    return m, m / (sd / n ** 0.5), n


def fire(rows, nm, thr, lo, hi, dr):
    seen, out = set(), []
    for d in rows:
        if d["open"] in seen or not (lo <= d["el"] < hi): continue
        s = d["S"].get(nm)
        if s is None or abs(s) < thr: continue
        side = "UP" if (s > 0) == (dr > 0) else "DOWN"
        seen.add(d["open"]); out.append((d, side))
    return out


def analyse(trades):
    """For one signal setting: information (mid move, cents) and what each response nets after fees (cents per contract)."""
    res = {}
    for name, bk, ak, secs in HZ:
        mv, net = [], []
        for d, side in trades:
            if d[bk] is None or d["el"] + secs > 870: continue         # the round must still be open when we look: after the close the quote is stuck at the settlement
            now_mid = (d["bid"] + d["ask"]) / 2; later_mid = (d[bk] + d[ak]) / 2
            move = (later_mid - now_mid) * (1 if side == "UP" else -1)
            px_in = d["ask"] if side == "UP" else 1 - d["bid"]
            px_out = d[bk] if side == "UP" else 1 - d[ak]
            if not .03 <= px_in <= .97: continue
            mv.append(100 * move); net.append(100 * (px_out - fee(px_out) - px_in - fee(px_in)))
        res[name] = (mean_sd(mv), mean_sd(net))
    hold = []
    for d, side in trades:
        px_in = d["ask"] if side == "UP" else 1 - d["bid"]
        if not .03 <= px_in <= .97: continue
        won = (d["res"] == "UP") == (side == "UP")
        hold.append(100 * ((1.0 if won else 0.0) - px_in - fee(px_in)))
    res["to the end"] = (None, mean_sd(hold))
    return res


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    use, cand, ts_, vs_ = hypothesis.load(days)
    btc = replay.Series(ts_, vs_); G.STEP = 60
    _q = G.qat; G.qat = lambda r, t_, t, maxage=90: _q(r, t_, t, 90)
    rows = G.build(use, cand, btc, None)
    keep = set(NM)
    for d in rows: d["S"] = {k: v for k, v in d["S"].items() if k in keep}
    opens = sorted({d["open"] for d in rows}); cut = opens[int(len(opens) * 0.6)]
    tr = [d for d in rows if d["open"] < cut]; te = [d for d in rows if d["open"] >= cut]
    print("%d rounds. For each signal at its top 20%% strength, both directions, early (min 1-6) and late (min 6-12) in the round." % len(opens))
    print("MOVE = how far the Kalshi price moved your way after the signal, cents, before costs. NET = what selling then would have made after spread and fees.")
    print("Each cell: average (t-stat) on the NEWER rounds only, so it is not tuned to them.\n")
    out = {}
    for nm in NM:
        vals = sorted(abs(d["S"][nm]) for d in tr if d["S"].get(nm))
        if len(vals) < 200: continue
        thr = vals[int(len(vals) * 0.8)]
        best = None
        for lo, hi in ((G.FIRST, 360), (360, G.LAST + 1)):
            for dr in (1, -1):
                Tt = fire(tr, nm, thr, lo, hi, dr)                    # choose the way to use it on the OLDER rounds only
                if len(Tt) < 40: continue
                Rt = analyse(Tt)
                info = max((Rt[h][0][1] for h in ("1 min", "2 min", "5 min") if Rt[h][0][2] >= 15), default=-9)
                if best is None or info > best[0]: best = (info, lo, hi, dr)
        if best:
            T = fire(te, nm, thr, best[1], best[2], best[3])           # ...and report it on the NEWER rounds it never saw
            best = (best[0], best[1], best[2], best[3], analyse(T), len(T)) if len(T) >= 20 else None
        if not best: continue
        info, lo, hi, dr, R, n = best
        out[nm] = {"dir": dr, "lo": lo, "hi": hi, "n": n, "R": {k: [list(v[0]) if v[0] else None, list(v[1])] for k, v in R.items()}}
        print("%-22s %s the signal, minutes %d-%d, %d trades" % (NM[nm], "WITH" if dr > 0 else "AGAINST", lo // 60, hi // 60, n))
        for h in ("1 min", "2 min", "5 min", "to the end"):
            mv, nt = R[h]
            print("    %-10s %s NET %+6.1f (t %+.1f)" % (h, ("MOVE %+5.1f (t %+.1f)  " % (mv[0], mv[1])) if mv else "                          ", nt[0], nt[1]))
    print("\nHow to read it: a signal is INFORMATIVE if MOVE is clearly positive (t above 2) even when NET is negative. Then the trading response is the problem (fees and spread eat a small move), and a better entry/exit or a stronger trigger can fix it. If MOVE is about zero, the signal itself says nothing.")
    json.dump({"made": int(time.time()), "rounds": len(opens), "signals": out}, open(G._out().replace("signals.json", "response.json"), "w"))


if __name__ == "__main__":
    main()
