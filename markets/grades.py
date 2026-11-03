"""PER-SIGNAL SCORECARD. Every signal is graded on its own, nothing lumped. For each one: its best way of using it (with the signal or
against it, early or late in the round, how strong it has to be), chosen on the OLDER rounds and then checked on the NEWER rounds it
never saw. Cents per contract after real fees. Then a suggested weight that starts from YOUR rating and moves with the evidence.
Read-only. Usage: python3 grades.py [days=14]"""
import json, os, sys, time
import signals as G
from signals import evaluate, avg

# Kylar's starting ratings (voice session, Nov 3): high=1.0, medium-high=.75, medium=.5, low=.25, ignore=0. None = not rated yet.
RATING = {"bmom10": "high", "bmom60": "high", "bmom180": "high", "kmom30": "medium", "kmom60": "medium", "bslow": "high", "kslow": "high",
          "z": "high", "hr": "medium-high", "xdiv": "low", "xdiv2": "low", "flow": "medium", "oichg": "low", "bookimb": "medium",
          "cbbook": "low", "funding": "low", "liq": "medium-high",
          # rated by Claude on 2026-11-03 at Kylar's request ("go with yours"); change any of these any time
          "tr15m": "medium-high", "tr4h": "medium", "tr24h": "medium-high", "tr7d": "medium", "a_news": "medium-high", "a_whales": "medium",
          "a_bigtrades": "medium", "a_fng": "low", "a_levels": "medium"}
LABEL = {"bmom10": "Bitcoin speed, 10 s", "bmom60": "Bitcoin speed, 1 min", "bmom180": "Bitcoin speed, 3 min", "kmom30": "Kalshi ticker speed, 30 s",
         "kmom60": "Kalshi ticker speed, 1 min", "bslow": "Bitcoin slowing down", "kslow": "Kalshi ticker slowing down", "z": "Distance from target (vs time left)",
         "hr": "Trend, 1 hour", "tr15m": "Trend, 15 min", "tr4h": "Trend, 4 hours", "tr24h": "Trend, 24 hours", "tr7d": "Trend, 7 days",
         "xdiv": "Coinbase vs Kraken gap", "xdiv2": "Coinbase vs Bybit gap", "flow": "Trade flow (buyers vs sellers)", "oichg": "Open interest change",
         "bookimb": "Kalshi order book imbalance", "cbbook": "Coinbase order book", "funding": "Funding rate", "liq": "Liquidations",
         "a_news": "News mood", "a_whales": "Whale moves onto/off exchanges", "a_bigtrades": "Big exchange trades", "a_fng": "Fear & Greed",
         "a_funding": "Funding (agent's reading)", "a_trend_h": "Agent's 1h/4h/24h trend blend", "a_trend_w": "Agent's 7d/30d trend blend",
         "a_levels": "Support and resistance", "a_book": "Agent's order book reading", "a_momentum": "Agent's momentum reading",
         "a_SCORE": "Agent's overall score", "a_PMODEL": "Agent's model odds"}
VAL = {"high": 1.0, "medium-high": .75, "medium": .5, "low": .25, "ignore": 0.0}


