#!/bin/bash
# QUEUE-OK
# Rerun of 102 for the overnight Nov 8-9 results (practice money, read-only). Result: memory/inbox/kalshi-wallet-curve.md
cd ~/starship/markets || exit 1
OUT=~/starship/memory/inbox/kalshi-wallet-curve.md
{ echo "# Kalshi wallet curve (queue 103, $(date '+%a %d %H:%M'), practice money only)"; echo; echo '```'
  timeout 120 python3 wallet_curve.py v_hold_s500 30 2>&1 | head -90
  echo; echo "---- v_hold_s100 (same entries, 1/5 the size) ----"
  timeout 90 python3 wallet_curve.py v_hold_s100 6 2>&1 | head -14
  echo '```'; } > "$OUT"
echo "wrote $OUT ($(wc -l < "$OUT") lines)"
cat "$OUT"
