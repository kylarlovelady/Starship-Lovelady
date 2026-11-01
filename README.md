# Starship Lovelady
The Control Room page for the Lovelady AI Hub. Served from the Pi; auto-updated from this repo.

## markets/
BTC 15-minute call engine (paper mode only, never places orders) and its phone page.
`collector.py` runs on the Pi as the `market-agent` service and writes `market.json`; `markets.html` shows it.
`setup.sh` installs it. Optional key goes in `~/market-data/env` as `WHALE_ALERT_KEY=...` (never commit keys).
