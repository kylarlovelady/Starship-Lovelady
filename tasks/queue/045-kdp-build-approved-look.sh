#!/bin/bash
# QUEUE-OK
# Rebuild all 8 notebooks (2 titles x 4 colour schemes) in the look Kylar approved: flat colour, fine grain, flat lettering, CAPS, double border.
cd ~/kdp-studio || exit 1
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py 2>&1 | tail -60
ls -la ~/starship/memory/inbox/kdp-preview/* | head -30
