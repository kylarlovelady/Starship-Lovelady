#!/bin/bash
# QUEUE-OK
# build the friendly Pi-hole activity page once now (private, stays on the Pi; this only prints a one-line summary, never browsing history)
cd ~/starship && python3 tasks/pihole_activity.py 2>&1 | tail -3
ls -la ~/crew-web/activity.html 2>&1 | cut -c1-120
