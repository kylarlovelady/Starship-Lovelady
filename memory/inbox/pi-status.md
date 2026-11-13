# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 16 hours, 45 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 3 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: cae3dd5 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 12 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    76 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (897 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 5 min ago
      OK    patterns.json updated 3 min ago
      OK    learn_report.json updated 20 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1478.64 over  225 rounds, wins 14%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  +919.05 over  225 rounds, wins 14%   (+0.00 over +3 rounds since last check)
            v_x64216772   +66.12 over  711 rounds, wins 55%   (-9.80 over +3 rounds since last check)
            v_x60222032   +35.35 over  676 rounds, wins 55%   (-9.80 over +3 rounds since last check)
            v_x60222031    +5.63 over  676 rounds, wins 46%   (+6.71 over +3 rounds since last check)
            v_x96220861    +5.39 over  676 rounds, wins 45%   (-9.53 over +3 rounds since last check)
            v_snipe_all    +2.70 over  613 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  458 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631    -4.34 over  663 rounds, wins 55%   (-9.80 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 143.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
