# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 8 hours, 45 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 33 hours; whisper Up 33 hours (healthy); piper Up 33 hours (healthy); pihole Up 33 hours (healthy); homeassistant Up 33 hours

## Sync and schedule
- Pi repo copy at: 972ec5d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (458 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031  +292.49 over  220 rounds, wins 43%   (-35.47 over +4 rounds since last check)
            v_x96220861  +208.09 over  220 rounds, wins 40%   (-33.70 over +4 rounds since last check)
            v_x88221261  +126.82 over  227 rounds, wins 23%   (-49.91 over +4 rounds since last check)
            v_x64216772  +119.05 over  255 rounds, wins 46%   (-9.23 over +4 rounds since last check)
            v_x40223632   +99.19 over  207 rounds, wins 45%   (+22.44 over +4 rounds since last check)
            v_x60222032   +88.28 over  220 rounds, wins 47%   (-9.23 over +4 rounds since last check)
            v_x40223631   +48.59 over  207 rounds, wins 44%   (-9.23 over +4 rounds since last check)
            v_snipe_all    +2.70 over  157 rounds, wins 1%   (+0.00 over +4 rounds since last check)
            v_take5      +0.88 over    2 rounds, wins 100%

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 15.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
