#!/bin/bash
# Saves the Kalshi key on the Pi only (never in chat, notes or GitHub).
#   bash ~/starship/markets/kalshi_setup.sh prod     (real account)    |    ... demo
set -e
D=~/market-data; mkdir -p "$D"; F="$D/env"; touch "$F"; chmod 600 "$F"
python3 -c "import cryptography" 2>/dev/null || pip install cryptography --break-system-packages -q
echo "Paste the PRIVATE key Kalshi showed you (all the lines, from -----BEGIN to -----END), then press Enter."
echo "Nothing is echoed back to the screen."
KEY=""
while IFS= read -r -s LINE; do
  KEY="$KEY$LINE"$'\n'
  case "$LINE" in *"-----END"*) break;; esac
done
[ -z "$KEY" ] && { echo "Nothing entered. No change."; exit 1; }
printf "%s" "$KEY" > "$D/kalshi_key.pem.new"; chmod 600 "$D/kalshi_key.pem.new"
if ! python3 -c "
from cryptography.hazmat.primitives import serialization
serialization.load_pem_private_key(open('$D/kalshi_key.pem.new','rb').read(), password=None)" 2>/dev/null; then
  rm -f "$D/kalshi_key.pem.new"; echo "That did not read as a private key. Nothing saved. Copy the whole block and try again."; exit 1
fi
mv "$D/kalshi_key.pem.new" "$D/kalshi_key.pem"
echo "Private key saved on this Pi (locked down)."
read -r -p "Now paste the Key ID Kalshi showed and press Enter: " ID
[ -z "$ID" ] && { echo "No Key ID entered. Run this again."; exit 1; }
grep -v "^KALSHI_KEY_ID=\|^KALSHI_ENV=" "$F" > "$F.tmp" || true
echo "KALSHI_KEY_ID=$ID" >> "$F.tmp"; echo "KALSHI_ENV=${1:-demo}" >> "$F.tmp"; mv "$F.tmp" "$F"; chmod 600 "$F"
echo "Saved. Environment: ${1:-demo}. Test it with: bash ~/starship/tasks/run.sh"
