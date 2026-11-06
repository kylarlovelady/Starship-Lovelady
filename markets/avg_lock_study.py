#!/usr/bin/env python3
"""READ-ONLY study: can we call the winning side near the end, when the price is close to the target and swinging?
Kalshi settles YES if the AVERAGE of the 60 per-second index values in the last minute is at least the target (strike). With `left` seconds to go, (60-left) of those 60 values are ALREADY KNOWN,
so the question is only: will the average of the remaining `left` values beat the number R that makes the full average reach the target? We model the remaining seconds as a random walk
(vol from the last 120 s of 1-second moves), get P(YES) exactly for that, compare with Kalshi's ask (price + 7% x p x (1-p) fee) and replay the bets against the REAL settled results.
Index used: Coinbase per-second price from the recordings (Kalshi uses the BRTI composite, so a few dollars of difference are possible: noted, not corrected).
Run: python3 avg_lock_study.py [days=5]. Output also in ~/starship/memory/inbox/avg-lock-study.md"""
import glob, gzip, json, math, os, sys, time, collections, statistics
D = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data")); days = float(sys.argv[1]) if len(sys.argv) > 1 else 5
OUT = os.path.expanduser("~/starship/memory/inbox/avg-lock-study.md")
def lv(x):
    try: return [(float(a), float(b)) for a, b in x]
    except Exception: return []
def Phi(z): return 0.5 * (1 + math.erf(z / math.sqrt(2)))
R = collections.defaultdict(dict); cut = time.time() - days * 86400
for p in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
    if os.path.getmtime(p) < cut: continue
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: r = json.loads(l)
                except ValueError: continue
                px = r.get("px"); left = r.get("left"); k = r.get("k") or {}
                if px is None or left is None: continue
                ob = r.get("ob") or {}
                y = lv(ob.get("yes_dollars") or ob.get("yes") or []); n = lv(ob.get("no_dollars") or ob.get("no") or [])
                sc = 1.0 if (y or n) and max(a for a, b in y + n) <= 1.0 else 100.0
                yb = max((a for a, b in y), default=None); nb = max((a for a, b in n), default=None)
                tk = int(round(r["t"] + left))
                R[tk][int(round(r["t"]))] = (float(px), float(k["floor_strike"]) if k.get("floor_strike") is not None else None,
                                             yb / sc if yb is not None else None, nb / sc if nb is not None else None)
    except OSError: pass
HIST = {}
try:
    for ln in open(os.path.join(D, "history", "rounds.jsonl")):
        try: r_ = json.loads(ln); HIST[int(r_["close"])] = 1 if r_["result"] == "UP" else 0
        except Exception: pass
except OSError: pass
def res(tk):
    for d in (0, 1, -1, 2, -2):
        if (tk + d) in HIST: return HIST[tk + d]
fee = lambda p: 0.07 * p * (1 - p)
rows = collections.defaultdict(list)     # left -> list of (edge, won, cost, near)
nr = 0
for tk, ticks in R.items():
    out = res(tk)
    if out is None or len(ticks) < 600: continue
    strikes = [v[1] for v in ticks.values() if v[1] is not None]
    if not strikes: continue
    strike = statistics.median(strikes); nr += 1
    for left in (10, 20, 30, 45):
        tnow = tk - left
        known = [ticks[t][0] for t in range(tk - 60, tnow + 1) if t in ticks]      # values from the last minute that already happened
        if len(known) < (60 - left) * 0.8: continue
        known_sum = sum(known) / len(known) * (60 - left)                           # fill small gaps with the mean
        hist = [ticks[t][0] for t in range(tnow - 120, tnow + 1) if t in ticks]
        if len(hist) < 60: continue
        d = [hist[i + 1] - hist[i] for i in range(len(hist) - 1)]
        sd1 = max(statistics.pstdev(d), 0.5)
        cur = ticks.get(tnow) or ticks.get(tnow - 1)
        if not cur or cur[2] is None or cur[3] is None: continue
        p0 = cur[0]; Rr = (60 * strike - known_sum) / left
        sdM = sd1 * math.sqrt(left * (left + 1) * (2 * left + 1) / 6.0) / left
        pyes = 1 - Phi((Rr - p0) / sdM)
        ask_y, ask_n = 1 - cur[3], 1 - cur[2]
        eY = pyes - ask_y - fee(ask_y); eN = (1 - pyes) - ask_n - fee(ask_n)
        side, e, ask = ("Y", eY, ask_y) if eY >= eN else ("N", eN, ask_n)
        won = (out == 1) if side == "Y" else (out == 0)
        near = abs(Rr - p0) / sdM < 1.0
        rows[left].append((e, won, ask + fee(ask), near, max(pyes, 1 - pyes), ask))
L = ["# Average-lock study (can we call the winning side late?)", "", "Rounds with real results and full recordings: %d. Model: the last-minute average is partly known; remaining seconds = random walk (recent 1 s vol). Edge = model P - Kalshi ask - fee." % nr, ""]
for left in (10, 20, 30, 45):
    L += ["## %d seconds left" % left, "", "| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |", "|---|---|---|---|---|---|---|"]
    for name, sel in (("any edge > 3c", lambda r: r[0] > 0.03), ("edge > 8c", lambda r: r[0] > 0.08), ("edge > 3c AND near target (within 1 sd)", lambda r: r[0] > 0.03 and r[3]),
                      ("always bet model favourite", lambda r: True), ("near target only, always bet model favourite", lambda r: r[3])):
        s = [r for r in rows[left] if sel(r)]
        if not s: L.append("| %s | 0 | | | | | |" % name); continue
        cost = sum(r[2] for r in s); prof = sum((1.0 if r[1] else 0.0) - r[2] for r in s)
        L.append("| %s | %d | %.1f%% | %.3f | %+.1f%% | %.2f | %.2f |" % (name, len(s), 100.0 * sum(1 for r in s if r[1]) / len(s), cost / len(s), 100.0 * prof / cost, statistics.mean(r[4] for r in s), statistics.mean(r[5] for r in s)))
    L.append("")
L.append("Calibration check (does the model's P match reality?): bucket by model P of the favourite")
for left in (20,):
    b = collections.defaultdict(lambda: [0, 0])
    for r in rows[left]:
        k = int(r[4] * 20) / 20.0; b[k][0] += 1; b[k][1] += 1 if r[1] else 0   # r[1] is won for the EDGE side; use for the favourite only when same side: approximate
    L.append("(left=20) " + "; ".join("P~%.2f: %d rounds, %.0f%% won" % (k, v[0], 100.0 * v[1] / v[0]) for k, v in sorted(b.items())))
open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L)); print("... wrote", OUT)
