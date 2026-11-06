#!/bin/bash
# QUEUE-OK
# Start the KDP keyword scan in the background (048 ran too long for the queue). Output file: memory/inbox/kdp-keywords.md, log in /tmp/kdp-kw.log
nohup python3 ~/starship/tasks/kdp_keywords.py > /tmp/kdp-kw.log 2>&1 &
sleep 2; echo "started pid $!"
