# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 3 hours, 15 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 27 hours; whisper Up 27 hours (healthy); piper Up 27 hours (healthy); pihole Up 27 hours (healthy); homeassistant Up 27 hours

## Sync and schedule
- Pi repo copy at: e912159 11 minutes ago: Daily check 2026-11-07: brief, projects, Kalshi snipe update
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 06:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (438 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +375.92 over  200 rounds, wins 40%   (+70.10 over +4 rounds since last check)
            v_x60222031  +297.72 over  200 rounds, wins 42%   (+9.42 over +4 rounds since last check)
            v_x88221261  +253.26 over  207 rounds, wins 23%   (-2.66 over +4 rounds since last check)
            v_x64216772  +144.73 over  235 rounds, wins 45%   (-13.36 over +4 rounds since last check)
            v_x60222032  +113.96 over  200 rounds, wins 46%   (-13.36 over +4 rounds since last check)
            v_x12229262   +76.18 over  179 rounds, wins 41%   (-41.76 over +4 rounds since last check)
            v_x40223631   +74.27 over  187 rounds, wins 43%   (-13.36 over +4 rounds since last check)
            v_x40223632   +53.25 over  187 rounds, wins 44%   (+30.52 over +4 rounds since last check)
            v_x96220872    +3.87 over  200 rounds, wins 33%   (-10.66 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 9.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
