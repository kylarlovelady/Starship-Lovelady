#!/usr/bin/env python3
"""READ-ONLY: does the previous 15-minute BTC round's result predict the next one? Uses ~/market-data/history/rounds.jsonl (every settled round Kalshi has, about 30 days).
Each round compares the 60 s average at its close with the 60 s average at its open, which is the previous round's close, so this is the lag-1 autocorrelation of 15-minute BTC returns.
Prints P(UP) after an UP and after a DOWN with counts, the gap and its standard error, older vs newer half, after two in a row, and by Central-time hour block."""
import collections, json, math, os, time
rows = []
for ln in open(os.path.expanduser("~/market-data/history/rounds.jsonl")):
    try:
        r = json.loads(ln); rows.append((int(r["close"]), 1 if r["result"] == "UP" else 0))
    except Exception:
        pass
rows.sort(); by = dict(rows)
print("rounds:", len(rows), "span days: %.1f" % ((rows[-1][0] - rows[0][0]) / 86400.0), "UP share: %.1f%%" % (100.0 * sum(r for c, r in rows) / len(rows)))
def tab(pairs, label):
    u = [b for a, b, c in pairs if a == 1]; d = [b for a, b, c in pairs if a == 0]
    if len(u) < 10 or len(d) < 10: print(label, "too few"); return
    pu, pd = sum(u) / len(u), sum(d) / len(d)
    se = math.sqrt(pu * (1 - pu) / len(u) + pd * (1 - pd) / len(d))
    print("%-22s P(UP|prev UP)=%.1f%% (n=%d)  P(UP|prev DOWN)=%.1f%% (n=%d)  gap=%+.1f pts  +-%.1f (1 SE)  z=%+.1f" % (label, 100 * pu, len(u), 100 * pd, len(d), 100 * (pu - pd), 100 * se, (pu - pd) / se))
pairs = [(by[c - 900], by[c], c) for c in sorted(by) if (c - 900) in by]
tab(pairs, "all")
m = sorted(c for a, b, c in pairs)[len(pairs) // 2]
tab([x for x in pairs if x[2] < m], "older half"); tab([x for x in pairs if x[2] >= m], "newer half")
two = [(by[c - 1800] + by[c - 900], by[c], c) for c in sorted(by) if (c - 900) in by and (c - 1800) in by]
for lab, key in (("after UP,UP", 2), ("after DOWN,DOWN", 0)):
    q = [b for a, b, c in two if a == key]
    if q: print("%-22s P(UP)=%.1f%% (n=%d)" % (lab, 100.0 * sum(q) / len(q), len(q)))
hb = collections.defaultdict(list)
for a, b, c in pairs:
    h = ((c - 21600) % 86400) // 3600; hb[h // 4].append((a, b, c))
for k in sorted(hb):
    tab(hb[k], "CT hours %02d-%02d" % (k * 4, k * 4 + 4))
