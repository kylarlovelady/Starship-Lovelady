#!/bin/bash
# QUEUE-OK
# Kalshi agent update for Kylar (read-only, practice money): forward review since Nov 16 (new wild-day test) and since Nov 11, wallet curves, did the wild variant load. Writes memory/inbox/kalshi-update-1123.md
cd ~/starship/markets || exit 1
OUT=~/starship/memory/inbox/kalshi-update-1123.md
{ echo "# Kalshi update (queue 126, $(date '+%a %d %H:%M'), practice money only)"; echo; echo '```'
  echo "== wild variant rows in trades.jsonl: $(grep -c v_hold_s250_wild ~/market-data/trades.jsonl 2>/dev/null)"
  echo "== agent: $(systemctl is-active market-agent 2>&1); markets repo: $(cd ~/starship && git log --oneline | head -1)"
  echo; echo "######## FORWARD REVIEW since Mon 16 (after the wild-day test was added)"
  timeout 150 python3 forward_review.py 2026-11-16 2>&1 | head -60
  echo; echo "######## FORWARD REVIEW since Wed 11"
  timeout 150 python3 forward_review.py 2026-11-11 2>&1 | head -45
  for w in v_hold_s250 v_hold_s250_wild hold; do echo; echo "######## WALLET CURVE $w (last 10 days)"; timeout 100 python3 wallet_curve.py $w 10 2>&1 | head -25; done
  echo '```'; } > "$OUT" 2>&1
echo "wrote $OUT ($(wc -l < "$OUT") lines)"
