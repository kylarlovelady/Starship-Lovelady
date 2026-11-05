#!/bin/bash
# Lets Jarvis and the Starship read Pi-hole's stats. Pi-hole 6 needs its web password. Run once; the password is typed hidden and stored only on the Pi
# in ~/voice-data/keys.env (chmod 600). Tip: in Pi-hole > Settings > Web interface/API you can make an "app password" just for this and use that instead.
read -s -p "Pi-hole web password (nothing shows as you type): " PW; echo
[ -z "$PW" ] && { echo "Nothing entered."; exit 1; }
mkdir -p ~/voice-data; touch ~/voice-data/keys.env; chmod 600 ~/voice-data/keys.env
grep -v '^PIHOLE_PASSWORD=' ~/voice-data/keys.env > ~/voice-data/keys.env.new; echo "PIHOLE_PASSWORD=$PW" >> ~/voice-data/keys.env.new; mv ~/voice-data/keys.env.new ~/voice-data/keys.env; chmod 600 ~/voice-data/keys.env
python3 - <<'PY'
import sys, os; sys.path.insert(0, os.path.expanduser("~/starship/voice")); import tools; print(tools.pihole())
PY
