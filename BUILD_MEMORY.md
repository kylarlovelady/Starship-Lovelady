# Build memory (read this first in any new session)

Owner: Kylar ("Kyler"), America/Chicago, iPhone. Pi 5 "LoveladyMainAiHub". Shell via Easy SSH app (tmux). Sends screenshots/recordings. Wants action, no repeated risk warnings ("its my money and i know my risks"). Keep API keys/tokens out of chat and GitHub.

## Pi
- Repo: kylarlovelady/Starship-Lovelady, on Pi at ~/starship. Pi pulls via cron `crew-update` (~3 min).
- Chromium kiosk: `--app=http://localhost:8080` (home screen). Home Assistant in ~/homeassistant (HACS installed). Tailscale name: loveladymainaihub.taild703ca.ts.net.
- Home screen themes: NOT in this repo and no ~/homeassistant/www or themes dir. Likely served from ~/crew-web (support.js found there). Open issue: text-cursor line appears next to clock when going full screen (Nov 4). Not yet fixed; find the theme file first.
- Sandbox cannot reach the Pi or PyPI; Kylar runs commands and sends screenshots.

## Markets (Kalshi 15-min BTC, practice money only, live mode OFF)
- See markets/PLAN.md. Service `market-agent` runs collector.py; it restarts itself only when collector.py changes (bump the "# vN restart" marker on line 2). Data in ~/market-data.
- Live View: http://loveladymainaihub.taild703ca.ts.net:8095/live.html ; control server port 8097.
- Rules: BTC only; nothing taken off the table (no strategy/signal retired); only hard rules are $5 minimum bet and no selling a winner unless profit >= $5 after fees; loss cuts are flexible (size, time left, distance to target).
- Honest status: no signal has beaten price + fees yet. Check tasks/verify.sh output and markets/review.py.
- Cron: crew-update, market-lab (every 3 h), supervisor hourly (also runs innovate.py).

## Voice assistant (voice/, README there)
- Built Nov 4: web page on phone (Add to Home Screen, screen on, charging), served by Tailscale HTTPS; service `phone-voice` port 8099; data ~/voice-data.
- Setup: `bash ~/starship/tasks/voice_setup.sh`. Wake-word model installed OK on Nov 4. Still waiting on OpenAI + ElevenLabs keys (Kylar must create new keys: platform.openai.com/api-keys, elevenlabs.io profile > API Keys; stored only in ~/voice-data/keys.env).
- Not built: voice ID/trust levels, AirPods/home-mic direction, echo cancellation, home speaker routing. iPhone web page cannot listen while locked.

## Dates
- KDP identity verification before Nov 8. Kalshi API location check by Nov 9. ElevenLabs renewal Nov 24.
