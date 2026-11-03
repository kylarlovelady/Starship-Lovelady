#!/bin/bash
# Picks which phone gets the Dynamic Island / Live Activity (only yours), saves it, and sends a 20-second test. Sends no secrets.
F=~/market-data/env; touch "$F"; chmod 600 "$F"
cd ~/starship/markets || exit 1
python3 - <<'PY'
import alerts, json
e = alerts._env()
try:
    names = alerts._targets((e.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/"), e["HA_TOKEN"])
except Exception as ex:
    print("Could not list phones:", ex); raise SystemExit(1)
open("/tmp/island-names", "w").write("\n".join(names))
for i, n in enumerate(names, 1): print(i, n)
PY
N=$(wc -l < /tmp/island-names); [ "$N" -ge 0 ] || exit 1
read -r -p "Number of YOUR iPhone from the list: " PICK
DEV=$(sed -n "${PICK}p" /tmp/island-names)
[ -z "$DEV" ] && { echo "That is not a number on the list."; exit 1; }
grep -v "^HA_LIVE_DEVICE=" "$F" > "$F.tmp"; echo "HA_LIVE_DEVICE=$DEV" >> "$F.tmp"; mv "$F.tmp" "$F"; chmod 600 "$F"
echo "Saved $DEV. Sending a test to the Dynamic Island for 20 seconds..."
python3 - <<'PY'
import alerts, time
e = alerts._env(); base = (e.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/")
alerts._activity(e["HA_TOKEN"], base, e["HA_LIVE_DEVICE"], "kalshi_test", "LIVE · $239.17 (test)", "+$0.00 this session · 0/0 rounds won", "$239", "#ff4d57", (300, 900))
time.sleep(20)
alerts._activity(e["HA_TOKEN"], base, e["HA_LIVE_DEVICE"], "kalshi_test", "", "", "", "", None, True)
print("Test finished. If you saw it on the lock screen or Dynamic Island, it works.")
PY
