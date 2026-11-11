#!/bin/bash
# QUEUE-OK
# Read-only probe for the new Hub screen: counts of Home Assistant device types (no names, no token) and how Jarvis mutes the mic. Writes memory/inbox/hub-probe.md
OUT=~/starship/memory/inbox/hub-probe.md
{ echo "# Hub probe ($(date '+%a %d %H:%M'))"; echo; echo '```'
python3 - <<'P'
import json, os, urllib.request
env = {}
for fn in ("market-data/env", "voice-data/keys.env"):
    try:
        for l in open(os.path.expanduser("~/" + fn)):
            if "=" in l and not l.lstrip().startswith("#"): k, v = l.strip().split("=", 1); env[k] = v.strip().strip('"\'')
    except OSError: pass
tok = env.get("HA_TOKEN"); base = (env.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/")
if not tok: print("no HA_TOKEN"); raise SystemExit
try:
    req = urllib.request.Request(base + "/api/states", headers={"Authorization": "Bearer " + tok})
    st = json.load(urllib.request.urlopen(req, timeout=8))
except Exception as e: print("HA read failed:", type(e).__name__); raise SystemExit
from collections import Counter
c = Counter(s["entity_id"].split(".")[0] for s in st)
print("Home Assistant entities by type:", dict(c.most_common()))
for dom in ("light", "switch", "climate", "media_player", "cover", "lock", "camera", "fan", "scene", "script", "input_boolean"):
    xs = [s for s in st if s["entity_id"].startswith(dom + ".")]
    if xs: print(" ", dom, len(xs), "on:", sum(1 for s in xs if s["state"] in ("on", "playing", "open", "unlocked", "heat", "cool", "auto")))
lights = [s for s in st if s["entity_id"].startswith("light.")]
modes = Counter(m for s in lights for m in (s["attributes"].get("supported_color_modes") or []))
print("light colour modes:", dict(modes))
P
echo; echo "hub services:"; systemctl list-units 'hub-*' --no-legend --plain 2>/dev/null | awk '{print $1, $3, $4}'
echo; echo "mute mentions in hub scripts:"; grep -n -i "mute" /usr/local/bin/hub-*.py 2>/dev/null | cut -c1-170 | head -14
echo; echo "mic state (alsa):"; amixer scontents 2>/dev/null | grep -i -B1 -A3 "capture" | head -12
echo '```'; } > "$OUT"
echo "wrote $OUT"; cat "$OUT"
