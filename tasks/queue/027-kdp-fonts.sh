#!/bin/bash
# QUEUE-OK
# Read-only: which fonts can the KDP studio use? Can the Pi reach Google Fonts on GitHub (open-license fonts)?
cd ~/kdp-studio || exit 1
./.venv/bin/python - <<'PY'
import sys; sys.path.insert(0,".")
import engine
F=engine.discover()
print("studio fonts (%d):"%len(F)); print(", ".join(sorted(F)))
PY
echo "== other fonts on the system"; fc-list : family 2>/dev/null | sort -u | head -60 | tr '\n' ';' | cut -c1-1500
echo; echo "== can reach GitHub raw?"; curl -s -m 8 -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/google/fonts/main/ofl/oswald/OFL.txt
