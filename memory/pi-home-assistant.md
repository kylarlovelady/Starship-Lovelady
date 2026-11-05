# Pi, Home Assistant, Jarvis (voice)
Updated 2026-11-04.
- Hardware: Raspberry Pi 5 (8 GB), Raspberry Pi OS 13, hostname LoveladyMainAiHub. Kylar uses the Easy SSH app (phone) or PowerShell `ssh` over Tailscale (laptop).
- Repo on the Pi: ~/starship. Cron `crew-update` pulls it about every 3 minutes. Home screen page: ~/crew-web/index.html (Chromium kiosk at http://localhost:8080). Not stored in the repo.
- Tailscale: machine name loveladymainaihub, HTTPS certificates enabled 2026-11-04. Voice page: https://loveladymainaihub.taild703ca.ts.net/
- 2026-11-04: Pi's network dropped about 5:49-9:30 pm (no reboot, power OK). tasks/net_watchdog_setup.sh installs a watchdog and persistent logs.
- Home screen fix 2026-11-04: added a no-cursor style/script (id="nocursor") to crew-web/index.html (backup index.html.bak).
- TODO: make the clock, weather and date easier to read on busy backgrounds (shadow, dim layer, or panel).

## Jarvis (voice assistant)
- Server: voice/phone_voice.py, service `phone-voice` on port 8099. Keys live in ~/voice-data/keys.env on the Pi (reused from Home Assistant). Voice: ElevenLabs "Brian". Transcription: OpenAI. Brain: gpt-4o-mini.
- iPhone Shortcut "Jarvis": Record audio -> POST https://.../ask (File body) -> Play Sound. Back Tap runs it. Tap-to-finish for long talk; a 6 s hands-free duplicate for Siri/car.
- Web page version (wake word "hey jarvis") built but not tested on the phone yet. iPhone web pages cannot listen with the screen locked.
- Not built: voice ID, AirPods/home-mic direction, echo cancellation, home-speaker routing.
- Kylar wants to use Jarvis in the car, hands-free only.
