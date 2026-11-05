# Changelog: what Claude did (newest first)
Claude adds an entry every time it changes something, so any conversation, Jarvis, or Kylar can see the history. Format: date, what, where, status (built / tested here / installed on Pi / confirmed by Kylar).

## 2026-11-05 (daily check, 06:20 Central)
- Read repo memory and inbox. No Jarvis voice notes to file (0 note files). Pi snapshot (pi-status.md, 06:00 sync, 20 min old): all services active, no failed units, 40.6C, disk 9%, no throttling; containers up (Pi-hole up 10 h, Home Assistant up 4 h). Jarvis last 24 h: 71 turns, 0 errors, first words avg 1.6 s (slowest 4.2 s), 9 hang-ups by you, 2 by quiet timeout; 0 voices enrolled. Kalshi data fresh to 04:19 (practice only, live OFF); digest shows most strategies positive over 24 h but the 05:07 report shows a bad last 4 rounds for the top ones. Queue 018: Starship page on :8095 is up and serves 200. Nothing in todo.md dated today or tomorrow. Wrote memory/brief.md and updated projects.md. Status: memory only, nothing run on the Pi.

## 2026-11-05 (13:25)
- CONFIRMED on the Pi (queue 023): collector v8.4 running; run wallet now uses v_hold (autolog 12:54: no strategy proven over 80+ rounds, holds to the end); the 12:45 round staked $24.91, so the $25 cap works. Next: watch 24 h of rounds, then the maker-entry test.

## 2026-11-05 (13:05)
- Kalshi run wallet found hopping between lucky v_x variants every 15 min (that is why it lost while v_hold won). sim.py auto_pick: hold-to-end default, a variant must beat it 1.5x over 80+ rounds, 6 h minimum dwell; collector marker v8.4 (agent restarts after next pull). Tested with fake data. Status: pushed, not yet seen on the Pi.

## 2026-11-05 (12:50)
- Full Kalshi review (queues 019-022 read from the Pi), recorded in kalshi-ai.md. Found and fixed a bug: saved default unproven_cap 50 in collector.py was overriding the 25 cap (v8.3). Fixed maker_study.py (it read the wrong price field and used 0 rounds; now 69 rounds). Looked up Kalshi's auto sell / take profit. Status: pushed, Pi pulls and restarts the agent itself.

## 2026-11-05 (04:35)
- Added to todo.md: Pi home pages cluttered; Starship page not loading.

## 2026-11-05 (04:30)
- Filed Kylar's answers: PE pellets (100 lb per shift), KDP under Lovelady LLC with a 1-hour target, how he wants Kalshi help and phone-only alerts, what Jarvis must do to replace Alexa and the build order (pi-home-assistant.md), new open items.

## 2026-11-05 (04:10)
- Corrected Kylar's shift schedule (4 nights, 3 off, 3 nights, 4 days, 7 off) and the plastic note (he buys poly pellets from his employer, free to use).

## 2026-11-05 (04:00)
- Filed Kylar's answers: live-trading plan and API key (kalshi-ai.md), family and work schedule and Jarvis access (family.md), business order, LLC, plastic idea (business.md), KDP plan (amazon-kdp.md), vehicle priorities and the pitman-arm safety note (truck-project.md), new open items (todo.md).

## 2026-11-05 (03:45)
- truck-project.md: recorded the F-150 goal (street legal daily to work, max power, no engine or trans swap).

## 2026-11-05 (03:40)
- truck-project.md: confirmed F-250 is a 6.7 Power Stroke and the white 2003 F-150 is a 5.4.

## 2026-11-05 (03:30)
- Filled memory/truck-project.md from Kylar's message: the 2020 F-250, Sheree's 2022 Expedition and the 2003 F-150, with open jobs. Flagged two things to confirm (F-250 engine, F-150 engine).

## 2026-11-05 (03:10)
- CONFIRMED on the Pi (queue 017): Overview tab added to the Hub page (first, default). Queue 016 was refused because its comment contained the word sudo; renamed to 017. Still to confirm by eye: Kylar opens :8081/hub.

## 2026-11-05 (03:05)
- Kylar ran pi_update.sh (restart Jarvis OK). Added "iPhone Shortcuts" to todo.md Open.

