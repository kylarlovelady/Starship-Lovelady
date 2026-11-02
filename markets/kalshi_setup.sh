#!/bin/bash
# Makes a trading key pair ON THE PI. The private key never leaves it. You only copy the PUBLIC key into Kalshi.
set -e
D=~/market-data; mkdir -p "$D"
python3 -c "import cryptography" 2>/dev/null || pip install cryptography --break-system-packages -q
if [ ! -f "$D/kalshi_key.pem" ]; then
  openssl genpkey -algorithm ed25519 -out "$D/kalshi_key.pem"; chmod 600 "$D/kalshi_key.pem"
  echo "Made a new private key on this Pi."
fi
echo; echo "=== PUBLIC key: copy everything between the lines into Kalshi's 'public key' box ==="
openssl pkey -in "$D/kalshi_key.pem" -pubout
echo "=== end ==="; echo
read -r -p "After Kalshi gives you the Key ID, paste it here and press Enter: " ID
[ -z "$ID" ] && { echo "No Key ID entered. Run this again when you have it."; exit 1; }
F="$D/env"; touch "$F"; chmod 600 "$F"
grep -v "^KALSHI_KEY_ID=\|^KALSHI_ENV=" "$F" > "$F.tmp" || true
echo "KALSHI_KEY_ID=$ID" >> "$F.tmp"; echo "KALSHI_ENV=${1:-demo}" >> "$F.tmp"; mv "$F.tmp" "$F"; chmod 600 "$F"
echo "Saved. Environment: ${1:-demo}. Test it with: bash ~/starship/tasks/run.sh"
