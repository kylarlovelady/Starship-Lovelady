#!/bin/bash
# One-time setup for the BTC market agent on the Pi. Safe to run again.
set -e
U=$(whoami)
cd ~/starship && git pull --ff-only
mkdir -p ~/market-data
touch ~/market-data/env && chmod 600 ~/market-data/env
# the on/off switch listens only on the Tailscale address
TS=$(tailscale ip -4 2>/dev/null | head -1)
grep -q MARKET_BIND ~/market-data/env || echo "MARKET_BIND=${TS:-127.0.0.1}" >> ~/market-data/env
cp markets/markets.html ~/crew-web/markets.html
# keep the page current with the same 3-minute auto-update
grep -q "markets.html" ~/crew-update.sh || echo 'cp ~/starship/markets/markets.html ~/crew-web/markets.html' >> ~/crew-update.sh
sudo tee /etc/systemd/system/market-agent.service >/dev/null <<UNIT
[Unit]
Description=BTC 15-minute market agent (paper mode)
After=network-online.target
[Service]
User=$U
EnvironmentFile=-/home/$U/market-data/env
ExecStart=/usr/bin/python3 /home/$U/starship/markets/collector.py
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
sudo systemctl enable --now market-agent
sleep 25
systemctl is-active market-agent
ls -l ~/crew-web/market.json
echo "Open http://loveladymainaihub.taild703ca.ts.net:8095/markets.html"
