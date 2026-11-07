#!/bin/bash
# QUEUE-OK
# give the home devices names in Pi-hole (local DNS names), then show the result
docker exec pihole pihole-FTL --config dns.hosts '["192.168.1.107 pi-hub","192.168.1.142 kylar-iphone","192.168.1.228 sharee-iphone","192.168.1.240 warren-ipad","192.168.1.130 living-room-tv"]' 2>&1 | head -5
sleep 3
echo "== dns.hosts now"; docker exec pihole pihole-FTL --config dns.hosts 2>&1 | head -3
echo "== name lookups via Pi-hole"
for n in kylar-iphone sharee-iphone warren-ipad living-room-tv pi-hub; do printf "%s -> " $n; getent hosts $n 2>/dev/null || python3 -c "import socket;print(socket.gethostbyname('$n'))" 2>&1 | head -1; done
echo "== reverse lookup of the iPad"; docker exec pihole pihole-FTL --config dns.hosts >/dev/null 2>&1; python3 -c "import socket;print(socket.gethostbyaddr('192.168.1.240'))" 2>&1 | head -1
