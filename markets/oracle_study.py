#!/usr/bin/env python3
"""READ-ONLY hindsight study: what was the best possible trade in every recorded round, and which signals (known BEFORE the trade) went with it?
Trades nothing. Uses ~/market-data/ticks-*.jsonl[.gz] (per-second recordings) and history/rounds.jsonl (real Kalshi results).
Part A  oracle: best single buy per round in hindsight (cheapest ask of the side that went on to win, after fee), and when in the round it was.
Part B  signal power: at fixed checkpoints (seconds left) every feature is measured; AUC says how well it predicts UP/DOWN on its own
        (0.50 = useless). 'vs market' = does it still help once the Kalshi price (the crowd's guess) is taken into account? Each AUC is also
        shown for the older half and the newer half of the rounds: a real signal keeps its sign in both halves.
Part C  simple edge rule: model chance from z-score vs the Kalshi ask, buy when the gap is big enough, after fee.
Run: python3 oracle_study.py [days=7]. Output: ~/starship/memory/inbox/oracle-study.md"""
import glob, gzip, json, math, os, sys, time, collections, statistics
D = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data"))
days = float(sys.argv[1]) if len(sys.argv) > 1 else 3
OUT = os.environ.get('OUTF', os.path.expanduser('~/starship/memory/inbox/oracle-study.md'))
CPS = (600, 420, 300, 180, 90, 45)
fee = lambda p: 0.07 * p * (1 - p)
Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def lv(x):
    try:
        return [(float(a), float(b)) for a, b in x]
    except Exception:
        return []


def asks_raw(r):
    ob = r.get("ob") or {}
    y = lv(ob.get("yes_dollars") or ob.get("yes") or [])
    n = lv(ob.get("no_dollars") or ob.get("no") or [])
    if not y or not n:
        return None
    sc = 1.0 if max(a for a, b in y + n) <= 1.0 else 100.0
    yb = max(a for a, b in y) / sc
    nb = max(a for a, b in n) / sc
    imb = None
    ys = sum(b for a, b in y); ns = sum(b for a, b in n)
    if ys + ns > 0:
        imb = (ys - ns) / (ys + ns)
    return 1 - nb, 1 - yb, imb


def slim(r):
    """keep only the few numbers this study needs (the raw rows are big; keeping them all can run the Pi out of memory)"""
    fl = r.get("flow") or {}; cb = r.get("cbbook") or {}; x = r.get("x") or {}; fu = r.get("funding") or {}
    return {"px": float(r["px"]), "a": asks_raw(r), "st": num((r.get("k") or {}).get("floor_strike")), "kr": num(x.get("kraken")),
            "fb": fl.get("buy_usd"), "fs": fl.get("sell_usd"), "cb": cb.get("bid_usd"), "ca": cb.get("ask_usd"), "fu": fu.get("rate")}


R = collections.defaultdict(list)
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
                k = r.get("k") or {}
                ce = int(round(r["t"] + r["left"]))
                R[ce].append((r["t"], float(r["left"]), slim(r)))
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


def asks(r):
    return r.get("a")


rounds = []
for ce, seq in R.items():
    seq.sort(key=lambda x: x[0])
    if len(seq) < 300 or seq[0][1] < 800:
        continue
    res = result(ce)
    if res is None:
        continue
    strike = None
    for t, left, r in seq:
        s = r.get("st")
        if s:
            strike = s
            break
    if strike is None:
        continue
    rounds.append((ce, seq, res, strike))
rounds.sort()
L = ["# Hindsight / oracle study (last %g days)" % days, "",
     "Rounds with a full recording, a strike and a real Kalshi result: **%d** (%d UP, %d DOWN)." % (len(rounds), sum(r[2] for r in rounds), sum(1 - r[2] for r in rounds)), ""]
if len(rounds) < 30:
    L.append("Too few rounds to say anything yet.")
    open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L)); sys.exit(0)

# ---------------- Part A: oracle ----------------
best = []
for ce, seq, res, strike in rounds:
    cheapest = None
    for t, left, r in seq:
        if left < 3:
            continue
        a = asks(r)
        if not a:
            continue
        ay, an, _ = a
        ask = ay if res == 1 else an
        if ask <= 0.01 or ask >= 0.995:
            continue
        if cheapest is None or ask < cheapest[0]:
            cheapest = (ask, left)
    if cheapest:
        best.append((cheapest[0], cheapest[1]))
L += ["## A. The perfect-hindsight buy (cheapest ask of the side that won, with 3+ s left)", "",
      "| statistic | value |", "|---|---|"]
