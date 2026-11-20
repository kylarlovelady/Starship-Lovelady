# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 18 hours, 42 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 22%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 43 hours; whisper Up 43 hours (healthy); piper Up 43 hours (healthy); pihole Up 43 hours (healthy); homeassistant Up 43 hours

## Sync and schedule
- Pi repo copy at: fabca47 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    62 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1432 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 34 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1189.86 over  856 rounds, wins 12%   (+286.24 over +3 rounds since last check)
            v_edge10_s100_dd  +705.36 over  856 rounds, wins 12%   (+92.34 over +3 rounds since last check)
            v_hold_s250_wild  +350.25 over  320 rounds, wins 64%   (+433.45 over +3 rounds since last check)
            v_x60222031  +219.87 over 1307 rounds, wins 48%   (+45.63 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1244 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1089 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x64216772    -4.67 over 1342 rounds, wins 58%   (+25.75 over +3 rounds since last check)
            v_x60222032   -35.44 over 1307 rounds, wins 59%   (+25.75 over +3 rounds since last check)
            v_x40223631   -75.13 over 1294 rounds, wins 59%   (+25.75 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 321.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
