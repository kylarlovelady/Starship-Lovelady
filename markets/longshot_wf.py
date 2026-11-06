#!/usr/bin/env python3
"""READ-ONLY forward-style test of ONE hypothesis from the pricing study (queue 078): 3 to 7 minutes before the close, Kalshi's prices imply LESS
Bitcoin movement than Bitcoin actually showed (implied/realized volatility about 0.8), so the cheap far-from-the-line side ("longshot") may win more often than its price says.
Rule: at a checkpoint (seconds left), buy the CHEAP side at its ask if the ask is between 2c and a ceiling; hold to the real result; taker fee 7% x p x (1-p). Nothing else.
It reports, per rule: bets, wins, profit per $ staked, a bootstrap 90% range (resampling rounds), the older half vs the newer half of the rounds, and per calendar day (Central).
A real edge keeps its sign in both halves and on most days, and its 90% range stays above zero. 12 rules are tried, so one lucky rule is expected; look for the pattern across rules.
Run: python3 longshot_wf.py [days=5]. Output: ~/starship/memory/inbox/longshot-wf.md. Light on memory (keeps rows with 160 to 460 s left only)."""
import collections, glob, gzip, json, os, random, sys, time
D = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data"))
days = float(sys.argv[1]) if len(sys.argv) > 1 else 5
OUT = os.environ.get("OUTF", os.path.expanduser("~/starship/memory/inbox/longshot-wf.md"))
fee = lambda p: 0.07 * p * (1 - p)
def lv(x):
    try: return [(float(a), float(b)) for a, b in x]
    except Exception: return []
R = collections.defaultdict(list); N = collections.Counter(); cut = time.time() - days * 86400
for p in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
    if os.path.getmtime(p) < cut: continue
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: r = json.loads(l)
                except ValueError: continue
                left = r.get("left")
                if left is None or r.get("t") is None: continue
                ce = int(round(r["t"] + left)); N[ce] += 1
                if left < 160 or left > 460: continue
                ob = r.get("ob") or {}
                y = lv(ob.get("yes_dollars") or ob.get("yes") or []); n = lv(ob.get("no_dollars") or ob.get("no") or [])
                if not y or not n: continue
                sc = 1.0 if max(a for a, b in y + n) <= 1.0 else 100.0
                R[ce].append((float(left), max(a for a, b in y) / sc, 1 - max(a for a, b in n) / sc))
    except OSError: pass
HIST = {}
try:
    for ln in open(os.path.join(D, "history", "rounds.jsonl")):
        try: r_ = json.loads(ln); HIST[int(r_["close"])] = 1 if r_["result"] == "UP" else 0
        except Exception: pass
except OSError: pass
def result(ce):
    for d in (0, 1, -1, 2, -2):
        if (ce + d) in HIST: return HIST[ce + d]
rounds = []
for ce, seq in R.items():
    if N[ce] < 300 or result(ce) is None or len(seq) < 100: continue
    seq.sort(key=lambda s: -s[0]); rounds.append((ce, seq, result(ce)))
rounds.sort()
L = ["# Longshot hypothesis test (cheap side 3 to 7 minutes out), last %g days" % days, "", "Rounds with a full recording and a real result: **%d**." % len(rounds), ""]
if len(rounds) < 40:
    L.append("Too few rounds."); open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L)); sys.exit(0)
def bets(c, cap):
    out = []   # (round index, cost, profit)
    for i, (ce, seq, res) in enumerate(rounds):
        pick = None
        for s in seq:
            if s[0] >= c: pick = s
            else: break
        if pick is None or pick[0] - c > 15: continue
        left, yb, ya = pick; ay, an = ya, 1 - yb
        side, ask = ("Y", ay) if ay <= an else ("N", an)
        if ask < 0.02 or ask > cap: continue
        win = (res == 1) if side == "Y" else (res == 0)
        out.append((i, ask + fee(ask), (1.0 if win else 0.0) - ask - fee(ask), win, ce))
    return out
def ppd(b): 
    c = sum(x[1] for x in b); return (sum(x[2] for x in b) / c) if c else None
random.seed(7)
L += ["| seconds left | price ceiling | bets | wins | avg price | profit per $ | 90% range (bootstrap) | older half | newer half | days positive |", "|---|---|---|---|---|---|---|---|---|---|"]
detail = None
for c in (420, 300, 240, 180):
    for cap in (0.10, 0.15, 0.20):
        b = bets(c, cap)
        if len(b) < 15: L.append("| %d | %.0fc | %d | | | | | | | |" % (c, 100 * cap, len(b))); continue
        mid = len(rounds) // 2
        bo = [x for x in b if x[0] < mid]; bn = [x for x in b if x[0] >= mid]
        byround = collections.defaultdict(list)
        for x in b: byround[x[0]].append(x)
        keys = list(byround); samp = []
        for _ in range(1500):
            pick = [x for k in (random.choice(keys) for _ in keys) for x in byround[k]]
            samp.append(ppd(pick))
        samp.sort(); lo, hi = samp[int(0.05 * len(samp))], samp[int(0.95 * len(samp))]
        dd = collections.defaultdict(list)
        for x in b: dd[(x[4] - 21600) // 86400].append(x)
        pos = sum(1 for k, v in dd.items() if ppd(v) > 0)
        L.append("| %d | %.0fc | %d | %d | %.0fc | %+.0f%% | %+.0f%% to %+.0f%% | %s | %s | %d of %d |" % (c, 100 * cap, len(b), sum(1 for x in b if x[3]), 100 * sum(x[1] for x in b) / len(b),
                 100 * ppd(b), 100 * lo, 100 * hi, ("%+.0f%% (%d)" % (100 * ppd(bo), len(bo))) if bo else "-", ("%+.0f%% (%d)" % (100 * ppd(bn), len(bn))) if bn else "-", pos, len(dd)))
        if c == 300 and cap == 0.15: detail = dd
if detail:
    L += ["", "## Per day for the 300 s / 15c rule (Central calendar days)", "", "| day | bets | wins | profit per $ |", "|---|---|---|---|"]
    for k in sorted(detail):
        v = detail[k]; L.append("| %s | %d | %d | %+.0f%% |" % (time.strftime("%m-%d", time.gmtime(k * 86400)), len(v), sum(1 for x in v if x[3]), 100 * ppd(v)))
L += ["", "## Reading this", "", "- Pays about 10 to 1 when it hits, so results swing hard: a few wins decide everything. Trust only a 90% range that stays above zero AND the same sign in both halves and on most days.",
      "- Practice only; nothing changes in the agent. If it holds, the next step is a small forward test as its own practice strategy, small stakes."]
open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L))
