#!/bin/bash
# QUEUE-OK
# Is the Hub media library server answering?
echo "process:"; pgrep -af "hub2/media_server.py" | cut -c1-120
echo "state:"; curl -s -m 5 http://127.0.0.1:8110/api/state | cut -c1-200; echo
echo "crew-update line:"; grep -c "hub2/media_server.py" ~/crew-update.sh
ls ~/hub-media 2>&1 | head -3
