#!/usr/bin/env python3
"""READ-ONLY study: does posting a resting buy (maker) instead of paying the ask (taker) cut the cost of getting in, once you count the orders that never fill?
Uses the agent's own per-second Kalshi recordings (~/market-data/ticks-*.jsonl[.gz]). It does not trade, does not touch the agent, needs no prediction:
for every recorded round and for BOTH sides (so no strategy luck), at 1, 2 and 3 minutes in:
  TAKER: buy 1 contract at the ask, hold to the end.                   fee = 7% x p x (1-p)  (Kalshi taker)
  MAKER: post a buy 1 cent above the bid, wait up to 2 minutes; it fills only if the ask falls to our price; hold to the end.   fee ASSUMED 1.75% x p x (1-p) (and shown with 0 fee too)
Prints cost per contract, win rate of filled vs all (adverse selection), and profit per $ staked. Run: python3 maker_study.py [days=3]"""
import glob, gzip, json, math, os, sys, time, collections
D = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data"))
days = float(sys.argv[1]) if len(sys.argv) > 1 else 3
def rows(p):
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: r = json.loads(l)
                except ValueError: continue
                ob = r.get("ob") or {}                       # the live order book is the trusted source (as in evidence.py)
                yl, nl = ob.get("yes_dollars") or ob.get("yes"), ob.get("no_dollars") or ob.get("no")
                if not yl or not nl or r.get("left") is None or r.get("t") is None: continue
                try:
                    yb = max(float(x[0]) for x in yl); nb = max(float(x[0]) for x in nl)
                except (TypeError, ValueError, IndexError): continue
                yb = yb if yb <= 1.0 else yb / 100.0; nb = nb if nb <= 1.0 else nb / 100.0
                yield int(r["t"] + r["left"]), r["t"], r["left"], yb, 1.0 - nb
    except OSError: return
rounds = collections.defaultdict(list)
cut = time.time() - days * 86400
for p in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
    if os.path.getmtime(p) < cut: continue
    for tk, t, left, b, a in rows(p): rounds[tk].append((left, b, a))
fee = lambda p, r: r * p * (1 - p)
agg = collections.defaultdict(lambda: collections.defaultdict(float))
n_rounds = 0
for tk, seq in rounds.items():
    seq.sort(key=lambda x: -x[0])                      # by time remaining, newest last
    if len(seq) < 600 or seq[0][0] < 800: continue     # need most of the 15 minutes
    last = seq[-1]
    if last[0] > 40: continue
    up = 1 if last[1] >= 0.85 else 0 if last[2] <= 0.15 else None   # result from the final quote
    if up is None: continue
    n_rounds += 1
    for t0 in (840, 780, 720):                         # about 1, 2, 3 minutes in
        i0 = next((i for i, (l, b, a) in enumerate(seq) if l <= t0), None)
        if i0 is None: continue
        l0, b0, a0 = seq[i0]
        for side in ("UP", "DOWN"):
            win = 1 if (side == "UP") == bool(up) else 0
            ask = a0 if side == "UP" else 1 - b0; bid = b0 if side == "UP" else 1 - a0
            if not (0.10 <= ask <= 0.90): continue
            g = agg[t0]
            g["n"] += 1
            tk_pay = win - ask - fee(ask, 0.07); g["taker_ev"] += tk_pay; g["taker_cost"] += ask + fee(ask, 0.07)
            lim = round(bid + 0.01, 2) if ask - bid >= 0.02 else bid
            filled = None
            for (l, b, a) in seq[i0 + 1:]:
                if l < t0 - 120 or l < 60: break
                ask_now = a if side == "UP" else 1 - b
                if ask_now <= lim + 1e-9: filled = lim; break
            if filled is None: continue
            g["fills"] += 1; g["fill_wins"] += win; g["all_wins_when_fill_possible"] += 0
            g["maker_ev"] += win - filled - fee(filled, 0.0175); g["maker_ev0"] += win - filled; g["maker_cost"] += filled + fee(filled, 0.0175)
            g["price_gain"] += ask - filled; g["taker_ev_on_fills"] += tk_pay; g["taker_wins_on_fills"] += win
            g["all_wins"] += 0
    for t0 in agg: pass
print("rounds used: %d (from %s, last %.0f days)" % (n_rounds, D, days))
for t0 in sorted(agg, reverse=True):
    g = agg[t0]
    if not g["n"]: continue
    print("\nentry at about %d min in: %d orders per method" % ((900 - t0) // 60, g["n"]))
    print("  TAKER  profit per contract %+.3f  per $ staked %+.1f%%   (win rate %.0f%%)" % (g["taker_ev"] / g["n"], 100 * g["taker_ev"] / max(1e-9, g["taker_cost"]), 100 * (g["taker_ev"] / g["n"] + g["taker_cost"] / g["n"]) ))
    if g["fills"]:
        print("  MAKER  filled %d of %d (%.0f%%); avg price %.1f cents better than the ask; win rate when filled %.0f%% (taker on the same orders %.0f%%)" % (g["fills"], g["n"], 100 * g["fills"] / g["n"], 100 * g["price_gain"] / g["fills"], 100 * g["fill_wins"] / g["fills"], 100 * g["taker_wins_on_fills"] / g["fills"]))
        print("         profit per FILLED contract %+.3f (assumed 1.75%% fee) / %+.3f (0 fee);  taker on those same orders %+.3f" % (g["maker_ev"] / g["fills"], g["maker_ev0"] / g["fills"], g["taker_ev_on_fills"] / g["fills"]))
        print("         per $ staked: maker %+.1f%% vs taker %+.1f%%;  per ATTEMPT (unfilled = 0): maker %+.3f vs taker %+.3f" % (100 * g["maker_ev"] / max(1e-9, g["maker_cost"]), 100 * g["taker_ev"] / max(1e-9, g["taker_cost"]), g["maker_ev"] / g["n"], g["taker_ev"] / g["n"]))
print("\nReading it: the maker only helps if per-$ profit beats the taker's AFTER filling only on dips (adverse selection shows up as a lower win rate when filled). Fee for maker is assumed; confirm on a first real fill.")
