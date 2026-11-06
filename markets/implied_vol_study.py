#!/usr/bin/env python3
"""READ-ONLY study: reverse-engineer how Kalshi's 15-minute BTC prices behave, from our own per-second recordings. Trades nothing.
Kalshi's contract is a digital option: YES pays $1 if the average of the last 60 index prices is above the strike. A fair price therefore
looks like Phi(distance / (sigma * sqrt(seconds left))). Market makers quote around that. This study asks:
 A. What volatility (sigma, dollars per sqrt-second) is the market PRICE implying at each time-left, and how does it compare with the
    volatility Bitcoin actually showed (trailing 60 s)? Implied above realized = the market is expensive on the near-the-line side; below = cheap.
 B. Calibration: when the price said p, how often did YES really win (one sample per round per checkpoint, no overlap), and what did buying the
    cheaper/dearer side earn after the fee? (favourite-longshot bias test)
 C. How wide are the quotes (ask minus bid) by time left and by distance from the strike (what market makers charge).
Run: python3 implied_vol_study.py [days=4]. Output: ~/starship/memory/inbox/implied-vol-study.md. Light on memory: keeps (t, left, px, yes bid, yes ask) tuples only."""
import collections, glob, gzip, json, math, os, statistics, sys, time
from statistics import NormalDist
N = NormalDist()
D = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data"))
days = float(sys.argv[1]) if len(sys.argv) > 1 else 4
OUT = os.environ.get("OUTF", os.path.expanduser("~/starship/memory/inbox/implied-vol-study.md"))
fee = lambda p: 0.07 * p * (1 - p)


def lv(x):
    try:
        return [(float(a), float(b)) for a, b in x]
    except Exception:
        return []


R = collections.defaultdict(list)     # close epoch -> [(t, left, px, yes_bid, yes_ask)]
STRIKE = {}
cut = time.time() - days * 86400
for p in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
    if os.path.getmtime(p) < cut:
        continue
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try:
                    r = json.loads(l)
                except ValueError:
                    continue
                if r.get("left") is None or r.get("t") is None or r.get("px") is None:
                    continue
                ob = r.get("ob") or {}
                y = lv(ob.get("yes_dollars") or ob.get("yes") or [])
                n = lv(ob.get("no_dollars") or ob.get("no") or [])
                if not y or not n:
                    continue
                sc = 1.0 if max(a for a, b in y + n) <= 1.0 else 100.0
                yb = max(a for a, b in y) / sc
                ya = 1 - max(a for a, b in n) / sc
                ce = int(round(r["t"] + r["left"]))
                R[ce].append((r["t"], float(r["left"]), float(r["px"]), yb, ya))
                if ce not in STRIKE:
                    try:
                        STRIKE[ce] = float((r.get("k") or {}).get("floor_strike"))
                    except (TypeError, ValueError):
                        pass
    except OSError:
        pass

HIST = {}
try:
    for ln in open(os.path.join(D, "history", "rounds.jsonl")):
        try:
            r_ = json.loads(ln)
            HIST[int(r_["close"])] = 1 if r_["result"] == "UP" else 0
        except Exception:
            pass
except OSError:
    pass


def result(ce):
    for d in (0, 1, -1, 2, -2):
        if (ce + d) in HIST:
            return HIST[ce + d]
    return None


rounds = []
for ce, seq in R.items():
    seq.sort()
    if len(seq) < 300 or seq[0][1] < 800 or ce not in STRIKE:
        continue
    rounds.append((ce, seq, result(ce), STRIKE[ce]))
rounds.sort()
L = ["# Kalshi pricing study (implied volatility, calibration, spreads), last %g days" % days, "",
     "Rounds with a full recording and a strike: **%d** (%d with a real result)." % (len(rounds), sum(1 for r in rounds if r[2] is not None)), "",
     "Settlement = average of the last 60 index prices vs the strike (CF Benchmarks), so inside the last minute part of the answer is already locked in. Sigma below is in dollars per square-root-second.", ""]
if len(rounds) < 30:
    L.append("Too few rounds.")
    open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L)); sys.exit(0)

TB = [(600, 840), (420, 600), (300, 420), (180, 300), (90, 180), (45, 90), (15, 45)]
imp = {b: [] for b in TB}; rea = {b: [] for b in TB}; ratio = {b: [] for b in TB}
spr = {b: [] for b in TB}; sprd = collections.defaultdict(list)
for ce, seq, res, strike in rounds:
    for i in range(60, len(seq)):
        t, left, px, yb, ya = seq[i]
        b = next((b for b in TB if b[0] <= left < b[1]), None)
        if b is None or i % 5:           # every 5th second is plenty
            continue
        mid = (yb + ya) / 2.0
        spr[b].append(ya - yb)
        d = px - strike
        if 0.1 < mid < 0.9 and abs(d) > 1.0:
            # distance bucket for spreads
            sprd[min(int(abs(d) / 25), 8)].append(ya - yb)
        if not (0.05 < mid < 0.95) or abs(d) < 1.0:
            continue
        z = N.inv_cdf(mid)
        if z == 0 or (z > 0) != (d > 0):
            continue
        si = d / (z * math.sqrt(left))
        ch = [seq[j][2] - seq[j - 1][2] for j in range(i - 59, i + 1)]
        sr = statistics.pstdev(ch)
        if sr <= 0.5:
            continue
        imp[b].append(si); rea[b].append(sr); ratio[b].append(si / sr)
