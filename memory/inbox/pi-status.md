# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 8 hours, 42 minutes; temp 47.2'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 4 days (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: ec1df63 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 4 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 22 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    73 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1607 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 18 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1451 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1296 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_edge10_s100_dd    -0.21 over 1063 rounds, wins 13%   (-58.19 over +4 rounds since last check)
            v_x64216772   -73.04 over 1549 rounds, wins 57%   (-4.56 over +4 rounds since last check)
            v_x60222032  -103.81 over 1514 rounds, wins 57%   (-4.56 over +4 rounds since last check)
            v_snipe    -112.85 over 1452 rounds, wins 27%   (-10.20 over +4 rounds since last check)
            v_edge10_s100  -116.40 over 1063 rounds, wins 13%   (-78.00 over +4 rounds since last check)
            v_x40223631  -143.50 over 1501 rounds, wins 57%   (-4.56 over +4 rounds since last check)
            v_x60222031  -231.99 over 1514 rounds, wins 46%   (-2.85 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 383.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
