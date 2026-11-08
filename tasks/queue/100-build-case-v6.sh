#!/bin/bash
# QUEUE-OK
# Rebuilds the kitchen screen case v6 on the Pi and runs the fit checks (needs node; reports if it is missing).
cd ~/starship/hardware/kitchen-screen-case/v6 || exit 1
command -v node >/dev/null || { echo "node is not installed on this Pi"; exit 0; }
node --stack-size=30000 case.mjs 2>&1 | tail -12
node --stack-size=30000 verify.mjs 2>&1 | tail -34
python3 check_mesh.py
