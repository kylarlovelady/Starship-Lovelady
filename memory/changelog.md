# Changelog: what Claude did (newest first)

## 2026-11-09 10:37 KDP last page changed: blank page, tiny centred LOVELADY LLC (built, waiting on Pi)
- tasks/kdp_owner.py: last page is now plain white (no lines, no page number) with LOVELADY LLC small and grey, centred near the bottom. Tested on a dummy PDF. Queue 104 will build it when the Pi is back online.

## 2026-11-09 10:22 Home Wi-Fi outage (Kylar at work)
- Pi silent since its 09:00 sync (no 09:30 or 10:00 sync, queue 104 not picked up). Kylar says the Wi-Fi went out again. Queue 104 (KDP rebuild) is in the repo and will run by itself within a few minutes of the Pi coming back online; no action needed. Kalshi practice agent cannot reach Kalshi while the line is down, so expect a gap in its rounds. Status: waiting on the internet.

## 2026-11-09 09:30 KDP: Lovelady LLC off the back cover, small on the last page (queued, waiting on Pi)
- tasks/kdp_build.py: back-cover text removed. tasks/kdp_owner.py: tiny grey LOVELADY LLC on the last interior page, bottom right on the page-number line (tested on a dummy PDF). Queue 104 rebuilds all 8 books and copies cover.pdf, interior.pdf and a last-page preview into memory/inbox/kdp-preview/<slug>/. The KDP author field stays Lovelady LLC (tasks/kdp_series.json) unless Kylar says otherwise. Live Process Operator books need the new cover and interior re-uploaded at KDP (goes back through review).

## 2026-11-09 06:25 Daily check (filed, pushed)
- Read all inbox files; Pi healthy, all services active, notes sync fresh (06:00). Filed take-profit, longshot and maker study results into kalshi-ai.md. Updated projects.md (KDP unblocked, Kalshi API key due today) and wrote brief.md. Flags: Kalshi snapshot/sim files last written ~04:00 (agent alive); nothing stalled over 3 days. No Pi or Kalshi actions taken.

## 2026-11-09 04:30 Notes from Kylar's morning voice drive filed (built, pushed)
- kalshi-ai.md (overnight result, design rules, jobs owed), business.md (case-selling idea), projects/3d-printing.md (hinge failure, support settings, recipe), todo.md (Starship rework, crew plan), amazon-kdp.md (all four colours live), projects.md rows. Queue 103 result read.

- 2026-11-09 04:08 Claude: queued tasks/queue/103-kalshi-wallet-curve-overnight.sh (rerun of 102) to get the overnight Kalshi breakdown for Kylar. Status: queued, result lands in memory/inbox/kalshi-wallet-curve.md.

## 2026-11-08 20:42 Kalshi: Kylar's sizing rule and plan filed
- memory/kalshi-ai.md: bigger bets when signals agree, smaller when weak; check the $5 vs ~$480 rounds against signal agreement. Plan: run tonight, new API key Mon Nov 9, then adjustments. Live OFF.

## 2026-11-08 20:45 Kalshi swing explained (Kylar asked)
- Read queue 102 output; summary filed in memory/kalshi-ai.md ("Big wallet swing explained"). v_hold_s500 peaked +$6,103 at 4:30 PM, now +$2,783; driven by cheap-side ~16c bets of ~$472 (2 wins +$4,282, 7 losses -$500 each since 3 PM). Live OFF. Kylar will move back to voice chat.

## 2026-11-08 Kalshi: wallet curve tool + queued job 102 (Kylar asked what the big wallet did)
- markets/wallet_curve.py (read-only): replays one practice strategy round by round from trades.jsonl (profit, peak, worst drop, latest rounds, by entry price/side/hour). Queue job 102 runs it for v_hold_s500 and v_hold_s100; output lands in memory/inbox/queue-results.md. Live stays OFF.
- Pi status 19:07 showed v_hold_s500 +4784 over 130 rounds, -490 over the last 4 rounds.

## 2026-11-08 Kitchen case: pry grooves on the doors (Kylar: no way to grab a door)
- 7 mm round vertical groove (z 12..26) across the seam at each door's free end, half in the door and half in the wall, so a screwdriver tip or fingernail can pry the door out once the 2 latch screws are out. 50 checks pass, plates/viewer/zips rebuilt.

## 2026-11-08 Kitchen case: stud height measured (3.6 mm), plates rebuilt
- so_h 3 -> 3.6 mm (photo of the stud edge-on against the tape). Tab screws M2.5 x 4 reach 2.4 mm into the studs. make_plates.py added (rebuilds plates/ from stl_slim). Plates, viewer, zips regenerated; 50 checks pass. Open: stud thread size (assumed M2.5, test with one screw).

## 2026-11-08 Kitchen case: screen mount holes corrected from the real screen
- Measured on Kylar's screen (photos with tape): black back plate 235 x 142 mm, 4 gold studs (identical, two under the kickstand brackets), centres 4 mm in from each edge, so 227 x 134 mm apart. Model had 6/7/5 mm; set to 4/4/4 (case.mjs P.holeX/holeTop/holeBot). Verify passes (50 on slim). Still unknown: stud height (3 mm assumed) and thread size (M2.5 assumed). Plate STLs not rebuilt yet; rebuild after stud height is known.

## 2026-11-08 Kitchen case: 4 ready-to-print plate files (Kylar chose grouped prints, no auto-eject)
- hardware/kitchen-screen-case/v6/plates/: plate1 body_left+door_A (hinge test first), plate2 body_right+door_C+door_B, plate3 faceplate_left, plate4 faceplate_right+feet. Faceplates flipped face-down; volumes checked against originals. Kylar has Bambu Studio on his Windows desktop; slicing there. Pi slicer route parked; auto-eject idea parked (big ASA parts, risk to toolhead).

## 2026-11-08 Kitchen case: cord exit moved to the RIGHT side (Kylar)
- 8 mm slot now through the bottom wall under the right bay (x 125.5..133.5); cord crosses the case along the bottom behind the Pi (y -58..-50, 7 mm high), checks pass. Old left slot removed.

## 2026-11-08 Kitchen case: single power cord exit added (slim final)
- 8 mm cord slot through the bottom wall under the left bay (x -133.5..-125.5); cord runs down the left wing from the Pi USB-C. Checks added and pass (48 on slim). Case fits the 12 in cubby (290 mm wide incl. doors); side doors can't swing in place, lift off keyholes to open. Pi slicer probe result: Pi 5 aarch64, no slicer installed, prusa-slicer apt available (needs sudo, asked Kylar to run it).