ps = [b[0] for b in best]
profits = [1 - a - fee(a) for a in ps]
L.append("| rounds with a usable book | %d |" % len(best))
L.append("| median cheapest winning ask | %.0fc |" % (100 * statistics.median(ps)))
L.append("| average perfect-hindsight profit per contract | %.1fc (%.0f%% on cost) |" % (100 * statistics.mean(profits), 100 * sum(profits) / sum(a + fee(a) for a in ps)))
L.append("| share of rounds where the perfect buy was 30c or less | %.0f%% |" % (100.0 * sum(1 for a in ps if a <= 0.30) / len(ps)))
L.append("| share where it was 50c or less | %.0f%% |" % (100.0 * sum(1 for a in ps if a <= 0.50) / len(ps)))
tb = collections.Counter(("0-60 s" if l <= 60 else "60-180 s" if l <= 180 else "180-420 s" if l <= 420 else ">420 s") for a, l in best)
L.append("| WHEN in the round the cheapest winning ask was (seconds left) | " + ", ".join("%s: %d%%" % (k, 100 * tb[k] / len(best)) for k in ("0-60 s", "60-180 s", "180-420 s", ">420 s")) + " |")
L += ["", "Reading: the perfect buy is nearly always a *cheap* winner early in the round that you could not have known about. The rest of this report asks which signals could have pointed to it in advance.", ""]

# ---------------- Part B: signal power ----------------
FEATS = ["z (btc vs strike, in sigmas)", "dist $ (btc - strike)", "mom 10s $", "mom 30s $", "mom 60s $", "kraken - coinbase $",
         "trade flow imbalance", "coinbase book imbalance", "kalshi book imbalance", "kalshi mid (crowd)", "funding rate"]


def at(seq, cp):
    """the last recorded row with at least cp seconds left, plus its index"""
    pick = None
    for i, (t, left, r) in enumerate(seq):
        if left >= cp:
            pick = i
        else:
            break
    return pick


def px_back(seq, i, secs):
    t0 = seq[i][0] - secs
    j = i
    while j > 0 and seq[j][0] > t0:
        j -= 1
    return seq[j][2].get("px")


def feats(seq, i, strike):
    t, left, r = seq[i]
    px = float(r["px"])
    ws = []
    prev = None
    for tt, ll, rr in seq[max(0, i - 60):i + 1]:
        if prev is not None and True:
            ws.append(float(rr["px"]) - prev)
        prev = float(rr["px"])
    sig = statistics.pstdev(ws) if len(ws) > 10 else None
    f = {}
    f["dist $ (btc - strike)"] = px - strike
    f["z (btc vs strike, in sigmas)"] = (px - strike) / (max(sig, 1.0) * math.sqrt(max(left, 1))) if sig is not None else None
    for s, nm in ((10, "mom 10s $"), (30, "mom 30s $"), (60, "mom 60s $")):
        b = px_back(seq, i, s)
        f[nm] = px - float(b) if b is not None else None
    f["kraken - coinbase $"] = r["kr"] - px if r.get("kr") is not None else None
    tot = (r.get("fb") or 0) + (r.get("fs") or 0)
    f["trade flow imbalance"] = (r["fb"] - r["fs"]) / tot if tot > 0 else None
    tot = (r.get("cb") or 0) + (r.get("ca") or 0)
    f["coinbase book imbalance"] = (r["cb"] - r["ca"]) / tot if tot > 0 else None
    a = asks(r)
    f["kalshi book imbalance"] = a[2] if a else None
    f["kalshi mid (crowd)"] = (a[0] + (1 - a[1])) / 2.0 if a else None
    f["funding rate"] = r.get("fu")
    return f, a


def auc(pairs):
    """pairs = [(score, label 1/0)]; probability a random UP round scores above a random DOWN round"""
    pos = [s for s, y in pairs if y == 1]; neg = [s for s, y in pairs if y == 0]
    if len(pos) < 8 or len(neg) < 8:
        return None
    w = 0.0
    for a in pos:
        for b in neg:
            w += 1.0 if a > b else 0.5 if a == b else 0.0
    return w / (len(pos) * len(neg))


def rank(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); rk = [0.0] * len(v)
    for k, i in enumerate(o):
        rk[i] = k
    return rk


def corr(a, b):
    n = len(a)
    if n < 20:
        return None
    ma, mb = sum(a) / n, sum(b) / n
    sa = math.sqrt(sum((x - ma) ** 2 for x in a)); sb = math.sqrt(sum((x - mb) ** 2 for x in b))
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb) if sa > 0 and sb > 0 else None


