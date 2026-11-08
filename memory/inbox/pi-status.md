# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 16 hours, 15 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 38%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 40 hours; whisper Up 40 hours (healthy); piper Up 40 hours (healthy); pihole Up 40 hours (healthy); homeassistant Up 40 hours

## Sync and schedule
- Pi repo copy at: c6ca1eb 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (490 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +325.01 over  252 rounds, wins 41%   (-24.14 over +4 rounds since last check)
            v_x60222031  +239.68 over  252 rounds, wins 44%   (+15.95 over +4 rounds since last check)
            v_hold_s100  +149.13 over   34 rounds, wins 71%   (+206.70 over +4 rounds since last check)
            v_x64216772  +130.02 over  287 rounds, wins 48%   (+13.62 over +4 rounds since last check)
            v_hold_s50  +103.45 over   34 rounds, wins 71%   (+102.75 over +4 rounds since last check)
            v_x60222032   +99.25 over  252 rounds, wins 50%   (+13.62 over +4 rounds since last check)
            v_hold_s250   +97.85 over   34 rounds, wins 71%   (+516.51 over +4 rounds since last check)
            v_x40223632   +89.90 over  239 rounds, wins 44%   (-11.41 over +4 rounds since last check)
            v_x40223631   +59.56 over  239 rounds, wins 47%   (+13.62 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 22.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
