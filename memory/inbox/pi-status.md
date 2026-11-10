# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 1 hour, 30 minutes; temp 37.3'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 9 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: 4b8995f 15 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (37 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 52 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (672 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1513.53 over  220 rounds, wins 62%   (+8.17 over +4 rounds since last check)
            v_hold_s250  +707.46 over  220 rounds, wins 62%   (+8.17 over +4 rounds since last check)
            v_hold_s100  +292.20 over  220 rounds, wins 62%   (+8.17 over +4 rounds since last check)
            v_hold_s50  +166.15 over  220 rounds, wins 62%   (+8.17 over +4 rounds since last check)
            v_x60222031  +129.11 over  438 rounds, wins 45%   (+40.16 over +4 rounds since last check)
            v_x64216772  +126.50 over  473 rounds, wins 53%   (+8.17 over +4 rounds since last check)
            v_x60222032   +95.73 over  438 rounds, wins 54%   (+8.17 over +4 rounds since last check)
            v_hold_s25   +84.89 over  220 rounds, wins 62%   (+8.17 over +4 rounds since last check)
            v_x40223631   +56.04 over  425 rounds, wins 53%   (+8.17 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 80.1 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