## 2026-11-08 Queued Pi probe 101-slicer-probe.sh
- Kylar wants prints sliced on the Pi and sent to his Bambu printer (AMS, ASA in slot A3). Probe checks slicer options and finds the printer on the LAN. Result lands in memory/inbox/queue-results.md. Printer LAN access code stays on the Pi, never in the repo.

## 2026-11-08 Kitchen screen case: FINAL = 38 mm slim build (Kylar chose thinner)
- Bare Pi 5 + Active Cooler on 4 plate posts, no kit case. Vent path: door B + door C slots in, 4 plate grille slots, 6 top louvers out (added one). 46 checks pass, 8 meshes watertight.
- Print set zip now holds stl_slim parts. Viewer opens on 38 mm. 49 mm kept as an unused option. Check Pi temp after a day.

## 2026-11-08 Kitchen screen case v6: screw holes matched to the bought screws
- Faceplate M2.5 x 10 (20), seam bolts M2.5 x 16 (4, pilot in right half), screen-tab M2.5 x 4 (4, counterbore deepened), hinge pins M3x30 (3). Verified by volume checks on both builds, all pass; meshes watertight.
- Files: hardware/kitchen-screen-case/v6 (case.mjs, verify.mjs, viewer.html, PRINT-NOTES.txt, zip), blueprint.png. Status: ready to print; dry fit Nov 10 still to confirm standoff height 3 mm, hole positions, HDMI chain.
Claude adds an entry every time it changes something, so any conversation, Jarvis, or Kylar can see the history. Format: date, what, where, status (built / tested here / installed on Pi / confirmed by Kylar).

## 2026-11-08 Kitchen screen case v6 final (Pi stays in its kit case)
- Kylar: slimmer was wanted, but the Pi stays in its kit case, taped inside (to the screen back by default). So STANDARD 49 mm is the print set (hardware/kitchen-screen-case/v6/stl, zip in the same folder). A 38 mm bare-Pi build exists in v6/stl_slim (optional, unused).
- Review fixes: hinge holes were drawn as radius instead of diameter (knuckle walls were 1 mm and the pin would not bite): now r4.5 knuckles, 2.8 mm wall, pin threads into a 2.7 mm tapped bottom knuckle, head recessed in knuckle and faceplate. Door latch holes did not line up with the faceplate screws: fixed, all 20 screws verified to have wall around them. Mesh micro-slivers cleaned: all parts watertight.
- Status: built and checked here; NOT yet printed. Next: dry fit Nov 10, hinge test print (door A + left half).

## 2026-11-08 Kitchen screen case v6 (print-ready files, 3D viewer, CAD pipeline)
- What: new generator (hardware/cad-kit/csg.mjs + hardware/kitchen-screen-case/v6/case.mjs) replaces the uncompiled SCAD (moved to old/). Outputs watertight STLs in v6/stl: body left/right halves (split so any bed over 160 mm works), faceplate halves, doors A/B/C, feet. Faceplate screws on (20 x M2.5 x 12), doors hinge on vertical M3 x 30 pins hidden under the faceplate, symmetric 18 mm side bays, corner tabs hold the screen (v5 posts were 34 mm tall and could not be reached by a 12 mm screw: fixed).
- Checks (v6/verify.mjs): doors swing clear 0 to 110 deg, screen/Pi/speakers/driver board/USB-C plug fit, all meshes watertight. Open: HDMI adapter + straight plug needs about 50 mm, bay gives 36 to 37 (maybe buy a short flexible right-angle HDMI extension); screw hole positions, standoff height (3 mm assumed), Pi case size are estimates until the Nov 10 dry fit.
- Also: interactive 3D viewer (v6/viewer.html, published as an artifact), blueprint.png v6, cad-kit README + example + generic STL viewer (view.mjs), queue jobs 099-cad-setup.sh (Pi Python CAD toolbox) and 100-build-case-v6.sh (rebuild and check on the Pi). Cart: supply swapped to SANOOV 27W $10.99; subtotal $245.64.
- Status: built and checked here; NOT yet printed or dry-fitted.

## 2026-11-08 Kitchen screen case v5
- Screw-on front faceplate (8 black M2.5 x 12), two hinged side/bottom doors (M3 x 30 hinge pins), 6 mm walls, vents kept (top slots, fan grille, speaker slots, door intake). Buy: 6-pack angled HDMI adapter, Kernmax M2.5 screw kit. Status: draft, NOT test-compiled; print one hinge first; door B position depends on the Nov 10 dry fit.

## 2026-11-08 Cable routing for the kitchen screen
- USB-C up, HDMI down along the edge; pocket 18 mm and taller. Status: dry fit pending.

## 2026-11-08 Kitchen screen case v4
- Thin symmetric frame, no cable bay, Pi kit case taped behind. Status: draft, dry fit needed.

## 2026-11-08 Kitchen screen case v3
- Fixed v2 flaw (pod floated case off the wall), cable fit review, vents and speaker slots; added 90 degree HDMI adapter to buy list. Status: draft, dry fit needed.

## 2026-11-08 Kitchen screen case v2
- Rebuilt around the maker's real dimensions and port layout (hardware/kitchen-screen-case). Added screw assortment to buy list. Status: draft, needs ruler check of mounting holes and a test print.

## 2026-11-08 Kitchen screen case draft
- Added hardware/kitchen-screen-case (scad + blueprint). Status: draft, needs screen measurements and a test print; OpenSCAD compile not checked.

## 2026-11-08 Room satellite plan noted
- Pi Zero 2 W judged fine as audio-only satellites; mic quality is the real issue. Filed in pi-home-assistant.md.

## 2026-11-08 Buy list: kitchen screen parts
- Added Pi 5 4GB kit, 27W supply/charger, microSD, short cables. Prices not yet checked. Status: waiting on Kylar's outlet/cable answers.

## 2026-11-08 Living room: kitchen screen plan
- Wrote Plan A/B for the GeekPi touch screen at the key holder (living-room-build.md). Status: waiting on outlet/cable answers.

## 2026-11-08 Starship zoomed rooms: removed stray agents and candle
- Removed the three agents queued outside the Captain's Office door and the agents/Captain seated in the Conference Room chairs in the zoomed-in room view (agents live in their own rooms). Removed the wall candle that sat on the Screen saver board. Status: pushed, page loads with no errors.

