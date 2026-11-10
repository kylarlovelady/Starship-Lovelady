#!/bin/bash
# QUEUE-OK
# Read-only: replay the recorded hold-to-end rounds under different bet-size rules (including Kylar's agree = bigger rule). Writes memory/inbox/kalshi-size-rules.md
cd ~/starship/markets || exit 1
OUT=~/starship/memory/inbox/kalshi-size-rules.md
{ echo "# Kalshi size rules replay (queue 107, $(date '+%a %d %H:%M'), practice money only)"; echo; echo '```'
  timeout 200 python3 size_rules.py v_hold_s500 2>&1 | head -60
  echo '```'; } > "$OUT"
echo "wrote $OUT"; cat "$OUT"
