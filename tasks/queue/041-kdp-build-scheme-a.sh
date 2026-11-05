#!/bin/bash
# QUEUE-OK
# Build Process Operator and Lab Operator (colour scheme A) in the KDP studio, run its checks, write preview images to memory/inbox/kdp-preview.
cd ~/kdp-studio || exit 1
~/kdp-studio/.venv/bin/python ~/starship/tasks/kdp_build.py 2>&1 | tail -60
ls -la ~/starship/memory/inbox/kdp-preview/* | head -30