## 2026-11-08 Starship video review (Kylar's screen recording)
- Fixed: closing a board (e.g. Screen saver editor) also opened the Crew achievements board under it (tap fell through to the room). Taps are now ignored while a board or pane is open and for half a second after closing.
- Fixed: ghosting double image while zooming into a room (room layer fade window made much shorter).
- Seen in the video, still open (filed in todo.md): clock and mic chip cover wall boards when zoomed; hit highlight box is a plain rectangle that clips; crew-achievements and other boards still show sample data; candle overlaps Screen saver board; tiny text in the editor preview; sprites cut off at the door when zoomed. Status: first two fixed and pushed.

## 2026-11-08 Daily Claude check (06:20 Central)
- What: read inbox (no new Jarvis notes; wake report, home mic report, Kalshi digest and snipe autopsy already recorded), Pi status green and fresh (sync 06:00), queue 098 ran (wake threshold now 0.8). Refreshed projects.md, wrote brief.md. Nothing due today; API location check is due tomorrow. Pi untouched, no orders placed.
- Status: pushed to main (see git log).

## 2026-11-07 Daily Claude check (06:20 Central)
- What: read inbox (no new Jarvis notes; studies and status files already recorded), Pi status all green and fresh (sync 06:00), nothing due today or tomorrow. Added the $1K-Snipe update to kalshi-ai.md, refreshed projects.md, wrote brief.md. Pi untouched, no orders placed.
- Status: pushed to main.

## 2026-11-08 8 AM check: Kalshi results, Jarvis threshold 0.8 live
- Queue resumed after the lock heal; queue 098 set wake threshold 0.8 at 23:07 (no false wake-ups overnight, versus 6 at 2-4 AM before). Kalshi: see memory/kalshi-ai.md Update 2026-11-08. No agent changes today.

## 2026-11-07 Task queue stuck since 12:40: found and healed
- Cause: queue 097 started the Jarvis mic switch from inside the queue, so it inherited the queue's lock (/tmp/queue.lock) and every later script (098 wake threshold 0.7 -> 0.8) never ran. The mic switch itself kept working. Fix: tasks/crew_report.py (runs from cron every 5 min) stops that process once; cron keep-alive restarts it cleanly; tasks/jarvis_install.sh no longer starts it itself. Status: pushed; queue should resume within about 8 min. Threshold is still 0.7 until 098 runs. Backup if still stuck: Kylar runs `pkill -f jarvis_mic.py` on the Pi.

## 2026-11-07 Buy list: living room and Pi items added
- memory/buy-list.md (6 rows, all 'not decided yet'). Status: pushed.

