#!/bin/bash
# QUEUE-OK
# make Pi-hole show the new device names: write them into its client table, then restart its DNS (a few seconds of pause)
DB=/etc/pihole/pihole-FTL.db
for pair in "192.168.1.107 pi-hub" "192.168.1.142 kylar-iphone" "192.168.1.228 sharee-iphone" "192.168.1.240 warren-ipad" "192.168.1.130 living-room-tv"; do
  ip=${pair% *}; nm=${pair#* }
  docker exec pihole pihole-FTL sqlite3 -ni $DB "update network_addresses set name='$nm', nameupdated=strftime('%s','now') where ip='$ip';" 2>&1 | head -2
done
docker exec pihole pihole-FTL --config resolver.refreshNames ALL 2>&1 | head -2
docker exec pihole pihole restartdns 2>&1 | tail -2
sleep 8
echo "== names now (address|name)"
docker exec pihole pihole-FTL sqlite3 -ni $DB "select ip, name from network_addresses where ip like '192.168.1.%';" 2>&1 | head -10
echo "== DNS still answering?"; docker exec pihole pihole status 2>&1 | head -3
