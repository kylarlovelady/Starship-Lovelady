#!/bin/bash
# QUEUE-OK
# close study: BTC speed per second, early-close check, z-rule timing vs when the book empties
python3 ~/starship/tasks/close_study.py 2>&1 | tail -45
