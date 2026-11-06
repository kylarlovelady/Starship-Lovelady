#!/bin/bash
# QUEUE-OK
# check the locked series spec: the build plan (no files rebuilt) and the ready-to-paste listing text
cd ~/kdp-studio && ~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py --check 2>&1 | tail -12
python3 ~/starship/tasks/kdp_listing.py 2>&1 | tail -14