## 2026-11-07 Living room build project started
- What: memory/projects/living-room-build.md (room layout from Kylar's photo, rules, parts research, wiring plan, open questions), projects.md row, todo.md. Status: planning only, nothing bought.

## 2026-11-07 Home Jarvis install confirmed on the Pi; wake threshold 0.7 -> 0.8 (queue 098)
- What: queue 097 installed the mic switch (port 8098 listening) and watcher; first report: 21 wake-ups in 7 days, 14 false (6 at 2-4 AM). Queue 098 raises the threshold to 0.8 with automatic restore. Status: queued; result to be read at the 4 PM review.

## 2026-11-07 Home Jarvis: mic switch on the Starship, false wake-up watcher, wake sensitivity tuner
- What: tasks/jarvis_mic.py (web switch on Pi port 8098, tailnet/home Wi-Fi only; mute, unmute, mute 1 h / 4 h / until 8 AM; uses the existing ~/hub-dashboard/muted file that hub-mic.py, the OLED and the lights already honour); tasks/jarvis_watch.py (every 5 min: labels each wake-up from audio stats as empty / us talking / real command, writes ~/crew-web/jarvis-wake.json and memory/inbox/jarvis-wake-report.md); tasks/jarvis_tune.sh (changes the openwakeword --threshold between 0.55 and 0.92, restores on failure, logs); tasks/jarvis_install.sh + queue 097 (cron keep-alive). Starship: a small JARVIS MIC chip under the clock (green = listening, red = muted, tap to open) and a Jarvis mic tab first on the Workshop Control board (and Security Office Pi Watch) with big Mute/Unmute and the false wake-up numbers.
- Findings (queues 095/096): wake word model openWakeWord threshold 0.7 in Docker; mic via hub-mic.py; only 21 wake clips recorded in about 2 days; satellite restarts by itself if killed.
- Status: tested here in a browser with a local copy of the switch. NOT on the Pi until queue 097 runs (about 6 min after push). The tuner has never been run on the Pi.

## 2026-11-07 Kalshi results and decision: hold to the end on the main wallet (queue 094), v9.8
- What: 72 h review and take-profit backtest read (details in memory/kalshi-ai.md Plan 2026-11-07). Selling at +25% loses vs holding. Main practice wallet switched to v_hold by queue 094; two later-entry hold tests added; marker v9.8. Live OFF.
- Status: pushed; runs on the Pi within minutes. 8 PM and 8 AM checks scheduled.

## 2026-11-07 Kalshi agent v9.5: take-profit and bet-size practice tests (Kylar's ideas), restart; checks scheduled 8 PM and 8 AM
- What: markets/sim.py new setting TAKE_PCT (sell the whole bet once it is up X% after fees) and 4 take-profit tests (v_take15, v_take25, v_take40, v_take25_cheap) plus 11 flat bet-size tests ($5,10,25,50,100,250,500 per round on hold-to-end: v_hold_s*; $10,50,250,500 on sell-at-+25%: v_take25_s*; new setting FLAT_BET, restart marker v9.6); markets/collector.py restart marker v9.5; markets/take_profit_study.py (backtest, queue 092) and queue 091 (72 h and 7 day review). Also (10:25, Kylar): sell-at-different-percent tests v_take5/10/20/30/50/75/100 and a wider backtest (queue 093). Marker v9.7. Live trading stays OFF.
- Status: pushed; the Pi restarts market-agent when it pulls. Results come from queue 091/092 and the daily digest.

## 2026-11-07 Kalshi board opens on the old full betting page; voice-call plans filed
- What: index.html (tab order: Betting page (full) first), memory/todo.md (STARSHIP NEXT). Status: pushed.

## 2026-11-06 Added todo: full room-by-room Starship bug pass
- What: memory/todo.md and projects.md next step (Kylar asked 23:22). Status: queued, not started.

## 2026-11-06 Starship boards with tabs: Kalshi (Training Room), Screen saver editor (Captain), Pi Watch (Security), Control board (Workshop); tap fix
- What: index.html. Clicking those wall boards opens a full panel with tabs. KALSHI (Training Room wall): Overview, Strategies, Lessons (real numbers from market.json), Full dashboard (live.html), Project notes (tasks/crew_report.py now copies memory/kalshi-ai.md to ~/crew-web/kalshi-notes.md), Voice training. SCREEN SAVER (new board, Captain's Office, back wall): Layout and Look editors from the Hub, plus notes. PI WATCH (Security Office monitor wall): Pi health, Alerts, Devices, Family activity, Voice assistant. CONTROL BOARD (Workshop services rack): service lights, Hub controls, Janitor, Memory.
- Zoom bug fixed: the room insides were redrawn every 1.4 s, which could swallow a tap on a phone; taps are now read on release. Crossfade between ship and room is shorter (less ghosting). Touch callout and tap highlight off.
- Status: tested here (phone size, boards open, no script errors). Hub tabs (iframes) cannot be tested from here; Kylar to confirm. Goes live on the Pi within ~5 min of the push.

## 2026-11-06 Starship rebuilt as one endless space (v1: sky, zoom, drag, clock, meteors, intro)
- What: index.html. Removed the TABS ship, the header text and the isolated room view. Added an endless starfield you can drag (mouse, touch, arrow keys) and zoom (wheel, pinch, + / -; 0 or double-click = fit). Zoomed all the way out the ship is a speck; zooming in brings it to the middle, and rooms open up in place with their clickable items. 12-hour Orbitron clock in a frosted bubble (top right). Meteor on the hour, comet at :30, shooting star at :15 and :45, random spots. First visit per session: THE STARSHIP fades in, holds 3 s, fades out, ship flies in.
- Hub pages (Network, Janitor, Memory, Layout, Look, Markets, Activity) open as a full-screen panel from room items (Esc or X closes). Control board and read-only Hub status are NOT done yet.
- Status: tested here in a browser (drag, zoom, room items, fly-to, no script errors). Not on the Pi/phone yet; goes live when crew-web copies it.
- Not done: Pi screen saver (frosted bubble and quiet-spot placement), Hub merge/control board.

## 2026-11-06 Friendly Pi-hole activity page built (12-hour time, plain-English names, per device)
- What: tasks/pihole_activity.py reads Pi-hole's database and writes ~/crew-web/activity.html (about 250 known sites/apps in tasks/pihole_names.json, unknown ones listed at the bottom for Claude to name). crew_report.py refreshes it every 5 minutes. Page is on the tailnet only: http://loveladymainaihub.taild703ca.ts.net:8095/activity.html . PRIVACY: browsing history is never written into this public repo.
- Not done yet: alerts per app, delete a device's history, blocking for Warren's iPad (todo.md).
- Status: pushed; queue 090 builds the first copy.

## 2026-11-06 Alert phone set on the Pi: only mobile_app_kylars_phone (Sharee's phone is mobile_app_sharees_iphone, not used by our alerts)
- Done by Kylar running markets/ha_phones.py set. Where: ~/market-data/alert_phone.txt on the Pi (not in repo).
- Status: done; Kylar to say if Sharee still gets anything (then it is a Home Assistant automation).

## 2026-11-06 Alerts fixed: Kylar's phone only, and only Pi problems (Kylar: Sharee was getting project notifications, too many)
- What: markets/alerts.py sends only to alert_phone.txt or HA_LIVE_DEVICE (Kylar's iPhone), never anyone else, and sends to nobody if neither is set. Kalshi/market alerts are muted (logged to alerts.log; turn back on with ~/market-data/market_alerts.on). tasks/alerts_check.py pushes only Pi problems (service down, hot, disk full, container down, repo not pulling); to-do reminders, 'cleared' notices, Kalshi-data-stale and Jarvis-error notes stay on the Starship page only. collector.py marker v9.4 restarts the agent to load it.
- Not touched: Home Assistant's own automations (Blink, thermostat) that notify her; those stay as they are.
- Status: pushed; takes effect when the Pi pulls (about 3 min).

## 2026-11-06 To-do added: friendly Pi-hole activity view (12-hour time, plain-English site names)
- Where: memory/todo.md
- Status: planned; notifications fix is first.

## 2026-11-06 Queue 089 was refused (the queue never reads key files). Replaced by markets/ha_phones.py that Kylar runs himself on the Pi
- Status: waiting for Kylar to run it and name his phone.

## 2026-11-06 Alerts to Kylar's phone only (Kylar: Sharee must not get notifications)
- What: markets/alerts.py now sends only to phones listed in ~/market-data/alert_phone.txt (if the file exists); queue 089 lists the phones and which automations notify, to pick Kylar's. Not active until the file is written and the agent restarts.
- Status: step 1 of 2.

## 2026-11-06 Device names written into Pi-hole's client table (queue 088)
- Result: pi-hub .107, kylar-iphone .142, sharee-iphone .228, warren-ipad .240, living-room-tv .130; DNS restarted and listening. Note: .106 (second Pi address) has no name.
- Status: done; Kylar to confirm on the dashboard.

## 2026-11-06 Queue 088: force Pi-hole to show the device names (dashboard still showed addresses after 087)
- Where: tasks/queue/088-pihole-names-refresh.sh. Restarts Pi-hole DNS for a few seconds.
- Status: queued.

## 2026-11-06 Naming devices in Pi-hole (queue 087)
- What: iPad found at 192.168.1.240; sets names pi-hub, kylar-iphone, sharee-iphone, warren-ipad, living-room-tv as local DNS names. Where: tasks/queue/087-pihole-names.sh, memory/home-network.md.
- Status: queued.

## 2026-11-06 Queue 086: retry of 085 (the Pi-hole container has no sqlite3; now uses pihole-FTL sqlite3). dns.hosts is empty, so no names are set yet.
- Status: queued.

## 2026-11-06 Queue 085: list Pi-hole devices (read-only) to find the iPad address, before naming devices
- Where: tasks/queue/085-pihole-clients.sh; result lands in memory/inbox/queue-results.md
- Status: queued; next script sets names (kylar-iphone .142, sharee-iphone .228, living-room-tv .130, warren-ipad).

## 2026-11-06 To-do added: Pi-hole per-device history, log delete, site/app alerts
- Where: memory/todo.md (Open)
- Status: plan written, not built.

## 2026-11-06 Business idea filed: coop cam livestream with donate-to-feed
- Where: memory/projects/coop-cam-stream.md (new), one line in memory/business.md, a row in memory/projects.md.
- Status: idea.

## 2026-11-06 To-do added: Starship mouse navigation on desktop/laptop
- Where: memory/todo.md (Open)
- Status: not started.

## 2026-11-06 TV cleanup notes, iPad DNS set, one-step-at-a-time rule
- What: CLAUDE.md now says give one step at a time (Kylar asked by voice); TV cleanup recorded in home-network.md; iPad DNS saved, Pi-hole shows 5 clients, 648 blocked (5.4%).
- Status: iPad address to confirm.

## 2026-11-06 Pi-hole: living room Sony Google TV connected
- What: static IP 192.168.1.130, gateway 192.168.1.1, DNS 192.168.1.107; shows in Pi-hole (4 clients, 419 blocked, 3.8%).
- Where: memory/home-network.md
- Status: done. Next: iPad, other 3 TVs after Pi hardening.

## 2026-11-06 Home network address list saved
- What: memory/home-network.md with the Pi and phone addresses for reference; living room TV rollout started.
- Status: done; add iPad and TV addresses as we go.

## 2026-11-06 Pi-hole: Sharee's phone connected and blocking
- What: Sharee's iPhone (192.168.1.228) uses Pi-hole; 3 clients, 331 blocked (3.1%) after about 25 min. mask.icloud.com is blocked on purpose (Pi-hole's way of telling Apple to turn Private Relay off on this network).
- Where: memory/pi-home-assistant.md
- Status: phones done. Next: iPad. TVs and router only after Pi hardening (todo.md).

## 2026-11-06 Pi-hole: Kylar's iPhone confirmed blocking (with Tailscale ON)
- What: 44 blocked in first test; cnn.com ad/tracker domains (tremorhub, rubiconproject, pubmatic) blocked for 192.168.1.142 with Tailscale on. Normal sites load.
- Where: memory/pi-home-assistant.md
- Status: done for iPhone. Next: Sharee's phone, iPad, 4 TVs after Pi hardening items.

## 2026-11-06 15:45 Pi-hole: first device connected; hardening note filed
- What: Kylar's iPhone (192.168.1.142) now queries Pi-hole (confirmed by his Network table screenshot). Filed HARDEN THE PI in todo.md (power, NVMe boot, Ethernet instead of Wi-Fi, auto-restart watchdog, backup DNS, one reserved address, reboot test). Noted the Pi has two addresses on wlan0.
- Status: phone connected; blocking test next, then Tailscale back on with DNS check, then Sharee's phone.

## 2026-11-06 16:35 15-minute markets study read; made it accumulate nightly (queue 084)
- What: read inbox/market-catalog.md (9 coins x 280 rounds). Findings in projects/kalshi-15m-markets.md: alts are decided 1 to 4 points earlier than BTC but are thin (BTC 36 to 1,000x deeper) and calibrated; round-to-round memory and BTC lead/lag look interesting but are the same rounds repeated in every series. Rewrote series_catalog.py to cache every round (history/series15m.jsonl) and added tasks/series_catalog_daily.sh (cron 4:40 am) and tasks/lag1_btc.py (lag-1 check on about 2,800 BTC rounds).
- Status: queue 084 installs the cron and starts the 14-day catch-up now. BTC-only rule unchanged.

## 2026-11-06 16:00 All 15-minute markets catalogued; predictability study queued (083)
- What: new memory/projects/kalshi-15m-markets.md lists every 15-minute crypto series found; new markets/series_catalog.py (read-only) pulls each series' settled rounds and 1-minute candles and compares favourite-right rate, Brier score, spreads, volume, round-to-round memory, calibration and BTC lead/lag; queued as 083 (runs about 30 min in the background, then syncs).
- Status: queued; BTC-only rule unchanged (this is data only).

## 2026-11-06 15:55 Forward tests read: longshot rejected, maker inconclusive
- What: queue 082 (450 rounds): longshot rule has no edge (ranges span zero, older half positive and newer half negative). Queue 081: every maker order skipped because the spread is under 2c; only 28 rounds have a tape. Notes in kalshi-ai.md.
- Status: nothing changed in the agent. Next: maker study v3 (post at the bid with queue position) once 150+ rounds have a tape.

## 2026-11-06 15:40 Pricing study read; maker study fixed; longshot test queued (081, 082)
- What: queue 078 (implied volatility, calibration, spreads) ran and is summarised in kalshi-ai.md (market implies about 12 to 18% less volatility than realized from 2 to 10 min out; cheap side under 20c won more than priced at 3 to 7 min out in this sample). Queue 080 failed with a MemoryError; maker_study2.py now keeps only the first 5 minutes of each round and runs as 081. New markets/longshot_wf.py tests the longshot idea with bootstrap range, older/newer halves and per-day results (queue 082).
- Status: 081 and 082 queued; practice only, nothing changes in the agent.

## 2026-11-06 15:10 More ideas, stricter maker study, wallet back to Auto (queues 079, 080)
- What: researched fees (taker 7%, maker 1.75%, rounded up per trade), the Volume Incentive Program, cross-venue arbitrage and an arxiv market-making paper; ideas listed in kalshi-ai.md. Wrote markets/maker_study2.py (fills need a real tape trade). Queue 077 showed the practice wallet still followed v_snipe, so queue 079 sets run.json strategy back to auto (backup kept; live untouched).
- Status: queued (078, 079, 080); results to memory/inbox/ and queue-results.md.

## 2026-11-06 14:50 Kalshi reverse-engineering research + pricing study (queue 078)
- What: searched GitHub, Kalshi help and contract terms; notes in kalshi-ai.md. Wrote markets/implied_vol_study.py (implied vs realized volatility by time left, calibration by price bucket, spreads) and queued it as 078.
- Status: queued; results to memory/inbox/implied-vol-study.md.

## 2026-11-06 14:25 Sniper switched OFF; back to experimenting (Kylar's call)
- What: markets/sniper.py now only runs when the file ~/market-data/sniper.on exists (it does not, so no new sniper bets); its settle thread still settles any open bet; all its files and the reports are kept. collector.py marker bumped to v9.3 so the Pi restarts the agent after the next pull. Queue 077 reads run.json and review.py to see what the experiments are doing.
- Why: after 72 rounds it bet 3 times (3 wins, wallet $1,219 practice) because nobody sells the winning side near the close; Kylar chose to go back to testing all strategies side by side.
- Status: pushed; the Pi restarts the agent itself after its next pull.

## 2026-11-06 14:10 Kalshi series probe queued (076)
- What: read-only probe of which short-term crypto series Kalshi lists and how liquid they are (idea: the sniper only gets about 3 bets per 72 BTC rounds, so more series would mean more bets).
- Status: queued.

## 2026-11-06 14:00 To-do added: Pi screen saver
- What: added 'fix the Pi screen saver' to memory/todo.md Open (details still needed from Kylar).
- Status: noted, not started.

## 2026-11-06 13:55 Pi-hole work started (at home)
- What: queued tasks/queue/075-pihole-check.sh (read-only: container, DNS answering, blocking test). Plan: confirm it answers, reserve the Pi address at the router, pilot on the iPad only, then phones, then TVs.
- Status: queued; results in memory/inbox/queue-results.md.

## 2026-11-06 13:40 Desktop workstation set up
- What: Kylar's Windows desktop now has Git, GitHub CLI, VS Code and Tailscale (Tailscale sign-in still to do), is signed in as kylarlovelady and cloned to C:\Users\<user>\Starship-Lovelady. Commits use the GitHub noreply address; pull.rebase and rebase.autoStash are on. First test push (memory/inbox/desktop-test.md, commit f46ee82) arrived in the repo.
- Status: confirmed working. Next: Tailscale sign-in, open the repo in VS Code, optional Claude on the desktop.

## 2026-11-06 06:20 Daily check (Claude, scheduled)
- What: read the inbox (no new Jarvis notes; the study files are already filed in kalshi-ai.md), pi-status (06:00 sync, fresh), Kalshi digest and sniper autopsy. Pi healthy: all services active, 39.5 C, disk 10%, Pi rebooted about 3 h before the snapshot (uptime 2 h 45 min, matches the earlier oracle-study load). Jarvis quiet overnight (0 turns, last use 16 h ago). Sniper wallet $1070.26 (2 bought, 2 won, rest skipped because nothing was for sale). No home-mic clips yet. Pi-hole stats still blank (needs tasks/pihole_key.sh). Wrote memory/brief.md and refreshed the projects.md header.
- Status: filed, nothing stalled over 3 days.

## 2026-11-06 06:15 Voice notes saved
- What: wrote the whole voice chat into the repo: projects/field-deck.md (decisions, module list, doomsday kit, repair plan), new projects/offline-brain.md, family.md (home West Columbia, work Clute), 3d-printing.md (ASA note).
- Status: filed. Open: model number, DeWalt/alligator-clip supply photo, ham license yes/no, separate doomsday radios or built in.

## 2026-11-06 04:55 Field Deck plan expanded
- What: field-deck.md now has the 25 to 50 mile mesh goal, Alexa devices, Qi/magnet charging idea and a build order; new projects/parts-inventory.md for photo-identified parts.
- Status: waiting on Kylar's model number, terrain/range target, 3D printer, charger details and part photos.

## 2026-11-06 04:40 Starship Field Deck project filed
- What: new memory/projects/field-deck.md (Note 20 Ultra + mesh radio + Linux terminal + module case); projects.md row now points to it.
- Status: idea, waiting on model number, mesh range need and 3D printer answer.

## 2026-11-06 04:25 Note 20 Ultra plan
- What: Kylar's phone is AT&T, holds a charge; he wants a Starship comms terminal and maybe an off-grid comms unit. Plan filed in projects.md (phase 1 Tailscale terminal, phase 2 Meshtastic + offline kit).
- Status: waiting for Kylar to install Tailscale on it.

## 2026-11-06 04:00 Oracle study result + Note 20 Ultra idea filed
- What: read oracle-study.md (300 rounds); no proven signal yet, details in kalshi-ai.md. Filed the Galaxy Note 20 Ultra repurpose idea in projects.md and todo.md.
- Status: study done; walk-forward test is the next step.

## 2026-11-06 03:20 Oracle study made memory-light (rerun queued as 073)
- Why: the Pi rebooted (uptime 0 minutes in the 03:00 snapshot) right as the first run (queue 071) started. I cannot prove the study caused it, but it loaded every recorded second into memory, so I rewrote it to keep only the needed numbers, default 3 days, and queue 073 caps it at 2 GB and lowest priority.
- Status: queued.

## 2026-11-06 02:55 Hindsight/oracle study (practice only, read-only)
- What: new markets/oracle_study.py finds the best possible buy in every recorded round and tests which signals (distance to strike, momentum, Kraken lead, trade flow, order-book imbalance, Kalshi price) predicted the winner at 6 checkpoints, split older/newer half; plus a simple z-vs-ask edge rule after fees. Queued as tasks/queue/071-oracle-study.sh; output memory/inbox/oracle-study.md.
- Status: queued, waiting for the Pi's next run (Kylar asked whether the best trades share signals).

## 2026-11-06 AI accelerator check (benchmark: 283 FPS, 1.8 W, works; no camera attached): Hailo-8 is installed, healthy and idle (queue 068); it only accelerates camera vision, not Jarvis voice or Kalshi. Findings in pi-home-assistant.md; queue 069 checks for a camera and benchmarks the chip.

## 2026-11-05 (daily check, 06:20 Central)
- 2026-11-06 00:55 Starship Captain slice 1: the Captain panel (Captain's Office) now shows the top 5 open to-dos and what is waiting on Kylar, read from memory/todo.md by tasks/crew_report.py every 5 min (crew.json: todo_top, waiting_on_kylar), on top of the open-alerts/changes rows. Page script re-checked (compiles). NOT yet built: Captain as a running agent, a text box to talk to the Captain, crew daily jobs (architecture.md build order).
- 2026-11-06 00:45 Sniper v9.2: the 00:00 'MISSED' round was a bookkeeping glitch (the book DID answer at 0.97 s, then a second process logged MISSED); two agent processes overlap briefly after a restart. Fix: markets/sniper.py claims each round once across processes (snipe_claims/ marker files), so no double bets or false MISSED. z-rule is working: round 01:30 reached z=4.1 at 144 s but nothing was for sale under 98.5c (Z_NOBUY); round 01:15 reached z=68 at 1.4 s with nothing to buy.
- 2026-11-06 00:45 Home screen pop-up font: index.html applies the chosen font (Great Vibes) to the whole page via body; queue 067 adds #you,#ai,.lbl rule with the normal font (backup index.html.bak-popupfont). Refresh the home screen after it runs.
- 2026-11-06 00:30 todo.md: moved finished items (Starship loading fix, tick data location, Kalshi 12 h review) to Done; added the four live items (sniper, KDP review, cell Wi-Fi unit, Starship build order).
- 2026-11-06 00:14 Cell Wi-Fi unit #1 facts filed (Verizon, truck/house/work, no new SIM on his plan): SIM options, Verizon certification need, truck power and expectation notes in memory/projects/cell-booster.md.
- 2026-11-06 00:10 Cell Wi-Fi unit: Kylar wants to build unit #1 for himself (US) first, then one for the buddy in Mexico; open questions for unit #1 added to memory/projects/cell-booster.md.
- 2026-11-06 00:08 Cell booster project: Kylar approved the one-piece plug-in cellular Wi-Fi unit; build plan (parts, software, placement, open questions) written in memory/projects/cell-booster.md; waiting on the buddy's carrier/town/signal before choosing parts.
- 2026-11-05 23:46 Filed Kylar's new project: build (not buy) a cellular booster for a buddy: memory/projects/cell-booster.md plus a row in projects.md. Status: idea; open questions and the legal note (no homemade amplifier in the US, passive antenna route is fine) are in the file.
- 2026-11-05 23:50 Starship: (1) FIXED the page that would not load: index.html had `this.pullExtra(); this.pullCrew()` with a semicolon inside a parenthesised setInterval (added 02:49 in e3e5e37), a syntax error that stopped the whole script; now compiles and renders in a headless browser. (2) New projects board: tasks/projects_board.py reads memory/projects.md (skips truck and buy list), adds the live $1K-Snipe wallet, writes a `projects` list into hub-extra.json; the Mission board (Captain's Office) shows the rows. crew_report.py (every 5 min) runs it and now also copies index.html into ~/crew-web so page fixes reach :8095 without a manual step. Verified by queue 064.
- 2026-11-05 23:35 Kalshi v9.1: sniper logs ROUND (max z per round) and Z_NOBUY (z-rule attempts that did not buy, with reason); autopsy shows z-rule stats. Collector marker bumped; Pi restarts itself. Rules unchanged.
- 2026-11-05 23:28 KDP paused at 2 books (navy A, green B in review) until Kylar reports the review result; notes in amazon-kdp.md and projects.md.
- 2026-11-05 23:30 KDP series locked: new tasks/kdp_series.json (colours, titles, lettering, price, settings, description + keywords) read by kdp_build.py; new tasks/kdp_listing.py prints paste-ready listing text per title; kdp_build sizes the title by its longer line, has --check and scheme-letter partial builds. Checked on the Pi by queue 063. Documented in amazon-kdp.md.
- 2026-11-05 23:20 KDP: scheme E espresso replaced by orchid purple #5B2A6E (Kylar picked option 1 of 6 mockups); kdp_build.py takes scheme letters for partial builds; built process-operator-e and lab-operator-e (queue 062) with the refined owner page.
- 2026-11-05 22:40 Pi sync fix: the Pi's pulls kept failing silently because it rewrites tracked report files (snipe-autopsy.md every ~5 min) and a pull with local edits is refused; memory_sync.sh now pulls with --autostash, and Kylar sets git config --global rebase.autoStash true once on the Pi so every cron pull is safe. This was why queue jobs and the z-rule deploy lagged.
- 2026-11-05 22:25 KDP: Process Operator B (forest green) submitted, In review, $18.99. Next C and E covers (queue 061).
- 2026-11-05 22:20 KDP: replaced the guessed keywords in amazon-kdp.md with the exact 7 Kylar entered (from his screenshot), including Blue collar gifts for women.
- 2026-11-05 22:10 KDP: saved the reusable description, keywords and listing settings in amazon-kdp.md (Reusable listing text) for every colour and title.
- 2026-11-05 21:46 KDP: Process Operator A hardcover submitted by Kylar, status In review, $18.99. Notes in amazon-kdp.md (Done section) and projects.md.
- 2026-11-05 21:35 Kalshi v9.0: close study (queue 058) found Kalshi never closes early; the book just empties a median 90 s before the close. Added the z-rule (buy at z>=4 while still for sale at <=98.5c) to sniper.py, collector marker v9.0. Tested on synthetic books. Status: pushed, Pi restarts itself; Kylar to confirm bets appear.
- 2026-11-05 21:20 Kalshi: first sniper rounds all SKIP (no sellers one second before close; favourite asked at $1.00); liquidity study (queue 056/057) over 268 rounds confirms it. Findings in kalshi-ai.md; options put to Kylar. KDP: owner page refined on all 8 interiors by queue 055/057 (kdp_owner.py); Process Operator A interior.pdf rebuilt 21:16 on the Pi, Kylar to re-download and re-upload.
- 2026-11-05 20:58 KDP: owner page redesigned (Kylar: the old one looked cheap and too big). New tasks/kdp_owner.py: small centred letter-spaced serif heading, short rule, quiet grey field labels with hairlines, tiny return line; post-processes each book's interior.pdf page 1 (original kept as interior-orig.pdf). Tested locally on a stand-in page. Queue 055 applies it to all 8 books on the Pi. Status: pushed; Kylar re-downloads interior.pdf and re-uploads it for Process Operator A.
- 2026-11-05 20:15 Kalshi v8.9, $1K-Snipe rebuilt as Kylar specified (his 20:02 complaint: it bet $25 with lots of time left). Causes: (1) collector main() forced the run wallet back to Auto on every restart, (2) the sim steps every 5 s so it could never hit a 1-second window. Fix: new markets/sniper.py, practice only, own pretend $1,000 (snipe.json), own clock, reads Kalshi's live order book about 4x/second in the last 9 s and the market status every second; bets the WHOLE wallet on the favourite on the first fresh book with 1.3 s or less to go, sweeping book levels up to 99c (unfilled part stays cash), holds to the result; logs every BOUGHT/SKIP/MISSED/WON/LOST to snipe_log.jsonl with seconds left and Kalshi answer time. Removed v_snipe_all from sim.py; collector no longer forces Auto; snipe_autopsy.py rewritten to read the sniper log. Reset: python3 ~/starship/markets/sniper.py reset. Status: pushed, awaiting Pi pull + restart.
- 2026-11-05 20:35 Added tasks/snipe_autopsy.py (loss post-mortems for $1K-Snipe and v_snipe, run from crew_report.py every ~5 min -> memory/inbox/snipe-autopsy.md). Tested on synthetic data locally; real output appears after the first losing round on the Pi.
- 2026-11-05 20:20 Renamed the all-in sniping test's display name to "$1K-Snipe" (key v_snipe_all unchanged so data stays linked); collector marker v8.8.
- 2026-11-05 20:15 avg_lock_study ran (queue 053): inconclusive, only 19 usable rounds; findings in kalshi-ai.md. Plan: rerun after 24-48 h of new data.
- 2026-11-05 20:25 Kalshi v8.7: added practice-only v_snipe_all (whole wallet on the favourite, last 15 s, hold; ALL_IN + CAP overrides in sim.py), collector marker bumped; syntax-checked and unit-tested size()/stage(). Status: pushed, awaiting Pi pull + restart and first rounds. Live mode untouched (OFF).
- 2026-11-05 20:10 Recorder v8.6: new per-second 'ks' field = Kalshi market STATUS, close/expiration times, can_close_early, early_close_condition and prices for the current market and the just-ended one (120 s after), to learn when/why a round stops taking orders. Collector marker bumped; takes effect after the Pi pull + restart. Mock-tested locally. Status: pushed, awaiting confirmation on the Pi.
- 2026-11-05 20:00 Sniping study run (queue 052 / paste): no edge at the end of rounds (about -3% to -6% per $ overall; 95-99c bucket about 0%), $1,000 would not fill at 90-94c. Findings in kalshi-ai.md; raw in memory/inbox/snipe-study.md. v_snipe (practice, $25) keeps running to collect forward data.
- 2026-11-05 19:40 Kalshi v8.5: added practice-only v_snipe (late favourite buy, last 2 min, up to 97c, hold to end; cap 25) in sim.py; ENTRY_MAX/MAX_PRICE overridable per test; collector restart marker bumped. Syntax-checked and imported locally. Status: pushed, awaiting Pi pull + restart confirmation. Wallet fresh start (queue 051 / button) still to be confirmed.
- 2026-11-05 19:25 Filed Kylar's SNIPING idea (late big favourite bet) in kalshi-ai.md with the maths and a replay-test plan (practice only). Status: idea, test not built.
- 2026-11-05 17:58 KDP: built 8 hardcover notebooks (Process Operator + Lab Operator x schemes A navy, B green, C burgundy, E espresso) in ~/kdp-studio/books/<title>-<scheme> in Kylar's approved look (flat colour lettering, CAPS Liberation Serif Bold, fine grain, thin double border, short rule, spine title, tiny 'Lovelady LLC' on back by barcode box, owner page, 120 lined numbered cream pages). Build script tasks/kdp_build.py (queue 046). Studio checks pass; NOT yet verified against KDP's cover calculator; description/keywords/price not written. Previews in memory/inbox/kdp-preview/. Engine min rect width patched (backup engine.py.bak-minw); studio needs a restart to show the new books.
- 2026-11-05 17:16 Home speaker mic recording ON (queue 040, confirmed healthy). Earlier 'unhealthy' verdicts (037) were a false alarm: a trace from the stopped process matched 'Error'. Recordings land in ~/voice-data/home-mic; report in memory/inbox/home-mic-report.md after Sharee tests. Next: noise suppression (needs webrtc_noise_gain in the satellite venv).
- 2026-11-05 17:10 Filed voice-call decisions (Captain rules in architecture.md), created buy-list.md, queued home mic recording (037, awaiting result). Status: filed.
- Read repo memory and inbox. No Jarvis voice notes to file (0 note files). Pi snapshot (pi-status.md, 06:00 sync, 20 min old): all services active, no failed units, 40.6C, disk 9%, no throttling; containers up (Pi-hole up 10 h, Home Assistant up 4 h). Jarvis last 24 h: 71 turns, 0 errors, first words avg 1.6 s (slowest 4.2 s), 9 hang-ups by you, 2 by quiet timeout; 0 voices enrolled. Kalshi data fresh to 04:19 (practice only, live OFF); digest shows most strategies positive over 24 h but the 05:07 report shows a bad last 4 rounds for the top ones. Queue 018: Starship page on :8095 is up and serves 200. Nothing in todo.md dated today or tomorrow. Wrote memory/brief.md and updated projects.md. Status: memory only, nothing run on the Pi.

## 2026-11-05 (15:30)
- Home speaker: my first change (mic noise suppression) crashed the satellite (missing webrtc_noise_gain package); rolled back at 15:16 (queue 035), speaker healthy again. Second change (recording only, queue 036) ran at 15:19 before the demo hold took effect: it restarted the speaker, judged it unhealthy (check waited only 14 s, the satellite needs about 13 s to say 'Waiting for wake word') and rolled back; speaker active. Held copy now waits 35 s: tasks/queue-held/036-home-mic-record-only.sh. Next after Kylar's demo: record-only, then install webrtc_noise_gain and enable noise suppression, each with the health check.

## 2026-11-05 (15:25)
- NAME RULE (Kylar, 15:09): his wife is spelled SHAREE and said "sheree"; he is KYLAR, said "kyler". Fixed every file (family.md, truck-project.md, pi-home-assistant.md, Jarvis lab page, CLAUDE.md top line). Jarvis: speech heard as Shari/Sherry/Sheree is converted to Sharee on input and spoken "Sheree" out loud (pronunciation default); mentioning Sharee or Warren now loads family.md into his answer. Needs the Jarvis restart (pi_update.sh) to take effect.
- Older changelog lines below still say Sheree; they are history.

## 2026-11-05 (15:15)
- Home Jarvis urgent: queued diagnostics 029-032; added HOME JARVIS, pop-up font and Captain runtime items to todo.md/architecture.md. Found so far: HA hears Kylar (transcripts like 'What do you know about Shari?') but the Jarvis agent returns nothing: 'Chat Log opened but no assistant message was added', and phone-voice logs BrokenPipe from HA at 15:00:53; satellite restarted 14:58 and 15:01. Home font: settings.json font is Great Vibes. Sheree pronunciation added.

## 2026-11-05 (14:55)
- KDP: Kylar chose 4 colour schemes per job title (A navy/gold, B forest/gold, C burgundy/cream, E espresso/tan). Tonight: Process Operator A and Lab Operator A. Flagged the duplicate-content risk for same-interior books.

## 2026-11-05 (14:40)
- KDP: recorded the design brief and the Canva workflow; made the cover guide overlay (120 pages, hardcover) for Kylar; read what the studio supports (queue 026). Next: set up both book projects in the studio (title only, owner page, numbered lined pages, texture) and the listing text.

## 2026-11-05 (14:20)
- KDP: Kylar needs hardcover. Checked the studio's hardcover numbers against KDP's help page and a published guide; they match except the spine width, which must be confirmed with KDP's cover calculator at upload. Recorded in amazon-kdp.md.

## 2026-11-05 (14:00)
- Read the KDP studio on the Pi (what it can do and its 6x9 hardcover spec, not yet verified with KDP) and recorded it in amazon-kdp.md with tonight's goal (2 books in review).

## 2026-11-05 (13:54)
- Kylar did the Fresh start on the practice wallet (screenshot: $1,000.00, 0 rounds, strategy Auto). New record for the run wallet starts about 1:53 pm Central under cap 25 and the hold-to-end Auto rule.

## 2026-11-05 (13:55)
- Kylar decided to keep all Kalshi memory and history and let it ride (recorded in kalshi-ai.md).

## 2026-11-05 (13:50)
- Recorded Kylar's stake-sizing idea (bigger when indicators are strong) with the proof rule, in kalshi-ai.md and todo.md.

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
