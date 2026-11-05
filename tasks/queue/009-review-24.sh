#!/bin/bash
# QUEUE-OK
# Read-only: the agent's own review of the last 24 hours (practice money). No orders, no changes.
cd ~/starship/markets && timeout 200 python3 review.py 24 2>&1 | grep -v -i -E "balance|token|secret|api.?key" | head -c 5800
