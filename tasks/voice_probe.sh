#!/bin/bash
# Read-only inventory of what the Pi has for voice, so the build fits it. Prints no keys.
echo "== system"; uname -m; python3 --version; free -m | sed -n 2p; df -h / | tail -1
echo "== mic / speakers"; arecord -l 2>/dev/null | grep -i card | head -4; aplay -l 2>/dev/null | grep -i card | head -4
echo "== tailscale"; tailscale version 2>/dev/null | head -1; tailscale serve status 2>&1 | head -5
echo "== voice services"; systemctl list-units --type=service --all 2>/dev/null | grep -i -E "wyoming|wake|whisper|piper|assist|voice|homeassistant|home-assistant" | head -10
docker ps --format '{{.Names}}  {{.Image}}' 2>/dev/null | head -10
echo "== ports"; ss -ltn 2>/dev/null | grep -E ":(8099|8123|10300|10400|10200|10700)\b" | head
echo "== phone-voice"; systemctl is-active phone-voice 2>/dev/null; ls ~/voice-data 2>/dev/null | head
