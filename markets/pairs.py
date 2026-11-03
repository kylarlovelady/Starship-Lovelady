"""LEAN x TRIGGER test (read-only). Your way of trading: a slow trend says which way the market leans (the lean), and a fast signal says when to act (the trigger).
For every lean (4h, 24h, 7d, 1h trend) and trigger (Bitcoin speed 1 and 3 min, distance from target): buy WITH the trigger only when it AGREES with the lean, or only when it DISAGREES,
or buy AGAINST it in those cases. Chosen on older rounds, checked on newer ones. Real prices, fees in, one buy per round.
Many combinations are tried, so only a luck test of t >= 3 counts. Usage: python3 pairs.py [days=14]   (uses minute data: all downloaded rounds)"""
import sys, time, json, itertools
import signals as G, replay, hypothesis
from signals import avg
from grades import tstat


def run(rows, trig, lean, tthr, lthr, lo, hi, agree, dr):
    from hypothesis import fee
    seen, L = set(), []
    for d in rows:
        if d["open"] in seen or not (lo <= d["el"] < hi): continue
        a, b = d["S"].get(trig), d["S"].get(lean)
        if a is None or b is None or abs(a) < tthr or abs(b) < lthr: continue
        if (a > 0) != (b > 0) if agree else (a > 0) == (b > 0): continue
        side = "UP" if (a > 0) == (dr > 0) else "DOWN"
        px = d["ask"] if side == "UP" else 1 - d["bid"]
        if not .05 <= px <= .95: continue
        won = (d["res"] == "UP") == (side == "UP")
        seen.add(d["open"]); L.append({"hold": (1.0 if won else 0.0) - px - fee(px), "exit": None, "px": px, "won": won})
    return L


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    use, cand, ts_, vs_ = hypothesis.load(days)
    btc = replay.Series(ts_, vs_)
    G.STEP = 60
    _q = G.qat; G.qat = lambda r, t_, t, maxage=90: _q(r, t_, t, 90)
    rows = G.build(use, cand, btc, None)
    opens = sorted({d["open"] for d in rows}); cut = opens[int(len(opens) * 0.6)]
    tr = [d for d in rows if d["open"] < cut]; te = [d for d in rows if d["open"] >= cut]
    TR, LE = ("bmom60", "bmom180", "z"), ("tr4h", "tr24h", "tr7d", "hr")
    res, tried = [], 0
    for trig, lean in itertools.product(TR, LE):
        tv = sorted(abs(d["S"][trig]) for d in tr if d["S"].get(trig)); lv = sorted(abs(d["S"][lean]) for d in tr if d["S"].get(lean))
        if len(tv) < 200 or len(lv) < 200: continue
        for tp, lp, (lo, hi), agree, dr in itertools.product((0.6, 0.85), (0.5,), ((G.FIRST, 360), (360, G.LAST + 1)), (True, False), (1, -1)):
            tthr, lthr = tv[int(len(tv) * tp)], lv[int(len(lv) * lp)]
            A = run(tr, trig, lean, tthr, lthr, lo, hi, agree, dr)
            if len(A) < 40: continue
            B = run(te, trig, lean, tthr, lthr, lo, hi, agree, dr)
            if len(B) < 20: continue
            tried += 1
            res.append((avg(B), avg(A), len(A), len(B), tstat(B), trig, lean, tp, lo, hi, agree, dr))
    print("%d rounds (%d older / %d newer), %d lean x trigger combinations tried. Cents per contract after fees, held to the end.\n" % (len(opens), len({d['open'] for d in tr}), len({d['open'] for d in te}), tried))
    NM = {"bmom60": "BTC speed 1m", "bmom180": "BTC speed 3m", "z": "distance", "tr4h": "4h trend", "tr24h": "24h trend", "tr7d": "7d trend", "hr": "1h trend"}
    print("trigger        lean       when    bet               | older  newer  n       luck test")
    both = [r for r in res if r[0] > 0 and r[1] > 0]
    both.sort(key=lambda r: -r[4])
    for r in both[:10]:
        nw, ol, na, nb, t, trig, lean, tp, lo, hi, agree, dr = r
        print("%-14s %-10s m%d-%-3d  %s the trigger, only when it %s the lean | %+5.1f %+5.1f  %3d/%-3d  t=%.1f" % (NM[trig], NM[lean], lo // 60, hi // 60, "WITH" if dr > 0 else "AGAINST", "agrees with" if agree else "disagrees with", 100 * ol, 100 * nw, na, nb, t))
    if not both: print("  none positive in both halves")
    print("\nbest luck test of anything tried: t=%.1f. With %d combinations tried, roughly %d would reach t>=2 by luck alone and about %.1f would reach t>=3." % (max([r[4] for r in res] or [0]), tried, round(tried * 0.023), tried * 0.00135))
    print("Only a result with t>=3 that ALSO keeps working on new rounds is worth building on.")
    json.dump({"made": int(time.time()), "tried": tried, "top": [{"trig": r[5], "lean": r[6], "agree": r[10], "dir": r[11], "older": r[1], "newer": r[0], "t": r[4]} for r in both[:10]]}, open(G._out().replace("signals.json", "pairs.json"), "w"))


if __name__ == "__main__":
    main()
