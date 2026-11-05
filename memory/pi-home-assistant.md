# Pi, Home Assistant, Jarvis (voice)
Updated 2026-11-04. Imported from the old "Hub Notes" doc (kept as an untouched backup).

## The Pi and access
- Raspberry Pi 5 (8 GB), Raspberry Pi OS 13, hostname LoveladyMainAiHub (Tailscale name loveladymainaihub). Terminal: Easy SSH app on the phone (paste works), PowerShell `ssh` over Tailscale on the laptop. Termius expired Nov 1; Raspberry Pi Connect (connect.raspberrypi.com) is a backup.
- Repo ~/starship (GitHub kylarlovelady/Starship-Lovelady). Cron `crew-update` pulls about every 3 minutes, so starship/markets changes need no pasting.
- Pages over Tailscale: Hub http://loveladymainaihub.taild703ca.ts.net:8081/hub , Home Assistant :8123 (HA 2026.10.2, HACS), Markets/Live View :8095, Pi-hole :8089. Home screen kiosk: Chromium at http://localhost:8080 serving ~/crew-web/index.html (not in the repo).
- Pi services: hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-memsum (timer), hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog, hub-janitor (timer), plus market-agent and phone-voice. Docker: homeassistant, piper, whisper, openwakeword. Scripts in /usr/local/bin/hub-*.py. Case lights/OLED: /opt/pironman5.
- Working rules: commands in code boxes, one at a time (a multi-line paste once removed the whisper container); back up before changes; never put passwords or keys in chat or notes; mic stays muted until Kylar says.
- Hardening done: fail2ban, auto updates, two services closed. SSH still allows password login (fail2ban guards it). Bitwarden set up (2-step done Nov 1).

## Nov 4 events
- Pi's network dropped about 5:49-9:30 pm (no reboot, power OK, throttled=0x0). tasks/net_watchdog_setup.sh installs a watchdog and persistent logs (needs confirming it was installed).
- Home screen: added a no-cursor style/script (id="nocursor") to crew-web/index.html (backup index.html.bak). Kylar to confirm the cursor line is gone.
- TODO: make clock, weather and date readable on busy backgrounds (text shadow, dim layer, or panel).

## Home voice assistant (Alexa replacement)
- Pipeline (Assist pipeline "Jarvis"): wake word openWakeWord (Docker port 10400, threshold 0.7, hey_jarvis) -> Wyoming satellite -> speech-to-text (local Whisper now; switching to OpenAI Whisper/gpt-4o-transcribe) -> OpenAI Conversation gpt-4o-mini with the family prompt -> ElevenLabs voice Brian. Piper/Whisper local kept as fallback. Keep a copy of any prompt before editing.
- Problems: wakes by itself when unmuted (false wake words), talks over him, sometimes does not hear him, less smooth than Alexa. Likely causes: hears its own voice (needs echo cancellation), wake-word threshold/model. His partner is getting annoyed, so this is a priority at home.
- Hardware: MXL AC-44 USB boundary mic (poor fit, no echo cancellation as far as known), USB Pebble speaker. A Sonic XVF3800-class mic is the planned upgrade, only one, last, after checking echo handling. Later: custom wake word "Penelope" and a female voice; a push-to-talk button.
- Home Assistant has NO devices connected yet; Alexa still controls cameras, door locks, thermostat, air quality reader. Plan: add devices one at a time, keep Alexa until each works.
- What Kylar wants: knows him, his family and schedule; speaks only when asked; answers like Claude/ChatGPT; controls the house; good memory; blunt and honest; ignores the TV; never talks over him; sounds human.
- At home next: unmute and test Hey Jarvis; switch Assist STT to OpenAI Whisper; router address reservations (Pi 192.168.1.106; router 192.168.1.1, Advanced > Network > DHCP Server); turn off Private Wi-Fi Address, Private Relay, VPN, Private DNS on iPad/phones; name 11 unnamed devices; Pi-hole pilot on the iPad, then phones, then TVs; Hub Web Activity tab after that.
- Costs: OpenAI prepaid about $10-15 a month; ElevenLabs Starter $6 a month, renews Nov 26 (decision reminder Nov 24 noon). Two OpenAI keys and one ElevenLabs key exist; after a couple of days check each OpenAI key's "Last used" date at platform.openai.com and delete only the unused one.

