# Project tracker
One line per project. Status: idea / in progress / stalled / done. Finish what is started: when something stalls, say why and what unblocks it. Updated 2026-11-05 (daily check 06:20 Central). Nothing stalled over 3 days; everything here was started this week.

| Project | Status | Next step | File |
|---|---|---|---|
| Jarvis voice assistant (phone) | in progress | Truck test with the replay log; tune speed, hang-ups, voice ID | pi-home-assistant.md |
| Jarvis at home (Home Assistant speaker) | in progress | Add-on installed; Jarvis Hub integration added in Home Assistant (Kylar, 2026-11-05); test at home, then echo/false-wake fixes | pi-home-assistant.md |
| Shared memory (Claude, Jarvis, Pi) | in progress | Run for a week; daily Claude check to file inbox notes | README.md |
| Pi health and network | in progress | Net watchdog installed 2026-11-05; at-home tasks (router reservations, Pi-hole pilot) | pi-home-assistant.md |
| One site (Hub + Jarvis front door merged) | built, waiting on Pi | Overview tab in Hub (queue 016), /home redirects after pi_update | projects/field-deck.md (parts: projects/parts-inventory.md) |
| Starship control room page | in progress | 00:55 Captain panel shows top to-dos and 'waiting on you' (slice 1); next: a way to talk to the Captain (intake), the Captain as a scheduled agent, crew daily jobs. 23:50 FOUND AND FIXED the reason it would not load (a stray semicolon in the 15 s refresh line broke the whole script since the 02:49 change); Mission board now lists the projects (Jarvis, Kalshi, KDP, others; not truck or buy list) with live Kalshi wallet. Pi check 05:01 says :8095 is served and returns 200 with the latest index.html; if it still fails on Kylar's phone, suspect the device/Tailscale (server only listens on the Tailscale address). Cleanup of cluttered Hub tabs still to do. Rooms: captain, log, safe, monitors, filing, trash now real (needs Pi pull to confirm). Next: agent rows, meetings, gauges are still sample | pi-home-assistant.md |
| Kalshi practice agent | in progress | 21:20: first 4 sniper rounds all SKIP, no sellers 1 s before close (see kalshi-ai.md, Kylar to pick next step). $1K-Snipe v8.9 (sniper.py, own $1,000) pushed 20:15: after the Pi pulls, Kylar runs `python3 ~/starship/markets/sniper.py reset` then reads memory/inbox/snipe-autopsy.md; investigate each loss/miss. Data sync now automatic (tasks/kalshi_data_sync.sh); find any proven edge; mission starts AFTER Jarvis is complete (roadmap.md) | kalshi-ai.md |
| Amazon KDP | paused (waiting on review) | PAUSED 2026-11-05 23:28: navy and green in review, Kylar reports back. Series spec locked in tasks/kdp_series.json (23:30). Process Operator A and B in review; C burgundy, E orchid purple, then Lab Operator A/B/C/E to list. Book 1 (Process Operator A) IN REVIEW since 2026-11-05 21:46 at $18.99; next: Lab Operator A listing (same steps), then more colours after A is accepted. 8 notebook files built (look approved 2026-11-05); verify cover size with KDP calculator, write listings, Kylar uploads | amazon-kdp.md |
| Freeze-drying business | idea | Pick containers, label template | projects/freeze-drying.md |
| 3D printing | idea | Fill in details | projects/3d-printing.md |
| Cellular Wi-Fi unit for a buddy in Mexico (one-piece, plug-in, DIY) | planned | Kylar sends carrier, town, signal; then finalize parts (LTE module + Pi + antennas + 3D-printed case). Not a repeater | projects/cell-booster.md |
| Truck / vehicle projects | in progress | Pick first job per vehicle: Expedition sensors + radio, F-250 SIM + dyno tune | truck-project.md |
| Pi-hole (DNS blocking + device visibility) | in progress (pilot not started) | Confirm it answers; pilot on iPad then phones then TVs; name devices; feed stats into the status bus | architecture.md |
| Everything working together (tools for Jarvis, one alert channel, one front door, task queue, daily Claude check) | built, waiting for install on the Pi | Kylar runs `bash ~/starship/tasks/pi_update.sh ha`; then check alerts arrive and Jarvis tools answer | architecture.md |
| Home screen readability (clock/weather/date on busy backgrounds) | idea | Add a soft panel/shadow behind the clock | pi-home-assistant.md |
| Galaxy Note 20 Ultra (old phone) as a Starship device | idea | Options: Starship terminal (Tailscale + home-screen page), camera/sensor node feeding the Pi (and the Hailo-8), Jarvis satellite, test rig for the cell Wi-Fi unit. Kylar wants it as a Pi/Starship comms device and maybe an off-grid 'doomsday' comms unit (phone is AT&T, holds a charge). Plan: phase 1 Tailscale + Starship page terminal; phase 2 Meshtastic LoRa radio + offline maps/Wikipedia. Check if bootloader is locked (US Snapdragon = locked) before any Linux install | todo.md |

## Done
- 2026-11-05: Built Jarvis tools, alert channel, front door /home, task queue, daily Claude check, Kalshi digest (see changelog.md).
- 2026-11-05: Jarvis streaming replies, barge-in, truck mode, Lab, replay log, voice ID basics.
- 2026-11-05: Siri Shortcut door to Jarvis.
- 2026-11-05: Pi to repo notes sync.
