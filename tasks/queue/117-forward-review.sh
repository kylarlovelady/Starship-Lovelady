#!/bin/bash
# QUEUE-OK
# Forward-test review + luck check (read-only, practice money). Writes memory/inbox/kalshi-forward-review.md
cd ~/starship/markets || exit 1
OUT=~/starship/memory/inbox/kalshi-forward-review.md
{ echo "# Kalshi forward review (queue 117, $(date '+%a %d %H:%M'), practice money only)"; echo; echo '```'
  timeout 150 python3 forward_review.py 2026-11-11 2>&1 | head -80
  echo '```'; } > "$OUT"
echo "wrote $OUT ($(wc -l < "$OUT") lines)"; cat "$OUT"
