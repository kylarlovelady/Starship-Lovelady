# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 5 hours, 42 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 5 days (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: 4cdf00e 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 23 Nov 16:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    63 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1662 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 3 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1514 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1359 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x64216772  -137.36 over 1612 rounds, wins 57%   (-30.28 over +3 rounds since last check)
            v_snipe    -147.87 over 1515 rounds, wins 26%   (+1.25 over +3 rounds since last check)
            v_x60222032  -168.13 over 1577 rounds, wins 57%   (-30.28 over +3 rounds since last check)
            v_x40223631  -207.82 over 1564 rounds, wins 57%   (-30.28 over +3 rounds since last check)
            hold       -240.06 over 1715 rounds, wins 58%   (-45.67 over +3 rounds since last check)
            v_x60222031  -297.74 over 1577 rounds, wins 46%   (-43.09 over +3 rounds since last check)
            v_hold_s10  -307.64 over 1359 rounds, wins 58%   (-11.27 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 404.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
