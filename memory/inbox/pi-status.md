# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 9 hours, 42 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 4 days (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: 01fc16d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 22 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    71 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1609 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1453 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1298 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_edge10_s100_dd   -63.78 over 1065 rounds, wins 12%   (-63.57 over +2 rounds since last check)
            v_x64216772   -81.87 over 1551 rounds, wins 57%   (-8.83 over +2 rounds since last check)
            v_x60222032  -112.64 over 1516 rounds, wins 57%   (-8.83 over +2 rounds since last check)
            v_snipe    -118.53 over 1454 rounds, wins 27%   (-5.68 over +2 rounds since last check)
            v_x40223631  -152.33 over 1503 rounds, wins 57%   (-8.83 over +2 rounds since last check)
            v_edge10_s100  -216.22 over 1065 rounds, wins 12%   (-99.82 over +2 rounds since last check)
            v_x60222031  -250.98 over 1516 rounds, wins 46%   (-18.99 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 384.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
