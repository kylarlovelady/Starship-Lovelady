#!/bin/bash
# QUEUE-OK
# install the home Jarvis mic switch (port 8098) and wake watcher; then show the first status
bash ~/starship/tasks/jarvis_install.sh
echo "--- watcher report"; head -12 ~/starship/memory/inbox/jarvis-wake-report.md 2>/dev/null
