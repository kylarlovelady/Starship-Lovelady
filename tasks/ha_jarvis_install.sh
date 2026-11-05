#!/bin/bash
# Makes the home speaker (Home Assistant Assist) use the SAME Jarvis as your phone: same brain, shared memory, notes, memory commands.
# Safe: it only ADDS a small Home Assistant add-on folder; your old Assist setup stays and you can switch back in one tap.
# Run on the Pi:  bash ~/starship/tasks/ha_jarvis_install.sh
set -e
SRC=~/starship/ha/custom_components/jarvis_hub
CFG=""
for c in ~/homeassistant /config /opt/homeassistant; do [ -d "$c/.storage" ] && CFG="$c" && break; done
[ -z "$CFG" ] && { echo "Could not find the Home Assistant config folder (looked for .storage in ~/homeassistant). Tell Claude."; exit 1; }
[ -f "$SRC/manifest.json" ] || { echo "Update first: cd ~/starship && git pull"; exit 1; }
# the Home Assistant folder is owned by root (it runs in Docker), so this step needs your Pi password
sudo mkdir -p "$CFG/custom_components" && sudo rm -rf "$CFG/custom_components/jarvis_hub" && sudo cp -r "$SRC" "$CFG/custom_components/jarvis_hub" || { echo "Could not copy the add-on. Tell Claude."; exit 1; }
echo "Copied the Jarvis Hub add-on into $CFG/custom_components"
NAME=$(docker ps --format '{{.Names}}' 2>/dev/null | grep -i -m1 homeassistant || true)
URL="http://127.0.0.1:8099"
if [ -n "$NAME" ]; then
  MODE=$(docker inspect "$NAME" --format '{{.HostConfig.NetworkMode}}')
  echo "Home Assistant container: $NAME (network: $MODE)"
  if [ "$MODE" != "host" ]; then
    GW=$(docker network inspect bridge --format '{{(index .IPAM.Config 0).Gateway}}' 2>/dev/null || echo 172.17.0.1)
    sudo mkdir -p /etc/systemd/system/phone-voice.service.d
    printf '[Service]\nEnvironment=VOICE_BIND_EXTRA=%s\n' "$GW" | sudo tee /etc/systemd/system/phone-voice.service.d/ha.conf >/dev/null
    sudo systemctl daemon-reload; sudo systemctl restart phone-voice; sleep 3
    URL="http://$GW:8099"; echo "Jarvis also listens on the Docker bridge $GW (not on your Wi-Fi)."
  fi
  echo "Restarting Home Assistant (about a minute)..."; docker restart "$NAME" >/dev/null
else
  echo "No Home Assistant container found by name; restart Home Assistant yourself (Settings > System > Restart)."
fi
echo
echo "NOW, on your phone or laptop, open Home Assistant:"
echo " 1. Settings > Devices & services > Add integration > search 'Jarvis Hub'. Server address: $URL . Submit."
echo " 2. Settings > Voice assistants > your Jarvis assistant > Conversation agent: choose 'Jarvis Hub'. Save."
echo " 3. Say 'Hey Jarvis' at home. He should now know the same things as the phone Jarvis."
echo "To go back: set the Conversation agent to what it was before (the old OpenAI one). Nothing else changed."
echo "Check from the Pi:  curl -s -X POST localhost:8099/ask -H 'Content-Type: application/json' -d '{\"format\":\"json\",\"text\":\"what is on my to do list\",\"audio\":false}'"
