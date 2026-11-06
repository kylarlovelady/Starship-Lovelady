#!/bin/bash
# QUEUE-OK
# Scan Amazon and Google search-bar suggestions for the KDP notebook keywords (about 4 minutes). Output in memory/inbox/kdp-keywords.md.
python3 ~/starship/tasks/kdp_keywords.py 2>&1 | tail -10
