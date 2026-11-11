#!/bin/bash
# QUEUE-OK
# Why isn't the Hub media server staying up? Try it in the foreground briefly, then start it detached.
S=$HOME/starship/hub2/media_server.py
echo "python: $(python3 --version 2>&1)"
echo "-- foreground test (3 s)"; timeout 3 python3 "$S" 2>&1 | head -8; echo "exit: $?"
echo "-- tail of crew-update.sh"; tail -4 ~/crew-update.sh | cut -c1-160
setsid nohup python3 "$S" >"$HOME/hub-media.log" 2>&1 < /dev/null &
sleep 3
echo "-- after detached start"; pgrep -af "hub2/media_server.py" | cut -c1-100; curl -s -m 5 http://127.0.0.1:8097/api/state | cut -c1-160; echo; cat "$HOME/hub-media.log" | head -5
