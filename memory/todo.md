# To do
Open items on top. When finished, move the line to Done with the date (never delete). Dropped items go to _archive.md.

## Open
- SAFETY (Kylar): F-250 pitman arm loose on the spline: torque to spec before driving; inspect front left noise. See truck-project.md.
- Jarvis reminders: one-time and repeating, spoken back at the time (build in voice server, store in voice-data, alerts via phone notify).
- KDP: pen name, one repeatable process from idea to upload, journals for plant jobs (amazon-kdp.md).
- Lovelady LLC: Claude proposes a structure for all business ideas (business.md).
- Kalshi: look up the take-profit option Kalshi offers after each trade and add it; new API key around Nov 9 (kalshi-ai.md).
- Satellite Pis for 3 bedrooms (family.md / pi-home-assistant.md).
- iPhone Shortcuts (added 2026-11-05 by Kylar): set up Siri Shortcuts for Jarvis and the Hub (e.g. "Hey Siri, Jarvis" opens/asks Jarvis, truck-mode shortcut, Hub and Starship on the home screen). Claude to list what to build, then give step-by-step taps.
- One site: after the next pull run `bash ~/starship/tasks/pi_update.sh` once (restarts Jarvis, needs the Pi password) so Jarvis /home redirects to the Hub; open http://loveladymainaihub:8081/hub and look at the new Overview tab. Tell Claude what else to fold in.
- Maker study found 0 rounds of tick data; Claude to check where the per-second ticks are stored.
- Home screen: confirm the frosted bubble looks right and the cursor line is gone (revert: copy index.html.bak-glass back in ~/hub-dashboard). Tell Claude if you want it bigger/smaller/clearer.
- Pi-hole: confirm it is answering, pilot on the iPad, then phones, then TVs; turn off Private Wi-Fi Address/Private Relay/VPN/Private DNS on devices; name the 11 unnamed devices; then feed its stats into Starship/Jarvis (see architecture.md).
- On the Pi: `cd ~/starship && git pull -q; bash ~/starship/tasks/pi_update.sh ha` (installs alerts, Kalshi sync, task queue, restarts Jarvis, installs the home-speaker add-on), then add the Jarvis Hub integration in Home Assistant (steps print at the end).
- 2026-11-09: redo Kalshi API location verification (kalshi.com Profile, API keys); do weekly.
- 2026-11-24 noon: ElevenLabs decision (renews Nov 26).
- Pi: confirm net watchdog installed; confirm home screen cursor line is gone.
- Jarvis: after update, test in the parked truck (page, Truck mode, barge-in), tag misses in /lab, enroll family voices, run pi_push_setup.sh; test Back Tap and the 6 s hands-free shortcut; try the web page wake word; later voice ID.
- Home screen: readability on busy backgrounds.
- Kalshi: review 12 h results in the morning.
- At home: unmute mic and test Hey Jarvis; switch Assist STT to OpenAI Whisper; router reservations; Pi-hole pilot (see pi-home-assistant.md).
- Empty the janitor trash (57 items, check the Hub first); encrypted off-Pi backups (destination undecided); check OpenAI key "Last used" dates.
- Tell Claude about the truck/vehicle projects so truck-project.md can be filled in.
- Starship: replace sample rows on the crew board/decision log with real data; make the HA speaker pipeline use shared memory (or route it through phone-voice); optional daily Claude check that files inbox notes and writes a morning brief.
- Run `bash ~/starship/tasks/memory_sync.sh` once after the update so pi-status.md appears in the repo.

## Done
- 2026-11-05: Network watchdog installed on the Pi (root cron every 2 min, log /var/log/net_watchdog.log, persistent journal). Confirmed by Kylar.
- 2026-11-05: Jarvis voice server live on the Pi with Brian voice, Siri Shortcut working.
- 2026-11-05: Shared memory split into topic files; Hub Notes migrated.
- 2026-11-05: Pi can push notes to the repo (deploy key) and syncs every 30 min.
- 2026-11-01: KDP identity verification.
- 2026-11-01: Bitwarden 2-step login and recovery code.
