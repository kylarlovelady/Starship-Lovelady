#!/bin/bash
# Saves a key on the Pi only (never in chat, notes or GitHub). Usage: bash ~/starship/markets/setkey.sh WHALE_ALERT_KEY
NAME="${1:-WHALE_ALERT_KEY}"
case "$NAME" in WHALE_ALERT_KEY|HA_TOKEN) ;; *) echo "Unknown key name: $NAME"; exit 1;; esac
F=~/market-data/env
touch "$F"; chmod 600 "$F"
read -r -s -p "Paste your $NAME (it stays hidden), then press Enter: " V; echo
[ -z "$V" ] && { echo "Nothing entered. No change."; exit 1; }
grep -v "^$NAME=" "$F" > "$F.tmp"; echo "$NAME=$V" >> "$F.tmp"; mv "$F.tmp" "$F"; chmod 600 "$F"
sudo systemctl restart market-agent && echo "Saved and restarted. Check in a minute with: python3 ~/starship/markets/check.py"
