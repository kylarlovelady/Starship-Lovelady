#!/usr/bin/env python3
"""READ-ONLY, STRICTER maker (resting order) study. Trades nothing.
The first maker study (maker_study.py) counted a resting buy as filled whenever the price touched it. Real life is stricter: our resting buy only fills
when somebody actually SELLS into it. Here a fill needs a REAL trade on Kalshi's public tape (recorded as "kt" in the per-second files) printing at our price
or better, on the right side, after we posted, within the wait window. We post 1 cent ABOVE the best bid (so we are first in the queue at that price) and skip
rounds where the spread is under 2 cents (no room). Compare with TAKER (buy at the ask right away). Both hold to the real result.
For each entry time (1, 2, 3 minutes into the round) and both sides (no prediction needed) it prints: how often we post, how often it fills, the win rate of the
orders that filled vs all posted (the adverse-selection check: do we only get filled when we are wrong?), and profit per $ for maker (1.75% fee, ASSUMED, also 0 fee)
vs taker (7% fee) on the same orders. Run: python3 maker_study2.py [days=4]. Output: ~/starship/memory/inbox/maker-study2.md"""
import collections, glob, gzip, json, os, sys, time
from calendar import timegm
D = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data"))
days = float(sys.argv[1]) if len(sys.argv) > 1 else 4
OUT = os.environ.get("OUTF", os.path.expanduser("~/starship/memory/inbox/maker-study2.md"))
WAIT = 120
fee_t = lambda p: 0.07 * p * (1 - p)
fee_m = lambda p: 0.0175 * p * (1 - p)


def lv(x):
    try:
        return [(float(a), float(b)) for a, b in x]
    except Exception:
        return []


def ts(s):
    try:
        return timegm(time.strptime(str(s)[:19], "%Y-%m-%dT%H:%M:%S"))
    except Exception:
        return None


ROWS = collections.defaultdict(list)    # close -> [(t, left, yb, ya)]
TR = collections.defaultdict(dict)      # close -> {trade id: (epoch, yes price, size, taker side)}
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
                if r.get("left") is None or r.get("t") is None:
                    continue
                if r["left"] < 570:
                    continue          # entries are 1 to 3 minutes in plus a 2 minute wait: the first 5 minutes is enough
                ce = int(round(r["t"] + r["left"]))
                for x in (r.get("kt") or []):
                    try:
                        yp = float(x.get("yes")); yp = yp if yp <= 1.0 else yp / 100.0
                        TR[ce][x.get("id")] = (ts(x.get("ts")), yp, float(x.get("n") or 0), x.get("side"))
                    except (TypeError, ValueError):
                        pass
                ob = r.get("ob") or {}
                y = lv(ob.get("yes_dollars") or ob.get("yes") or [])
                n = lv(ob.get("no_dollars") or ob.get("no") or [])
                if not y or not n:
                    continue
                sc = 1.0 if max(a for a, b in y + n) <= 1.0 else 100.0
                ROWS[ce].append((float(r["t"]), float(r["left"]), max(a for a, b in y) / sc, 1 - max(a for a, b in n) / sc))
    except OSError:
        pass
HIST = {}
try:
    for ln in open(os.path.join(D, "history", "rounds.jsonl")):
        try:
            r_ = json.loads(ln); HIST[int(r_["close"])] = 1 if r_["result"] == "UP" else 0
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
for ce, seq in ROWS.items():
    seq.sort()
    if len(seq) < 200 or seq[0][1] < 800 or result(ce) is None or not TR.get(ce):
        continue
    rounds.append((ce, seq, result(ce), sorted((v for v in TR[ce].values() if v[0] is not None), key=lambda v: v[0])))
rounds.sort()
L = ["# Stricter maker study (fills need a real trade on the tape), last %g days" % days, "",
     "Rounds with a full recording, a tape and a real result: **%d**. Orders are 1 contract; post 1c above the best bid; wait %d s; hold to the result." % (len(rounds), WAIT), ""]
if len(rounds) < 20:
    L.append("Too few rounds with a trade tape yet.")
    open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L)); sys.exit(0)
L += ["| entry | possible orders | skipped (spread under 2c) | filled | fill rate | win rate (filled) | win rate (all posted) | avg maker price | maker profit/$ (1.75% fee) | maker profit/$ (0 fee) | taker profit/$ same orders | taker profit/$ filled only |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for off in (60, 120, 180):
    n_pos = n_skip = n_fill = 0
    w_fill = w_all = 0
    cm = pm = pm0 = ct = pt = ctf = ptf = cp = 0.0
    for ce, seq, res, tape in rounds:
        row = next((s for s in seq if s[1] <= 900 - off), None)
        if row is None:
            continue
        t0, left, yb, ya = row
        for side in ("Y", "N"):
            if side == "Y":
                bid, ask = yb, ya
            else:
                bid, ask = 1 - ya, 1 - yb
            if ask - bid < 0.0199 or bid < 0.03 or ask > 0.97:
                n_skip += 1; continue
            p = round(bid + 0.01, 2)
            n_pos += 1
            win = (res == 1) if side == "Y" else (res == 0)
            w_all += 1 if win else 0
            ct += ask + fee_t(ask); pt += (1.0 if win else 0.0) - ask - fee_t(ask)
            filled = False
            for (te, yp, sz, ts_side) in tape:
                if te < t0 or te > t0 + WAIT:
                    continue
                if side == "Y" and ts_side == "no" and yp <= p + 1e-9 and sz >= 1:
                    filled = True; break
                if side == "N" and ts_side == "yes" and yp >= (1 - p) - 1e-9 and sz >= 1:
                    filled = True; break
            if filled:
                n_fill += 1; w_fill += 1 if win else 0
                cp += p; cm += p + fee_m(p); pm += (1.0 if win else 0.0) - p - fee_m(p); pm0 += (1.0 if win else 0.0) - p
                ctf += ask + fee_t(ask); ptf += (1.0 if win else 0.0) - ask - fee_t(ask)
    if n_pos and n_fill:
        L.append("| %d s in | %d | %d | %d | %.0f%% | %.0f%% | %.0f%% | %.0fc | %+.1f%% | %+.1f%% | %+.1f%% | %+.1f%% |" % (
            off, n_pos, n_skip, n_fill, 100.0 * n_fill / n_pos, 100.0 * w_fill / n_fill, 100.0 * w_all / n_pos, 100 * (cp / n_fill), 100 * pm / cm,
            100 * pm0 / cp, 100 * pt / ct, 100 * ptf / ctf))
    else:
        L.append("| %d s in | %d | %d | %d | | | | | | | | |" % (off, n_pos, n_skip, n_fill))
L += ["", "## How to read it", "",
      "- Fill rate: the share of resting orders a real seller actually hit. The first study assumed much higher.",
      "- If the win rate of FILLED orders is lower than for ALL posted orders, we get filled mostly when we are wrong (adverse selection) and the maker saving is partly an illusion.",
      "- 'taker profit/$ filled only' is the fair comparison: the same orders that filled, bought at the ask instead. Maker beats taker only if maker profit/$ is higher there.",
      "- The 1.75% maker fee is from one article (dev.to) and should be confirmed with a real fill. Practice only; sample is a few hundred orders, so small differences are noise."]
open(OUT, "w").write("\n".join(L) + "\n")
print("\n".join(L))