L += ["## A. Implied vs realized volatility (only seconds where the price is between 5c and 95c and BTC is at least $1 from the strike)", "",
      "| seconds left | samples | median implied sigma | median realized sigma (trailing 60 s) | median ratio implied/realized |", "|---|---|---|---|---|"]
for b in TB:
    if len(ratio[b]) >= 20:
        L.append("| %d-%d | %d | %.2f | %.2f | %.2f |" % (b[0], b[1], len(ratio[b]), statistics.median(imp[b]), statistics.median(rea[b]), statistics.median(ratio[b])))
L += ["", "Ratio near 1.0 = the market prices with the volatility Bitcoin is actually showing. Above 1 = the market assumes MORE movement than recent (cheaper favourite). Below 1 = it assumes less movement (dearer favourite). A ratio that changes a lot with time left shows how makers adjust near the close.", ""]

# ---------------- B calibration ----------------
CPS = (420, 300, 180, 90, 45)
L += ["## B. Calibration: price said p (YES mid), how often did YES win? (one sample per round per checkpoint)", "",
      "| left | YES mid bucket | rounds | YES won | avg mid | gap (won - mid) | profit per $ buying the CHEAPER side at its ask | profit per $ buying the DEARER side at its ask |", "|---|---|---|---|---|---|---|---|"]
for c in CPS:
    bk = collections.defaultdict(list)
    for ce, seq, res, strike in rounds:
        if res is None:
            continue
        pick = None
        for s in seq:
            if s[1] >= c:
                pick = s
            else:
                break
        if pick is None or pick[1] - c > 20:
            continue
        t, left, px, yb, ya = pick
        mid = (yb + ya) / 2.0
        k = min(int(mid * 5), 4)           # 5 buckets of 20c
        bk[k].append((mid, res, yb, ya))
    for k in sorted(bk):
        v = bk[k]
        if len(v) < 8:
            continue
        won = sum(x[1] for x in v); am = sum(x[0] for x in v) / len(v)
        cheap = dear = 0.0; cc = dc = 0.0
        for mid, res, yb, ya in v:
            ay, an = ya, 1 - yb               # asks for YES / NO
            for side_cheap in (True, False):
                if (ay <= an) == side_cheap:
                    ask, w = ay, res
                else:
                    ask, w = an, 1 - res
                if ask <= 0.01 or ask >= 0.995:
                    continue
                pf = (1.0 if w else 0.0) - ask - fee(ask)
                if side_cheap:
                    cheap += pf; cc += ask + fee(ask)
                else:
                    dear += pf; dc += ask + fee(ask)
        L.append("| %ds | %d-%dc | %d | %.0f%% | %.0fc | %+.0fc | %s | %s |" % (c, k * 20, k * 20 + 20, len(v), 100.0 * won / len(v), 100 * am, 100 * (won / len(v) - am),
                 ("%+.1f%%" % (100 * cheap / cc)) if cc else "n/a", ("%+.1f%%" % (100 * dear / dc)) if dc else "n/a"))
L.append("")

# ---------------- C spreads ----------------
L += ["## C. What the quotes cost (ask minus bid, in cents)", "", "| seconds left | samples | median spread | 90th percentile |", "|---|---|---|---|"]
for b in TB:
    v = spr[b]
    if len(v) >= 20:
        v = sorted(v)
        L.append("| %d-%d | %d | %.1fc | %.1fc |" % (b[0], b[1], len(v), 100 * statistics.median(v), 100 * v[int(0.9 * len(v))]))
L += ["", "| BTC distance from strike | samples | median spread |", "|---|---|---|"]
for k in sorted(sprd):
    v = sprd[k]
    if len(v) >= 20:
        L.append("| $%d-%d | %d | %.1fc |" % (k * 25, k * 25 + 25, len(v), 100 * statistics.median(v)))
L += ["", "## Reading this", "",
      "- Practice only; nothing here changes a setting. About 300 rounds: gaps under a few cents per bucket are noise.",
      "- Look for a bias that repeats across time-left checkpoints and price buckets, and then test it forward on new rounds."]
open(OUT, "w").write("\n".join(L) + "\n")
print("\n".join(L))
