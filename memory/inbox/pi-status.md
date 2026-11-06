# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 hours, 45 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 33%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 hours; whisper Up 7 hours (healthy); piper Up 7 hours (healthy); pihole Up 7 hours (healthy); homeassistant Up 7 hours

## Sync and schedule
- Pi repo copy at: ce53cb6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (355 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 5 min ago
      OK    patterns.json updated 4 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +441.77 over  116 rounds, wins 40%   (-7.15 over +4 rounds since last check)
            v_x60222031  +418.21 over  116 rounds, wins 42%   (+55.64 over +4 rounds since last check)
            v_x88221261  +284.55 over  123 rounds, wins 19%   (+25.12 over +4 rounds since last check)
            v_x64216772  +141.84 over  151 rounds, wins 45%   (+2.92 over +4 rounds since last check)
            v_x64216771  +132.44 over  151 rounds, wins 36%   (-0.07 over +4 rounds since last check)
            v_x80218932  +121.69 over  135 rounds, wins 43%   (-19.01 over +4 rounds since last check)
            v_x60222032  +111.07 over  116 rounds, wins 47%   (+2.92 over +4 rounds since last check)
            v_x52220781   +95.60 over  127 rounds, wins 20%   (+28.74 over +4 rounds since last check)
            v_x40223631   +71.38 over  103 rounds, wins 41%   (+2.92 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 20.1 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
