#!/bin/bash
# QUEUE-OK
# Kalshi news module step 1: probe which free news feeds the Pi can reach, fetch once, and make crew-update.sh (every 3 min) keep logging headlines to ~/market-data/news.jsonl.
cd ~/starship/markets || exit 1
OUT=~/starship/memory/inbox/news-probe.md
{ echo "# News feeds probe (queue 119, $(date '+%a %d %H:%M'))"; echo; echo '```'
  timeout 100 python3 news_log.py probe 2>&1
  echo; timeout 120 python3 news_log.py once 2>&1
  echo '```'; } > "$OUT"
grep -q "news_log.py" ~/crew-update.sh || echo '(flock -n /tmp/newslog.lock timeout 150 python3 $HOME/starship/markets/news_log.py once >> $HOME/news_log.out 2>&1 &)' >> ~/crew-update.sh
cat "$OUT"
