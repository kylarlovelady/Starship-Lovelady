#!/bin/bash
# QUEUE-OK
# Read-only: why is the Starship page (:8095) not loading?
echo "== listener"; ss -ltn | grep 8095
echo "== server process"; ps aux | grep "[h]ttp.server 8095" | cut -c1-200
echo "== files in crew-web"; ls -la ~/crew-web | head -30
echo "== fetch"; curl -s -m 5 -o /dev/null -w "index %{http_code} %{size_download}b\n" http://100.105.140.126:8095/
curl -s -m 5 -o /dev/null -w "crew.json %{http_code}\n" http://100.105.140.126:8095/crew.json
echo "== index.html matches repo?"; cmp ~/starship/index.html ~/crew-web/index.html && echo same
echo "== crew-update log"; tail -5 ~/crew-update.log 2>/dev/null
