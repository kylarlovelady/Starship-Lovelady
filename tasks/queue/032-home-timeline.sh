#!/bin/bash
# QUEUE-OK
# Read-only: timeline of the last home voice attempts from Home Assistant's own debug log, plus how the satellite and its watchdog are set up.
echo "== satellite unit"; systemctl cat hub-satellite 2>/dev/null | grep -E "ExecStart|Environment|Restart" | cut -c1-400
echo "== watchdog unit"; systemctl cat hub-watchdog 2>/dev/null | grep -E "ExecStart" | cut -c1-300
echo "== HA voice pipeline events (last 90 min)"
docker logs --since 90m homeassistant 2>&1 | grep -E "assist_pipeline|wyoming|conversation|wake_word|stt|tts" | sed 's/\x1b\[[0-9;]*m//g' | cut -c1-210 | tail -45
