# Project tracker
One line per project. Status: idea / in progress / stalled / done. Finish what is started: when something stalls, say why and what unblocks it. Updated 2026-11-05 (daily check 06:20 Central). Nothing stalled over 3 days; everything here was started this week.

| Project | Status | Next step | File |
|---|---|---|---|
| Jarvis voice assistant (phone) | in progress | Truck test with the replay log; tune speed, hang-ups, voice ID | pi-home-assistant.md |
| Jarvis at home (Home Assistant speaker) | in progress | Add-on installed; Jarvis Hub integration added in Home Assistant (Kylar, 2026-11-05); test at home, then echo/false-wake fixes | pi-home-assistant.md |
| Shared memory (Claude, Jarvis, Pi) | in progress | Run for a week; daily Claude check to file inbox notes | README.md |
| Pi health and network | in progress | Net watchdog installed 2026-11-05; at-home tasks (router reservations, Pi-hole pilot) | pi-home-assistant.md |
| One site (Hub + Jarvis front door merged) | built, waiting on Pi | Overview tab in Hub (queue 016), /home redirects after pi_update | todo.md |
| Starship control room page | in progress | Pi check 05:01 says :8095 is served and returns 200 with the latest index.html; if it still fails on Kylar's phone, suspect the device/Tailscale (server only listens on the Tailscale address). Cleanup of cluttered Hub tabs still to do. Rooms: captain, log, safe, monitors, filing, trash now real (needs Pi pull to confirm). Next: agent rows, meetings, gauges are still sample | pi-home-assistant.md |
| Kalshi practice agent | in progress | 21:20: first 4 sniper rounds all SKIP, no sellers 1 s before close (see kalshi-ai.md, Kylar to pick next step). $1K-Snipe v8.9 (sniper.py, own $1,000) pushed 20:15: after the Pi pulls, Kylar runs `python3 ~/starship/markets/sniper.py reset` then reads memory/inbox/snipe-autopsy.md; investigate each loss/miss. Data sync now automatic (tasks/kalshi_data_sync.sh); find any proven edge; mission starts AFTER Jarvis is complete (roadmap.md) | kalshi-ai.md |
| Amazon KDP | in progress | Book 1 uploaded; new owner page built 21:16, re-upload interior.pdf, approve, price. 8 notebook files built (look approved 2026-11-05); verify cover size with KDP calculator, write listings, Kylar uploads | amazon-kdp.md |
| Freeze-drying business | idea | Pick containers, label template | projects/freeze-drying.md |
| 3D printing | idea | Fill in details | projects/3d-printing.md |
| Truck / vehicle projects | in progress | Pick first job per vehicle: Expedition sensors + radio, F-250 SIM + dyno tune | truck-project.md |
| Pi-hole (DNS blocking + device visibility) | in progress (pilot not started) | Confirm it answers; pilot on iPad then phones then TVs; name devices; feed stats into the status bus | architecture.md |
| Everything working together (tools for Jarvis, one alert channel, one front door, task queue, daily Claude check) | built, waiting for install on the Pi | Kylar runs `bash ~/starship/tasks/pi_update.sh ha`; then check alerts arrive and Jarvis tools answer | architecture.md |
| Home screen readability (clock/weather/date on busy backgrounds) | idea | Add a soft panel/shadow behind the clock | pi-home-assistant.md |

## Done
- 2026-11-05: Built Jarvis tools, alert channel, front door /home, task queue, daily Claude check, Kalshi digest (see changelog.md).
- 2026-11-05: Jarvis streaming replies, barge-in, truck mode, Lab, replay log, voice ID basics.
- 2026-11-05: Siri Shortcut door to Jarvis.
- 2026-11-05: Pi to repo notes sync.
