#!/bin/bash
# Installs the home Jarvis mic switch (keep-alive every minute) and the wake watcher (every 5 minutes) in the user crontab, and starts the switch now.
S=$HOME/starship/tasks
( crontab -l 2>/dev/null | grep -v -E 'jarvis-mic|jarvis-watch'
  echo "* * * * * flock -n /tmp/jarvis-mic.lock python3 $S/jarvis_mic.py >> $HOME/jarvis-mic.log 2>&1 # jarvis-mic"
  echo "*/5 * * * * python3 $S/jarvis_watch.py >> $HOME/jarvis-watch.log 2>&1 # jarvis-watch" ) | crontab -
# (do not start the server from here: a process started by the task queue inherits the queue lock; cron starts it cleanly within a minute)
python3 $S/jarvis_watch.py; curl -s -m 3 http://127.0.0.1:8098/mic | cut -c1-300; echo; ss -ltn | grep ':8098'