## 2026-11-05 (03:30)
- Safe now shows real money: real Kalshi cash (read-only from the agent, unknown while Kalshi is in maintenance), practice wallet balance/profit, Jarvis usage. OpenAI dollar spend still not measured. (crew_report.py wallet block + index.html.)
- ONE SITE: the Lovelady Hub (:8081/hub) is now the single website. Queue 016 adds an Overview tab (first, default) to Hub that embeds the Jarvis front door (/home?embed=1: right-now chips incl. wallets, alerts, Jarvis/Lab/Replay/Pi-hole/HA/KDP links, notes viewer). Duplicates removed from it (Starship, Live View, Hub tiles, services chip; those are Hub tabs). Visiting Jarvis /home directly now redirects to the Hub (/home?old=1 keeps the old page). /api/hub also returns crew.json. Needs: pull, `sudo` restart of phone-voice (bash ~/starship/tasks/pi_update.sh) and queue 016 (auto). hub.html backup: hub.html.bak-merge. Status: built, not yet on Pi.
- Maker study (014) ran but found 0 rounds: no recorded per-second ticks in ~/market-data for the last 3 days (check the tick file names/location before trusting it).

## 2026-11-05 (03:10)
- Kalshi changes (commit d5c60bc): unproven-strategy cap $50 to $25; Auto wallet only trusts a strategy with 40+ rounds and a positive record, otherwise holds; collector marker v8.2 (agent restarts on next Pi pull; Kalshi is in maintenance until 5 am ET, practice only); read-only maker-vs-taker study (markets/maker_study.py, queue 014, result not read yet). Status: pushed, not yet confirmed on Pi.
- Crew changes: new tasks/crew_report.py (run by alerts_check every 5 min) writes crew.json plus copies hub-extra.json and hub-alerts.json into ~/crew-web (fixes the 404 bug, the page is served from there). index.html now shows real data for Decision log (from this changelog), Captain, Safe (Jarvis usage; dollar spend is NOT tracked yet), Bookshelf, Filing, Trash, Monitor wall Pi health and Threat view. Falls back to sample text if the files are missing. Agent rows, meetings, gauges, weak spots, training board are still sample. Status: tested here, not yet on Pi.

