#!/bin/bash
# QUEUE-OK
# how much can be bought at 99c or less, second by second before the close
python3 ~/starship/tasks/liq_by_second.py 2>&1 | tail -30
