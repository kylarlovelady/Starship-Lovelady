#!/usr/bin/env python3
"""READ-ONLY study for the SNIPING idea (buy the favourite at the very end of a round). Uses the agent's per-second recordings (~/market-data/ticks-*.jsonl[.gz]); trades nothing.
Part 1: WHEN does a round really stop? For every recorded round: seconds left on the clock at the LAST recorded second (the recorder only sees OPEN markets, so left>3 = the market stopped being open early), and how far the price was.
Part 2: for buffers B = last tick with at least B seconds left, buy 1 contract of the favourite at the ask if ask <= 99c, hold to the result. Win rate vs price paid (after the 7% x p x (1-p) fee), by price bucket, and the dollars the book offered at that ask (can $1,000 fill?).
Run: python3 snipe_study.py [days=5]. Output also written to ~/starship/memory/inbox/snipe-study.md"""
import glob, gzip, json, os, sys, time, collections, statistics
D = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data")); days = float(sys.argv[1]) if len(sys.argv) > 1 else 5
OUT = os.path.expanduser("~/starship/memory/inbox/snipe-study.md")
def lv(x):
    try: return [(float(a), float(b)) for a, b in x]
    except Exception: return []
def rows(p):
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: r = json.loads(l)
                except ValueError: continue
                if r.get("left") is None or r.get("t") is None: continue
                ob = r.get("ob") or {}
                y = lv(ob.get("yes_dollars") or ob.get("yes") or []); n = lv(ob.get("no_dollars") or ob.get("no") or [])
                if not y or not n: continue
                sc = 1.0 if max(a for a, b in y + n) <= 1.0 else 100.0
                yield int(round(r["t"] + r["left"])), r["t"], float(r["left"]), [(a / sc, b) for a, b in y], [(a / sc, b) for a, b in n]
    except OSError: return
R = collections.defaultdict(list); cut = time.time() - days * 86400
for p in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
    if os.path.getmtime(p) < cut: continue
    for tk, t, left, y, n in rows(p): R[tk].append((left, y, n))
fee = lambda p: 0.07 * p * (1 - p)
L = ["# Sniping study (recorded per-second data, last %g days)" % days, ""]
full = {}; lasts = []
for tk, seq in R.items():
    seq.sort(key=lambda x: -x[0])
    if len(seq) < 300 or seq[0][0] < 800: continue
    full[tk] = seq; lasts.append(seq[-1][0])
L.append("Rounds with a full recording: %d" % len(full))
L.append("")
if lasts:
    bk = collections.Counter(("0-2 s" if v <= 2 else "2-5 s" if v <= 5 else "5-10 s" if v <= 10 else "10-30 s" if v <= 30 else "30-120 s" if v <= 120 else ">120 s") for v in lasts)
    L += ["", "## Part 1: seconds left on the clock at the LAST second the market was still open", "", "| left at last recorded second | rounds | share |", "|---|---|---|"]
    for k in ("0-2 s", "2-5 s", "5-10 s", "10-30 s", "30-120 s", ">120 s"): L.append("| %s | %d | %.0f%% |" % (k, bk[k], 100.0 * bk[k] / len(lasts)))
    L.append("")
    L.append("Median seconds left at last open second: %.1f (a high number means Kalshi stopped quoting before the clock ran out, or our recorder missed the last seconds)." % statistics.median(lasts))
    early = [(tk, seq[-1]) for tk, seq in full.items() if seq[-1][0] > 10]
    ex = []
    for tk, (left, y, n) in early[:12]:
        yb = max(a for a, b in y); nb = max(a for a, b in n); ex.append("left %ds, YES bid %.2f / NO bid %.2f" % (left, yb, nb))
    L += ["", "Examples of rounds that stopped with more than 10 s left: " + ("; ".join(ex) if ex else "none")]
HIST = {}
try:
    for ln in open(os.path.join(D, "history", "rounds.jsonl")):
        try: r_ = json.loads(ln); HIST[int(r_["close"])] = 1 if r_["result"] == "UP" else 0
        except Exception: pass
except OSError: pass
def result(seq, tk=None):
    """The REAL settled result from Kalshi's history (never guessed from the last quote, which would make the test circular)."""
    for d in (0, 1, -1, 2, -2):
        if tk is not None and (tk + d) in HIST: return HIST[tk + d]
    return None
L += ["", "Rounds with a real settled result in history: %d of %d" % (sum(1 for tk in full if any((tk + d) in HIST for d in (0, 1, -1, 2, -2))), len(full)), "", "## Part 2: buy the favourite at the last tick that still had at least B seconds left, hold to the result", ""]
for B in (3, 5, 10, 20, 40, 60):
    buck = collections.defaultdict(lambda: [0, 0, 0.0, 0.0, []])   # n, wins, cost per contract sum, profit sum, depth dollars
    for tk, seq in full.items():
        res = result(seq, tk)
        if res is None: continue
        cand = [s for s in seq if s[0] >= B]
        if not cand: continue
        left, y, n = cand[-1]
        yb = max(a for a, b in y); nb = max(a for a, b in n)
        ay = 1 - nb; an = 1 - yb                         # ask to buy YES / NO
        side, ask = ("Y", ay) if ay <= an else ("N", an)  # favourite = cheaper-to-complete? use higher probability side
        side, ask = ("Y", ay) if yb >= nb else ("N", an)
        if ask > 0.995 or ask <= 0.5: continue
        book = n if side == "Y" else y                    # hitting the opposite side's bids
        top = max(book, key=lambda x: x[0]); depth = top[1] * ask
        won = (res == 1) if side == "Y" else (res == 0)
        k = "%02d-%02dc" % (int(ask * 100) // 5 * 5, int(ask * 100) // 5 * 5 + 4)
        b = buck[k]; b[0] += 1; b[1] += 1 if won else 0; b[2] += ask + fee(ask); b[3] += (1.0 if won else 0.0) - ask - fee(ask); b[4].append(depth)
    L += ["### B = %d s left" % B, "", "| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |", "|---|---|---|---|---|---|"]
    tot = [0, 0.0, 0.0]
    for k in sorted(buck):
        n_, w_, c_, p_, d_ = buck[k]; L.append("| %s | %d | %.1f%% | %.3f | %+.1f%% | $%.0f |" % (k, n_, 100.0 * w_ / n_, c_ / n_, 100.0 * p_ / c_, statistics.median(d_)))
        tot[0] += n_; tot[1] += p_; tot[2] += c_
    if tot[0]: L.append("| ALL | %d | | | %+.1f%% | |" % (tot[0], 100.0 * tot[1] / tot[2]))
    L.append("")
open(OUT, "w").write("\n".join(L) + "\n")
print("\n".join(L[:60]))
print("... wrote", OUT)
