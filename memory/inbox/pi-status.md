# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 11 hours, 45 minutes; temp 45.0'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 16 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 7ed7082 24 minutes ago: Kitchen case: cord exit moved to the right bay
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 14:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (565 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +2446.46 over  110 rounds, wins 65%   (+519.77 over +4 rounds since last check)
            v_hold_s250 +1322.21 over  110 rounds, wins 65%   (+262.11 over +4 rounds since last check)
            v_hold_s100  +531.90 over  110 rounds, wins 65%   (+107.79 over +4 rounds since last check)
            v_hold_s50  +277.71 over  110 rounds, wins 65%   (+56.12 over +4 rounds since last check)
            v_x96220861  +251.73 over  328 rounds, wins 43%   (-27.33 over +4 rounds since last check)
            v_x60222031  +234.80 over  328 rounds, wins 45%   (-33.41 over +4 rounds since last check)
            v_hold_s25  +131.29 over  110 rounds, wins 65%   (+30.62 over +4 rounds since last check)
            v_x64216772  +106.06 over  363 rounds, wins 51%   (+10.92 over +4 rounds since last check)
            v_take100   +99.33 over  110 rounds, wins 65%   (+30.62 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 42.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