half = len(rounds) // 2
L += ["## B. Which signals predict UP/DOWN? (AUC: 0.50 = coin flip, 1.00 = perfect, below 0.50 = points the other way)", "",
      "Each cell: AUC all rounds (older half / newer half). **Bold** = 0.60 or more (or 0.40 or less) AND the same side of 0.50 in both halves. 'vs market' = rank correlation of the signal with (result minus Kalshi mid), i.e. does it know something the price does not. Roughly +-0.13 is noise at this sample size.", ""]
hdr = "| signal | " + " | ".join("%ds left" % c for c in CPS) + " |"
L += [hdr, "|---|" + "---|" * len(CPS)]
store = {c: {nm: [] for nm in FEATS} for c in CPS}   # (feature, label, mid, round index, ask pair)
for idx, (ce, seq, res, strike) in enumerate(rounds):
    for c in CPS:
        i = at(seq, c)
        if i is None or seq[i][1] - c > 20:
            continue
        f, a = feats(seq, i, strike)
        for nm in FEATS:
            if f.get(nm) is not None:
                store[c][nm].append((f[nm], res, idx, f.get("kalshi mid (crowd)")))
resid_lines = []
for nm in FEATS:
    cells = []; rc = []
    for c in CPS:
        v = store[c][nm]
        pa = auc([(s, y) for s, y, ix, m in v])
        if pa is None:
            cells.append("n/a"); rc.append("n/a"); continue
        h1 = auc([(s, y) for s, y, ix, m in v if ix < half]); h2 = auc([(s, y) for s, y, ix, m in v if ix >= half])
        t = "%.2f (%s / %s)" % (pa, "%.2f" % h1 if h1 else "-", "%.2f" % h2 if h2 else "-")
        if h1 and h2 and ((pa >= 0.60 and h1 > 0.5 and h2 > 0.5) or (pa <= 0.40 and h1 < 0.5 and h2 < 0.5)):
            t = "**" + t + "**"
        cells.append(t)
        vm = [(s, y - m) for s, y, ix, m in v if m is not None]
        if len(vm) >= 20:
            cr = corr(rank([s for s, _ in vm]), rank([e for _, e in vm]))
            rc.append("%+.2f" % cr if cr is not None else "n/a")
        else:
            rc.append("n/a")
    L.append("| %s | %s |" % (nm, " | ".join(cells)))
    resid_lines.append("| %s | %s |" % (nm, " | ".join(rc)))
L += ["", "### Does it beat the market price? (rank correlation with result minus Kalshi mid)", "", hdr, "|---|" + "---|" * len(CPS)] + resid_lines + [""]

# ---------------- Part C: edge rule ----------------
L += ["## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result", ""]
L += ["| left | min gap | bets | win rate | profit per $ staked | avg cost |", "|---|---|---|---|---|---|"]
for c in CPS:
    for gap in (0.05, 0.10, 0.20):
        n = w = 0; cost = prof = 0.0
        for ce, seq, res, strike in rounds:
            i = at(seq, c)
            if i is None or seq[i][1] - c > 20:
                continue
            f, a = feats(seq, i, strike)
            z = f.get("z (btc vs strike, in sigmas)")
            if z is None or not a:
                continue
            py = Phi(z)
            ay, an, _ = a
            gy = py - ay - fee(ay); gn = (1 - py) - an - fee(an)
            side, g, ask = ("Y", gy, ay) if gy >= gn else ("N", gn, an)
            if g < gap or ask <= 0.02 or ask >= 0.995:
                continue
            won = (res == 1) if side == "Y" else (res == 0)
            n += 1; w += won; cost += ask + fee(ask); prof += (1.0 if won else 0.0) - ask - fee(ask)
        if n:
            L.append("| %ds | %.2f | %d | %.0f%% | %+.1f%% | %.2f |" % (c, gap, n, 100.0 * w / n, 100.0 * prof / cost, cost / n))
L += ["", "## How much to trust this", "",
      "- %d rounds, many signals x checkpoints: a few will look good by luck. Only a signal that stays on the same side in both halves, at several checkpoints, deserves a real test." % len(rounds),
      "- Hindsight always finds a great trade. The test that matters is walk-forward: pick the rule on older rounds, test it on newer ones, after fees.",
      "- Practice only. Nothing here changes any setting."]
open(OUT, "w").write("\n".join(L) + "\n")
print("\n".join(L))