## 2026-11-05 (02:45)
- Kalshi review (12 h, 24 h, learned files, signal grades, stake check) read from the Pi through the queue and recorded in kalshi-ai.md with recommendations (waiting for Kylar's go). Confirmed the $50 cap holds. Jarvis Hub integration in Home Assistant confirmed done by Kylar.
- Found the real URLs: Starship page is :8095 (not :8080, which is the home-screen clock). Fixed the /home front door tile and pi-home-assistant.md.

## 2026-11-05 (02:24)
- Network watchdog INSTALLED on the Pi (confirmed by Kylar's screenshot): checks internet every 2 min, restarts NetworkManager after 3 fails and tailscaled after 6, logs to /var/log/net_watchdog.log, persistent journal on. Moved to Done in todo.md.

## 2026-11-05 (late night, home screen)
- Found where the home screen lives: ~/hub-dashboard (server.py on 127.0.0.1:8080, page index.html with #clock, #date, #wx; theme in theme.html + settings.json), NOT the repo's index.html. crew-update.sh copies the repo index.html over ~/crew-web/index.html every 3 minutes, which also wiped the earlier no-cursor edit (that was applied to the wrong file).
- Built tasks/queue/007-glass-bubble.sh: frosted-glass bubble behind clock/date/weather (iOS look, tint adapts to dark or light text), no text caret, backups *.bak-glass, safe to run twice; "glass": false in settings.json turns it off. Tested here on a mock page with a busy background. Status: APPLIED on the Pi 02:22 (queue confirmed patched index.html and theme.html, screen asked to reload); waiting for Kylar to confirm how it looks.
- Dropped by Kylar: GitHub 2-step reminder (moved to _archive.md).

## 2026-11-05 (late night, second queue run)
- CONFIRMED on the Pi: Jarvis waits now 25 s / 40 s / 1.3 s (the old saved values are replaced); Home Assistant loaded the jarvis_hub add-on (shows in its log); Pi-hole is Core v6.5, Web v6.6.1, FTL v6.8 (needs its password for stats: tasks/pihole_key.sh); Kalshi agent running practice (run.json active, strategy set), market-data about 190 MB, disk 9%. No trace.jsonl yet: no page conversations since the replay log was added, so the truck retest is still the real test.
- Still open: Kylar adds the "Jarvis Hub" integration in Home Assistant and selects it as the conversation agent (2 taps each); run tasks/pihole_key.sh (optional).

## 2026-11-05 (late night, after first queue run)
- Task queue CONFIRMED working end to end (Pi ran 001-diagnose.sh and sent results back). Real findings: Pi-hole runs in Docker with the v6 API (needs a password to read stats; tasks/pihole_key.sh stores it on the Pi only); Home Assistant is on host network (URL 127.0.0.1:8099 is right); Jarvis tools answered "how is the Pi" correctly from live data; first words averaged 1.7 s over 4 chats; crontab has crew-update, market-watchdog/supervisor/lab, memory sync, alerts, Kalshi sync, queue.
- Found: Jarvis's saved settings.json still held the OLD waits (silence 1.0 s, 10 s, 20 s), overriding my new defaults, so the hang-up fix was not in effect. 002-fix-settings.sh sets 1.3 / 25 / 40.
- Fixed: markets file path is ~/crew-web/market.json (alerts and status were looking in the wrong place); live mode read from run.json; containers (pihole, homeassistant, whisper, piper, openwakeword) now watched by alerts instead of a non-existent pihole-FTL service; Pi-hole v6 login in Jarvis tools.

## 2026-11-05 (late night, install)
- Kylar ran tasks/pi_update.sh ha: alert checker, Kalshi daily sync, task queue installed and notes sync ran (CONFIRMED by his screenshot). Home-speaker add-on copy failed: ~/homeassistant is root-owned (Docker); installer now uses sudo for the copy. First task-queue script (tasks/queue/001-diagnose.sh) pushed to check Pi-hole, HA network mode, crontab and Jarvis tools; results land in memory/inbox/queue-results.md.

## 2026-11-05 (night): making everything work together
- Jarvis tools (voice/tools.py): live facts pulled in when asked (Pi status, Kalshi agent, Pi-hole, what Claude changed) and spoken device control for lights, switches and fans via Home Assistant (locks and doors deliberately excluded). Works on phone page, Shortcut, and home speaker. Status: built, tested here with a fake Home Assistant; needs install on Pi (pi_update.sh); uses HA_TOKEN already in ~/market-data/env.
- One alert channel (tasks/alerts_check.py, every 5 min): services down, Pi hot/full, Kalshi data stale, Jarvis errors, Pi-hole down, stuck repo pull, and dated to-dos (lines starting "- YYYY-MM-DD" in memory/todo.md Open). Phone alert through Home Assistant, re-alert every 6 h, "Cleared" message, shows on Starship Mission board and Security light. Status: built, tested here; needs install on Pi.
- Front door page (voice/home.html at https://loveladymainaihub.taild703ca.ts.net/home): status chips, links to Starship, Jarvis, Lab, Live View, Hub, Pi-hole, Home Assistant, and a viewer for the memory files. Status: built, tested here.
- Task queue (tasks/queue/, tasks/queue_runner.sh): Claude leaves a script, the Pi runs it once and writes output to memory/inbox/queue-results.md. Guards: header check, deny list (speed bump, not a sandbox), no sudo, 5 min limit, kill switch ~/queue.off. Status: built, tested here; needs install; keep GitHub 2-step login on.
- Daily Claude check (scheduled task, 6:17 am Central): files inbox notes, flags problems, updates projects.md, writes memory/brief.md and a changelog entry. Status: created; first run 2026-11-05 6:17 am Central; auto-approval mode.
- Kalshi into memory: daily digest (memory/inbox/kalshi-digest.md) and data coverage (kalshi-data-status.md) from tasks/kalshi_data_sync.sh. Status: built; needs install.
- Pi-hole stats added to status snapshot, Jarvis, Starship and front door (shows "did not answer" if its API needs a login; then Claude needs the exact Pi-hole version).
- tasks/pi_update.sh: one command to install all of the above on the Pi.

## 2026-11-05 (evening)
- Rules: finished items stay under "## Done" (never deleted); memory/projects.md tracker; memory/roadmap.md (Mission 1 Pi + voice, Mission 2 Kalshi betting help); CLAUDE.md so every attached conversation follows the same rules; architecture.md. Jarvis learned "mark ... done" and memory commands now work on the voice page too.
- Home speaker uses the same Jarvis: ha/custom_components/jarvis_hub + tasks/ha_jarvis_install.sh. Status: built, untested on real Home Assistant, not installed.
- Kalshi daily data sync (tasks/kalshi_data_sync.sh).
- Status snapshot (tasks/status_report.sh -> memory/inbox/pi-status.md and hub-extra.json), Starship Mission board with the real mission, README refresh.
- Jarvis replay log (/report, Lab "Replay for Claude") and hang-up fixes (blank/noise no longer ends the chat, longer waits, echo guard). Status: built, tested with fake mic; Kylar saw hanging up before the fix; needs truck retest.
- Pi can push notes to the repo (deploy key, memory_sync every 30 min). Status: confirmed working by Kylar's output.

## 2026-11-04
- Voice server on the Pi (Brian voice, OpenAI transcription), Siri Shortcut, streaming replies, barge-in, truck mode, Lab, voice recognition basics, shared memory split into topic files, Hub Notes migrated, net watchdog script, markets review and $50 cap. See pi-home-assistant.md and kalshi-ai.md.