def tstat(L):
    v = [x["hold"] for x in L]
    if len(v) < 5: return 0.0
    m = sum(v) / len(v); sd = (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5 or 1e-9
    return m / (sd / len(v) ** 0.5)


def grade(older, newer, t=0.0):
    """older/newer: average cents per contract of the best setting, in dollars. Expect about -2.5c for a signal with no information."""
    if older > 0.005 and newer > 0.005 and t >= 1.65: return "EDGE"
    if older > 0 and newer > 0: return "maybe"       # positive in both, but too few trades to rule out luck
    if older < -0.045 and newer < -0.045: return "FLIP?"
    return "no info"


def main():
    minute = "--minute" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    days = float(args[0]) if args else 14
    import replay
    if minute:
        # the signals that only need minute prices (trends, distance, Bitcoin 1-3 min speed), graded on every old round we downloaded
        import hypothesis
        use, cand, ts_, vs_ = hypothesis.load(days)
        btc = replay.Series(ts_, vs_); E = None
        G.STEP = 60
        _q = G.qat; G.qat = lambda rows_, ts, t, maxage=90: _q(rows_, ts, t, 90)
    else:
        use, cand, btc = replay.load_ticks(days); btc = G.with_history(btc)
        E = G.extras(days)
    rows = G.build(use, cand, btc, E)
    if minute:
        keep = {"hr", "tr15m", "tr4h", "tr24h", "tr7d", "z", "bmom60", "bmom180"}
        for d in rows: d["S"] = {k: v for k, v in d["S"].items() if k in keep}
    opens = sorted({d["open"] for d in rows})
    if len(opens) < 40:
        print("Only %d usable recorded rounds so far; need ~60+ for grades to mean anything. Let it record longer." % len(opens)); return
    cut = opens[int(len(opens) * 0.6)]
    tr = [d for d in rows if d["open"] < cut]; te = [d for d in rows if d["open"] >= cut]
    names = sorted({k for d in rows for k in d["S"]})
    out = {}
    for nm in names:
        vals = sorted(abs(d["S"][nm]) for d in tr if d["S"].get(nm))
        if len(vals) < 150: out[nm] = None; continue
        best = None
        for pct in (0.6, 0.8, 0.93):
            thr = vals[int(len(vals) * pct)]
            for lo, hi in ((G.FIRST, 360), (360, G.LAST + 1)):
                for dr in (1, -1):
                    A = evaluate(tr, nm, thr, lo, hi, dr)
                    if len(A) < 30: continue
                    B = evaluate(te, nm, thr, lo, hi, dr)
                    if len(B) < 15: continue
                    if best is None or avg(A) > best[0]: best = (avg(A), avg(B), len(A), len(B), pct, lo, hi, dr, tstat(B))
        out[nm] = best
    print("%d rounds (%d older / %d newer). Expect about -2c to -3c for a signal that tells us nothing (that is the cost of trading).\n" % (len(opens), len({d['open'] for d in tr}), len({d['open'] for d in te})))
    print("%-34s %-6s %-10s %-8s %-4s %-9s | older  newer  | grade   | rating -> weight" % ("signal", "use", "strength", "when", "n", "best way"))
    W = {}
    for nm in sorted(out, key=lambda k: -(out[k][1] if out[k] else -9)):
        lab = LABEL.get(nm, nm); r = RATING.get(nm); b = out[nm]
        if b is None:
            print("%-34s too few trades at any strength to grade yet | rating %s" % (lab, r or "NOT RATED")); W[nm] = {"label": lab, "rating": r, "grade": "no data", "weight": None}; continue
        older, newer, na, nb, pct, lo, hi, dr = b[:8]
        g = grade(older, newer, b[8])
        base = VAL.get(r, None)
        mult = {"EDGE": 1.3, "maybe": 1.0, "no info": 0.6, "FLIP?": 0.6}[g]
        w = None if base is None else round(min(1.0, base * mult), 2)
        W[nm] = {"label": lab, "rating": r, "grade": g, "weight": w, "best": {"luck_test": round(b[8], 2), "direction": "with" if dr > 0 else "against", "from_min": lo // 60, "to_min": hi // 60, "top_pct": round(100 * (1 - pct)), "older": round(100 * older, 1), "newer": round(100 * newer, 1)}}
        print("%-34s %-6s top %-3d%%   m%-2d-%-3d %3d/%-3d %-9s | %+5.1f  %+5.1f  | %-7s | %s -> %s" % (lab[:34], "WITH" if dr > 0 else "AGAINST", round(100 * (1 - pct)), lo // 60, hi // 60, na, nb, "", 100 * older, 100 * newer, g, r or "NOT RATED", "-" if w is None else w))
    unrated = [LABEL.get(k, k) for k, v in W.items() if v["rating"] is None]
    print("\nNOT RATED BY YOU YET (%d): %s" % (len(unrated), "; ".join(unrated)))
    print("\nWeight = your rating (high 1.0, medium-high .75, medium .5, low .25) x evidence (EDGE x1.3 only when the newer rounds clear a luck test, maybe x1, no info or FLIP? x0.6). Nothing here changes the agent yet.")
    json.dump({"made": int(time.time()), "rounds": len(opens), "signals": W}, open(os.path.join(G.os.path.dirname(G._out()), "signal_weights.json"), "w"))


if __name__ == "__main__":
    main()
