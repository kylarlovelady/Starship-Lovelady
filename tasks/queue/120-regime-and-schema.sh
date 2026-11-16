#!/bin/bash
# QUEUE-OK
# Kalshi daily self-review step 1: label past days calm/trending/wild and show each strategy per kind of day; also list the field names of the Pi's data files (keys only) so the round-by-round review can use them.
cd ~/starship/markets || exit 1
OUT=~/starship/memory/inbox/kalshi-regime-days.md
{ echo "# Kalshi regime days (queue 120, $(date '+%a %d %H:%M'), practice money only)"; echo; echo '```'
  timeout 200 python3 regime_days.py 2>&1 | head -70
  echo; echo "---- data file field names (keys only) ----"
  M=~/market-data
  for f in trades.jsonl sim_windows.jsonl calls.jsonl snapshots.jsonl history/rounds.jsonl; do
    echo "== $f"; tail -n 1 $M/$f 2>/dev/null | python3 -c "
import sys, json
for ln in sys.stdin:
    try:
        r = json.loads(ln)
        print('  keys:', sorted(r)[:40])
        for k, v in r.items():
            if isinstance(v, dict): print('  ', k, '->', sorted(v)[:25])
    except Exception as e: print('  unreadable', e)"
  done
  echo '```'; } > "$OUT"
cat "$OUT" | cut -c1-260
