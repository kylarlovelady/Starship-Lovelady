#!/bin/bash
# QUEUE-OK
# read-only: the missed 00:00 round in detail, and how the home screen applies the font
echo "== log lines for the 01:00 (00:00 local) round"; grep "NOV060100" ~/market-data/snipe_log.jsonl | cut -c1-400
echo "== agent journal 23:57 to 00:03"; journalctl -u market-agent --since "23:57" --until "00:03" --no-pager 2>/dev/null | cut -c1-220 | tail -15
echo "== tick coverage 23:59:00 to 00:00:10 (rows per second)"; python3 - <<'PY'
import glob, json, time, collections
c = collections.Counter(); last = None
for p in sorted(glob.glob("/home/kylarlovelady/market-data/ticks-*.jsonl"))[-2:]:
    for l in open(p):
        try: r = json.loads(l)
        except ValueError: continue
        t = r.get("t", 0)
        if 1793945930 <= t <= 1793946010: c[int(t) - 1793945930] += 1; last = (r.get("left"), (r.get("k") or {}).get("ticker"), bool(r.get("ob")))
print("seconds with a row:", len([k for k in c]), "of 80; last row (left, ticker, has book):", last)
PY
echo "== font in index.html"; grep -n -i "font" ~/hub-dashboard/index.html | cut -c1-260 | head -25
