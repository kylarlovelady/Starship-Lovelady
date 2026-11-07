#!/bin/bash
# QUEUE-OK
# read-only (v2, uses pihole-FTL sqlite3): which devices (addresses) used Pi-hole in the last 24 h, how many lookups, last seen, and the local names set today
echo "== devices seen in the last 24 h (address, lookups, last seen, blocked)"
docker exec pihole pihole-FTL sqlite3 -ni /etc/pihole/pihole-FTL.db "select client, count(*), datetime(max(timestamp),'unixepoch','localtime'), sum(case when status in (1,4,5,6,7,8,9,10,11) then 1 else 0 end) from queries where timestamp > strftime('%s','now')-86400 group by client order by count(*) desc;" 2>&1 | head -20
echo "== names Pi-hole knows (address, name)"
docker exec pihole pihole-FTL sqlite3 -ni /etc/pihole/pihole-FTL.db "select a.ip, a.name, n.macVendor from network_addresses a left join network n on n.id=a.network_id order by a.lastSeen desc limit 20;" 2>&1 | head -20
echo "== local DNS names set (dns.hosts)"
docker exec pihole pihole-FTL --config dns.hosts 2>&1 | head -5
