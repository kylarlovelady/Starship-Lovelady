# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 21 hours, 15 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 21 hours; whisper Up 21 hours (healthy); piper Up 21 hours (healthy); pihole Up 21 hours (healthy); homeassistant Up 21 hours

## Sync and schedule
- Pi repo copy at: 9c16ea1 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 00:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (414 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +368.31 over  176 rounds, wins 39%   (-55.73 over +4 rounds since last check)
            v_x60222031  +263.74 over  176 rounds, wins 40%   (-52.87 over +4 rounds since last check)
            v_x88221261  +256.46 over  183 rounds, wins 21%   (-15.56 over +4 rounds since last check)
            v_x64216772  +202.19 over  211 rounds, wins 46%   (+22.36 over +4 rounds since last check)
            v_x12229262  +173.77 over  155 rounds, wins 41%   (+22.36 over +4 rounds since last check)
            v_x60222032  +171.42 over  176 rounds, wins 47%   (+22.36 over +4 rounds since last check)
            v_x64216771  +157.82 over  211 rounds, wins 36%   (-72.08 over +4 rounds since last check)
            v_x40223631  +131.73 over  163 rounds, wins 44%   (+22.36 over +4 rounds since last check)
            v_x52220781  +102.59 over  187 rounds, wins 22%   (-22.24 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 3.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
