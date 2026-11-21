# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 6 hours, 12 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 3 days (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 0f35a55 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 21 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    63 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1529 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 2 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd   +92.93 over  972 rounds, wins 12%   (+4.39 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1360 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1205 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_edge10_s100   -49.75 over  972 rounds, wins 12%   (+18.24 over +3 rounds since last check)
            v_x60222031   -67.58 over 1423 rounds, wins 47%   (-19.22 over +3 rounds since last check)
            v_x64216772   -95.22 over 1458 rounds, wins 57%   (+28.09 over +3 rounds since last check)
            hold       -125.88 over 1561 rounds, wins 58%   (+28.44 over +3 rounds since last check)
            v_x60222032  -125.99 over 1423 rounds, wins 58%   (+28.09 over +3 rounds since last check)
            v_snipe    -144.31 over 1361 rounds, wins 27%   (-5.76 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 356.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
