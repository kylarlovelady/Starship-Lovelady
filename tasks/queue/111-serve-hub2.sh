#!/bin/bash
# QUEUE-OK
# Serve the new glass Hub preview from the Starship web port: http://<pi>:8095/hub2/index.html (copied from the repo every 3 minutes by crew-update.sh)
grep -q "crew-web/hub2" ~/crew-update.sh || echo 'mkdir -p ~/crew-web/hub2 && cp -r ~/starship/hub2/. ~/crew-web/hub2/' >> ~/crew-update.sh
mkdir -p ~/crew-web/hub2 && cp -r ~/starship/hub2/. ~/crew-web/hub2/
ls -la ~/crew-web/hub2
curl -s -o /dev/null -w "hub2 over http 8095: %{http_code}\n" http://127.0.0.1:8095/hub2/index.html
