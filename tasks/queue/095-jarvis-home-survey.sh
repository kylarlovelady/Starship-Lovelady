#!/bin/bash
# QUEUE-OK
# read-only survey of the HOME Jarvis (Wyoming satellite, wake word, mic) so a mic mute switch and a false-wake watcher can be built. No keys are printed.
echo "== docker"; docker ps --format '{{.Names}}  {{.Image}}  {{.Status}}' 2>&1 | head -12
echo "== units (ExecStart only)"
for u in hub-satellite hub-voice hub-watchdog; do echo "-- $u: $(systemctl is-active $u 2>&1)"; systemctl cat $u 2>/dev/null | grep -E '^(ExecStart|User|WorkingDirectory)' | cut -c1-400; done
echo "== satellite process"; ps -eo user,pid,etime,args | grep -i -E "wyoming|satellite" | grep -v grep | cut -c1-420 | head -6
echo "== audio capture devices"; arecord -l 2>&1 | head -8
echo "== mixer (capture controls)"; for c in 0 1 2 3; do amixer -c $c scontrols 2>/dev/null | sed "s/^/card$c: /" | head -6; done
echo "== groups"; id -nG
echo "== voice-data"; ls -la ~/voice-data 2>&1 | head -14; ls ~/voice-data/home-mic 2>/dev/null | head -5
echo "== satellite log, last 24 h: count of key lines"; journalctl -u hub-satellite --since '24 hours ago' --no-pager 2>/dev/null > /tmp/sat24.log; wc -l /tmp/sat24.log
grep -i -c -E 'wake' /tmp/sat24.log; grep -i -E 'wake|detect|streaming|stt|pipeline|mute|error' /tmp/sat24.log | tail -25 | cut -c1-200
echo "== openwakeword container log tail"; for n in $(docker ps --format '{{.Names}}' | grep -i wake); do docker logs --tail 15 $n 2>&1 | cut -c1-200; done
echo "== tailscale name/ports free?"; ss -ltn 2>/dev/null | awk '{print $4}' | grep -E ':(8095|8097|8081|8099|10400|10300|10200|8123)$'
