#!/bin/bash
# QUEUE-OK
# Read-only look at the home screen page so Claude can add a frosted-glass bubble behind the clock/weather/date.
echo "== crew-update.sh"; sed -n 1,25p ~/crew-update.sh | cut -c1-160
echo "== crew-web"; ls -l ~/crew-web | head -20 | cut -c1-100
F=~/crew-web/index.html
echo "== size/lines"; wc -lc $F; cmp -s $F ~/starship/index.html && echo "SAME as repo index.html" || echo "DIFFERENT from repo index.html"
echo "== hits (line:text, cut)"; grep -n -i -E "clock|weather|theme|<body|\.date|backdrop" $F | cut -c1-170 | head -60
echo "== has glass already?"; grep -c -i "backdrop-filter" $F
