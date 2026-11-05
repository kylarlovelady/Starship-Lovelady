#!/bin/bash
# QUEUE-OK
# First queue test: read-only facts so Claude can finish the install without screenshots.
echo "== crontab (names only)"; crontab -l 2>/dev/null | sed -E 's/^([^ ]+ +[^ ]+ +[^ ]+ +[^ ]+ +[^ ]+) .*#/\1 #/' | cut -c1-120
echo "== ha dir"; ls -ld ~/homeassistant ~/homeassistant/custom_components 2>&1 | head -3
echo "== docker"; docker ps --format '{{.Names}} {{.Status}}' 2>&1 | head -8
echo "== ha network"; docker inspect homeassistant --format '{{.HostConfig.NetworkMode}}' 2>&1 | head -1
echo "== pihole"; (pihole -v 2>&1 | head -4); systemctl is-active pihole-FTL 2>&1; curl -s -m 3 "http://127.0.0.1:8089/admin/api.php?summaryRaw" | head -c 300; echo; curl -s -m 3 http://127.0.0.1:8089/api/info/version | head -c 200; echo
echo "== services"; for s in market-agent phone-voice tailscaled hub-dashboard hub-watchdog; do echo "$s $(systemctl is-active $s)"; done
echo "== alerts test (dry)"; python3 ~/starship/tasks/alerts_check.py 2>&1 | tail -2; tail -3 ~/market-data/alerts.log 2>/dev/null | cut -c1-140
echo "== jarvis tools"; curl -s -X POST localhost:8099/ask -H 'Content-Type: application/json' -d '{"format":"json","text":"how is the pi doing","audio":false}' | head -c 400; echo
echo "== net watchdog"; ls ~/net_watchdog* /usr/local/bin/*watchdog* 2>/dev/null | head -5
