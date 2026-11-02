#!/bin/bash
# Saves the Kalshi key id on the Pi (never in chat/GitHub). The private key was made on this Pi by an earlier run and never leaves it.
#   bash ~/starship/markets/kalshi_setup.sh prod <KEY_ID>      (real account; use demo for the demo site)
set -e
D=~/market-data; mkdir -p "$D"; F="$D/env"; touch "$F"; chmod 600 "$F"
python3 -c "import cryptography" 2>/dev/null || pip install cryptography --break-system-packages -q
if [ ! -f "$D/kalshi_key.pem" ]; then
  openssl genpkey -algorithm ed25519 -out "$D/kalshi_key.pem"; chmod 600 "$D/kalshi_key.pem"; echo "Made a new private key on this Pi."
fi
echo "=== PUBLIC key on this Pi (include the BEGIN and END lines when pasting into Kalshi) ==="
openssl pkey -in "$D/kalshi_key.pem" -pubout; echo "=== end ==="
ID="$2"; [ -z "$ID" ] && read -r -p "Paste the Key ID and press Enter: " ID
[ -z "$ID" ] && { echo "No Key ID. Run again with it."; exit 1; }
grep -v "^KALSHI_KEY_ID=\|^KALSHI_ENV=" "$F" > "$F.tmp" || true
echo "KALSHI_KEY_ID=$ID" >> "$F.tmp"; echo "KALSHI_ENV=${1:-demo}" >> "$F.tmp"; mv "$F.tmp" "$F"; chmod 600 "$F"
echo "Saved. Environment: ${1:-demo}. Test it with: bash ~/starship/tasks/run.sh"