## Jarvis on the phone (built Nov 4)
- Server voice/phone_voice.py, service `phone-voice` on 8099, https://loveladymainaihub.taild703ca.ts.net/ . Keys in ~/voice-data/keys.env (reused from Home Assistant). Voice Brian; transcription OpenAI; brain gpt-4o-mini; reads these memory files.
- iPhone Shortcut "Jarvis": Record audio -> POST https://.../ask (File body) -> Play Sound. Back Tap runs it. Tap-to-finish for long talk; a 6 s copy for hands-free Siri/car. Tested working Nov 4 (Brian understood Kylar well after switching to OpenAI transcription).
- Jarvis Lab (built Nov 4): https://loveladymainaihub.taild703ca.ts.net/lab shows transcripts with timings (hear/think/voice seconds), tag buttons (too slow, misheard, talked too long, said a word wrong, wrong answer, good), and sliders for talking speed, reply length, voice model (Flash fastest), plus a pronunciation list (Kylar = Kyler). `bash ~/starship/tasks/jarvis_review.sh` prints the same for pasting to Claude. Default replies now 1-3 sentences.
- Jarvis upgrades (built Nov 5, needs `cd ~/starship && git pull -q; sudo systemctl restart phone-voice`): replies stream sentence by sentence (faster first words); say "Hey Jarvis" while he talks to cut him off (barge-in) plus STOP TALKING button; Truck mode toggle on the phone page (big buttons only); Lab sliders for follow-up waits and end-of-speech pause; tuning tips in the Lab; basic voice recognition (Lab > Voices: record 20 s per person, set level owner/family/guest, "who is this?" test; weak for similar voices, labels only, NOT security); Jarvis is told who is talking.
- Notes sync: `bash ~/starship/tasks/pi_push_setup.sh` (run twice: makes a deploy key, add it on GitHub with write access, run again) installs a 30 min cron of tasks/memory_sync.sh. It pushes only topic notes and a feedback summary (counts, timings, tags), never transcripts (repo is public).
- Jarvis replay log (Nov 5): every turn is traced (state changes, your recording length/loudness/noise, what he heard, each sentence he said with timings, phone play start/end, hang-up reason). Lab > "Replay for Claude" > Copy, then paste to Claude; or `bash ~/starship/tasks/jarvis_review.sh`. Hang-up fixes: blank/noisy recording no longer ends the chat (3 in a row does), clicks under 0.35 s ignored, waits 25 s / 40 s, errors keep the chat open, "never mind/goodbye" only counts in short phrases, 0.9 s echo guard after he speaks.
- MISSION (Kylar, 2026-11-05): "Progressing and maintaining the Pi and the AI voice assistant, and also helping with the Kalshi AI and other business ideas." The Starship page Mission board now shows this and live rows from hub-extra.json (written by tasks/status_report.sh every 30 min with the notes sync).
- Reality check (2026-11-05): the Starship "crew" (Captain, Security, Mechanic, Librarian, Trainer) is a visual control room. Real parts: status.json (Pi health, from the Pi's hub scripts), hub-extra.json (voice, markets, sync), the hub-* services, market-agent, phone-voice. The crew board rows, decision log, safe, trash and rule book are still sample text. Nothing autonomous reads memory and acts except Jarvis (answers) and the markets agent; Claude acts when asked.
- Memory flow: Claude <-> repo memory/ (Claude pulls/pushes); Jarvis (phone-voice) reads repo memory on the Pi and writes notes to inbox; Pi pushes inbox + pi-status.md every 30 min. GAPS: the Home Assistant speaker pipeline ("Jarvis" in HA) has its own prompt and does NOT read this memory; a new Claude chat only knows the memory if told to read memory/README.md; markets results reach memory only when Claude writes them.
- One Jarvis (built 2026-11-05, NOT yet installed/tested): ha/custom_components/jarvis_hub is a Home Assistant conversation agent that sends the speaker's words to phone-voice /ask, so home and phone share brain, memory, notes and commands. Install: `bash ~/starship/tasks/ha_jarvis_install.sh`, then add the "Jarvis Hub" integration and pick it as the Conversation agent in the Jarvis voice assistant (old agent stays as a fallback).
- Jarvis memory commands (phone page and Shortcut): "remember that ...", "mark ... done" (kept with date, nothing deleted), "forget ..." (moves to archive).
- Known issues Nov 4: Shortcut path is slow (fixed 3-6 s recording + full-file voice) and Play Sound cannot be stopped mid-answer. The web page has a big STOP TALKING button and follow-ups without re-triggering; best option for the truck, but the screen must stay on (CarPlay/Maps can background Safari).
- Web page (wake word hey jarvis) built, untested on the phone. iPhone web pages can't listen when the screen is locked.
- Wanted but not built: voice ID with "who am I speaking with?" and trust levels (family voices; strangers get nothing important), reply only to the device that heard the voice, AirPods/home-mic direction, echo cancellation, wake-word trigger log with good/false marks (built in the web page).
- Phone mode rule: replies play on the phone/AirPods only, never the home speakers.

## Starship / Control Room
- Control Room is live in the Lovelady Hub (Status, Appearance, Control Room tabs). Ideas: real data in popups, more life aboard, test live mode on the phone. Portrait rooms are small; landscape is best.

## Other
- Janitor: moves files to ~/.janitor/trash (57 items); empty around Nov 2 if nothing broke; 5 .bak files need sudo. Device names live in ~/hub-dashboard/device-names.json (key = MAC). ntfy pushes never reach the iPhone; plan: Home Assistant Companion app notifications (Pushover as fallback).
- Phone/iPad location tracking dropped. Phone/iPad wifi connect/disconnect alerts stay off.

## Done
(Finished items go here with the date, newest first. Never delete.)
