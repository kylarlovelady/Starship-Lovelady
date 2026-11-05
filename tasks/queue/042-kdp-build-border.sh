#!/bin/bash
# QUEUE-OK
# Rebuild both notebooks with the gold border drawn on top of the texture.
cd ~/kdp-studio || exit 1
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py 2>&1 | tail -60
ls -la ~/starship/memory/inbox/kdp-preview/* | head -30
