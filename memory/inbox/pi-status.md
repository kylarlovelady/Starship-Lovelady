# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 9 hours, 45 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 3 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: d8452c6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 13 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    79 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (955 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 12 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1468.49 over  290 rounds, wins 14%   (-8.19 over +4 rounds since last check)
            v_edge10_s100_dd  +793.20 over  290 rounds, wins 14%   (-8.19 over +4 rounds since last check)
            v_x64216772   +90.74 over  776 rounds, wins 55%   (+4.51 over +4 rounds since last check)
            v_x60222032   +59.97 over  741 rounds, wins 56%   (+4.51 over +4 rounds since last check)
            v_x40223631   +20.28 over  728 rounds, wins 55%   (+4.51 over +4 rounds since last check)
            v_snipe_all    +2.70 over  678 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  523 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x60222031   -52.25 over  741 rounds, wins 46%   (-29.75 over +4 rounds since last check)
            v_hold_s10   -54.79 over  523 rounds, wins 60%   (-5.59 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 160.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
