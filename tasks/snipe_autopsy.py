#!/usr/bin/env python3
"""Loss autopsy for the $1K-Snipe practice test (strategy key v_snipe_all) and the $25 v_snipe. Writes memory/inbox/snipe-autopsy.md (numbers only, no secrets).
For every finished round: what it bought (side, contracts, price, seconds left), what the book offered, how it ended; for LOSSES a second-by-second timeline around the buy
(BTC price, target, running 60 s average, bids, Kalshi market status) and a plain-English guess of what would have prevented it."""
import glob, gzip, json, os, time, collections
HOME = os.path.expanduser("~"); D = HOME + "/market-data"; OUT = HOME + "/starship/memory/inbox/snipe-autopsy.md"
STRATS = ("v_snipe_all", "v_snipe")
def jl(p):
    try:
        for l in open(p):
            try: yield json.loads(l)
            except ValueError: pass
    except OSError: return
wins = [w for w in jl(D + "/sim_windows.jsonl") if w.get("strat") in STRATS]
trades = [t for t in jl(D + "/trades.jsonl") if t.get("s") in STRATS]
L = ["# $1K-Snipe and v_snipe autopsy (auto, refreshed every ~5 min)", ""]
for s in STRATS:
    ws = [w for w in wins if w["strat"] == s]; n = len(ws); w_ = [w for w in ws if w["pnl"] > 0]; l_ = [w for w in ws if w["pnl"] < 0]
    tot = sum(w["pnl"] for w in ws); stk = sum(w.get("staked", 0) for w in ws)
    L.append("- **%s**: %d rounds with a result, %d won, %d lost, %d no bet; profit $%.2f on $%.2f staked%s" % (s, n, len(w_), len(l_), n - len(w_) - len(l_), tot, stk, (" (%+.1f%% per $)" % (100 * tot / stk)) if stk else ""))
L.append("")
losses = [w for w in wins if w["pnl"] < 0][-12:]
by_round = collections.defaultdict(list)
for t in trades:
    if t.get("a") == "BUY": by_round[(t["s"], int(t["t"]) // 900)].append(t)
need = set()
for w in losses:
    for t in by_round.get((w["strat"], int(w["t"]) // 900), []): need.add(int(t["t"]))
ticks = {}
if need:
    lo, hi = min(need) - 50, max(need) + 80
    for p in sorted(glob.glob(D + "/ticks-*.jsonl*")):
        if os.path.getmtime(p) < lo - 3600: continue
        op = gzip.open if p.endswith(".gz") else open
        try:
            with op(p, "rt") as f:
                for l in f:
                    try: r = json.loads(l)
                    except ValueError: continue
                    if lo <= r.get("t", 0) <= hi: ticks[int(r["t"])] = r
        except OSError: pass
L.append("## Recent losses, with timeline")
if not losses: L.append("(no losing round yet)")
for w in reversed(losses):
    bs = by_round.get((w["strat"], int(w["t"]) // 900), [])
    L += ["", "### %s round %s: lost $%.2f (staked $%.2f), result %s" % (w["strat"], time.strftime("%H:%M", time.localtime(w["t"])), -w["pnl"], w.get("staked", 0), w.get("outcome"))]
    if not bs: L.append("- no buy record found"); continue
    for b in bs: L.append("- bought %s x%s at %s (ask %s, bid %s) at %s: %s" % (b.get("side"), b.get("c"), b.get("px"), b.get("ask"), b.get("bid"), time.strftime("%H:%M:%S", time.localtime(b["t"])), (b.get("why") or "")[:120]))
    t0 = int(bs[0]["t"]); close = None
    for t in range(t0 - 3, t0 + 70):
        r = ticks.get(t)
        if r and r.get("left") is not None: close = int(r["t"] + r["left"]); break
    if close is None: L.append("- (no tick recording for this round yet)"); continue
    strike = None; run = []
    L.append("")
    L.append("| sec left | BTC | target | gap | avg so far (last 60 s) | YES bid | NO bid | market status |")
    L.append("|---|---|---|---|---|---|---|---|")
    for t in range(close - 60, close + 6):
        r = ticks.get(t)
        if not r: continue
        k = r.get("k") or {}; strike = k.get("floor_strike", strike); px = r.get("px")
        if px is not None and t <= close: run.append(px)
        ob = r.get("ob") or {}
        def best(x):
            try: return max(float(a[0]) for a in x)
            except Exception: return None
        yb = best(ob.get("yes_dollars") or ob.get("yes") or []); nb = best(ob.get("no_dollars") or ob.get("no") or [])
        ks = (r.get("ks") or {}).get("cur", {}).get("status") or ""
        if (close - t) % 5 == 0 or abs(t - t0) <= 1:
            L.append("| %d | %s | %s | %s | %s | %s | %s | %s%s |" % (close - t, ("%.0f" % px) if px else "", ("%.0f" % strike) if strike else "", ("%+.0f" % (px - strike)) if (px and strike) else "", ("%.0f" % (sum(run) / len(run))) if run else "", yb, nb, ks, " <-- BUY" if t == t0 else ""))
    # plain-English guess
    try:
        b0 = bs[0]; late = close - t0
        gap_at_buy = (ticks[t0]["px"] - strike) if (ticks.get(t0) and strike) else None
        last = [ticks[t]["px"] for t in range(close - 10, close) if t in ticks]
        end_gap = (sum(last) / len(last) - strike) if last and strike else None
        g = []
        if late > 25: g.append("it bought %d s before the close: too early, the last seconds still decided it" % late)
        if gap_at_buy is not None and abs(gap_at_buy) < 15: g.append("BTC was only $%.0f from the target when it bought: a toss-up; skip rounds closer than about $%.0f" % (abs(gap_at_buy), max(15, abs(gap_at_buy) * 2)))
        if gap_at_buy is not None and end_gap is not None and (gap_at_buy > 0) != (end_gap > 0): g.append("BTC crossed the target after the buy (gap %+.0f at buy, about %+.0f in the final 10 s)" % (gap_at_buy, end_gap))
        if b0.get("px") and float(b0["px"]) > 0.95: g.append("paid %.0fc: one miss costs about %d wins" % (float(b0["px"]) * 100, round(float(b0["px"]) / (1 - float(b0["px"])))))
        L.append("")
        L.append("**What would have prevented it:** " + ("; ".join(g) if g else "nothing obvious from this timeline; look at the numbers above"))
    except Exception as e:
        L.append("(guess failed: %s)" % e)
open(OUT, "w").write("\n".join(L) + "\n")
print("autopsy written,", len(wins), "rounds,", len(losses), "recent losses")
