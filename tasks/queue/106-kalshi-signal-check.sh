#!/bin/bash
# QUEUE-OK
# Read-only: do the agent's signals agree with its winning bets, and why are some rounds $5? Writes memory/inbox/kalshi-signal-check.md
cd ~/starship/markets || exit 1
OUT=~/starship/memory/inbox/kalshi-signal-check.md
{ echo "# Kalshi signal check (queue 106, $(date '+%a %d %H:%M'), practice money only)"; echo; echo '```'
  timeout 200 python3 signal_check.py v_hold_s500 2>&1 | head -80
  echo '```'; } > "$OUT"
echo "wrote $OUT"; cat "$OUT"
