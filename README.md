# Starship Lovelady

The Control Room for the Lovelady AI Hub (a Raspberry Pi 5 at home). **Mission: progress and maintain the Pi and the AI voice assistant, and help with the Kalshi AI and other business ideas.**

| Folder / file | What it is |
|---|---|
| `index.html`, `support.js` | The Starship page (control room). Served from the Pi, auto-updated from this repo. Reads `status.json` (Pi health) and `hub-extra.json` (voice, markets, sync) from the Pi. Many crew-board rows are still sample text. |
| `voice/` | Jarvis, the phone voice assistant (`phone_voice.py`, the phone page, the Lab tuning page, voice recognition). See `voice/README.md`. |
| `markets/` | The Kalshi BTC practice agent (paper money only, live mode off), its review tools and phone pages. |
| `memory/` | Shared memory for Claude, Jarvis and Kylar, one topic per file. Start at `memory/README.md`. |
| `tasks/` | Scripts run on the Pi: setup, reviews, `status_report.sh` (health snapshot), `memory_sync.sh` (notes and status to the repo every 30 min), `pi_push_setup.sh`. |

Rules: no keys or passwords in this repo (it is public). Keys live on the Pi (`~/voice-data/keys.env`, `~/market-data/env`). Conversations never go in this repo.
