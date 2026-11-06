#!/usr/bin/env python3
"""How much can actually be bought at <=99c on the favourite, second by second before the close? Reads ~/market-data/ticks-*.jsonl(.gz). Writes memory/inbox/liq-by-second.md.
Caveat: the recorder skips seconds where a side of the book is empty, so 'no row' at small s means the book was one-sided (nothing to buy)."""
import glob, gzip, json, os, collections
HOME = os.path.expanduser("~"); D = HOME + "/market-data"; OUT = HOME + "/starship/memory/inbox/liq-by-second.md"
rows = collections.defaultdict(dict)   # ticker -> {s: dollars_fillable}
rounds = set()
def lv(x, sc): 
    o = []
    for a in x or []:
        try: o.append((float(a[0]) / sc, float(a[1])))
        except Exception: pass
    return o
for p in sorted(glob.glob(D + "/ticks-*.jsonl*")):
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: r = json.loads(l)
                except ValueError: continue
                s = r.get("left"); tk = (r.get("k") or {}).get("ticker")
                if tk is None or s is None or s < 0 or s > 40: continue
                rounds.add(tk); ob = r.get("ob") or {}
                yl, nl = ob.get("yes_dollars") or ob.get("yes"), ob.get("no_dollars") or ob.get("no")
                both = list(yl or []) + list(nl or [])
                if not both: rows[tk][s] = 0.0; continue
                sc = 1.0 if max(float(a[0]) for a in both) <= 1.0 else 100.0
                yb, nb = lv(yl, sc), lv(nl, sc)
                if not yb or not nb: rows[tk][s] = 0.0; continue
                fav_y = max(a for a, b in yb) >= max(a for a, b in nb)
                opp = nb if fav_y else yb
                rows[tk][s] = sum(q * (1 - p) for p, q in opp if 1 - p <= 0.99 + 1e-9)    # dollars of favourite you could buy at <=99c
    except OSError: continue
L = ["# Liquidity before the close (auto): dollars buyable on the favourite at 99c or less", "", "Rounds seen: %d. 'any' = at least $25 buyable, 'full' = at least $1,000 buyable. Seconds with no row count as nothing buyable." % len(rounds), "", "| s before close | rounds with data | any | full ($1,000) | median $ buyable |", "|---|---|---|---|---|"]
for s in list(range(0, 21)) + [25, 30, 40]:
    vals = [rows[t].get(s, 0.0) for t in rows]
    if not vals: continue
    vs = sorted(vals); n = len(vs)
    L.append("| %d | %d | %.0f%% | %.0f%% | $%.0f |" % (s, n, 100 * sum(v >= 25 for v in vs) / n, 100 * sum(v >= 1000 for v in vs) / n, vs[n // 2]))
open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L))
