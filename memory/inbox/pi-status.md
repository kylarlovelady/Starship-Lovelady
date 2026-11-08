# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 22 hours, 45 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 hours; whisper Up 47 hours (healthy); piper Up 47 hours (healthy); pihole Up 47 hours (healthy); homeassistant Up 47 hours

## Sync and schedule
- Pi repo copy at: 650f04f 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 01:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (514 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1020.20 over   58 rounds, wins 67%   (-291.06 over +4 rounds since last check)
            v_hold_s250  +734.13 over   58 rounds, wins 67%   (-150.74 over +4 rounds since last check)
            v_hold_s100  +397.24 over   58 rounds, wins 67%   (-66.77 over +4 rounds since last check)
            v_x96220861  +273.21 over  276 rounds, wins 42%   (-1.89 over +4 rounds since last check)
            v_x60222031  +259.81 over  276 rounds, wins 43%   (-5.79 over +4 rounds since last check)
            v_hold_s50  +222.25 over   58 rounds, wins 67%   (-38.59 over +4 rounds since last check)
            v_hold_after60  +182.49 over   58 rounds, wins 69%   (-16.81 over +4 rounds since last check)
            v_hold_after120  +174.43 over   58 rounds, wins 67%   (+24.23 over +4 rounds since last check)
            v_x64216772  +135.22 over  311 rounds, wins 50%   (-13.48 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 29.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
