#!/bin/bash
# QUEUE-OK
# read-only Pi-hole check: container, DNS answers, blocking, address
echo "== container"; docker ps --filter name=pihole --format '{{.Names}} {{.Status}} {{.Ports}}' | cut -c1-200
echo "== pi address"; hostname -I
echo "== normal lookup via pihole"; dig +short +time=2 +tries=1 @127.0.0.1 example.com | head -3
echo "== ad domain via pihole (blocked answers 0.0.0.0 or ::)"; dig +short +time=2 +tries=1 @127.0.0.1 doubleclick.net | head -3
echo "== same ad domain via 1.1.1.1 (real address)"; dig +short +time=2 +tries=1 @1.1.1.1 doubleclick.net | head -3
echo "== pihole version"; docker exec pihole pihole -v 2>&1 | head -4
echo "== pihole status"; docker exec pihole pihole status 2>&1 | head -5
echo "== what the Pi itself uses for DNS"; grep -v '^#' /etc/resolv.conf | head -3
