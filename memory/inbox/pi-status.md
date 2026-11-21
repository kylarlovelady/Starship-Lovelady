# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 12 hours, 42 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 8af42c7 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 23:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    61 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1481 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 21 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 16 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031   +37.08 over 1364 rounds, wins 47%   (-19.08 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1301 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1146 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd   -58.27 over  913 rounds, wins 12%   (-98.34 over +3 rounds since last check)
            v_x64216772   -58.72 over 1399 rounds, wins 58%   (+2.64 over +3 rounds since last check)
            v_x60222032   -89.49 over 1364 rounds, wins 58%   (+2.64 over +3 rounds since last check)
            v_snipe    -121.50 over 1302 rounds, wins 27%   (+0.17 over +3 rounds since last check)
            v_x40223631  -129.18 over 1351 rounds, wins 58%   (+2.64 over +3 rounds since last check)
            v_edge10_s100  -150.72 over  913 rounds, wins 12%   (-199.91 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 339.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
