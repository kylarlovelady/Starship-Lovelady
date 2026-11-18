# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 16 hours, 15 minutes; temp 46.6'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 11 days (healthy); piper Up 11 days (healthy); pihole Up 8 days (healthy); homeassistant Up 11 days

## Sync and schedule
- Pi repo copy at: 7d813e4 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 17 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    71 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1281 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 4 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 19 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +1774.86 over  138 rounds, wins 64%   (-35.75 over +4 rounds since last check)
            v_edge10_s100 +1170.68 over  674 rounds, wins 12%   (+398.20 over +4 rounds since last check)
            v_edge10_s100_dd  +867.27 over  674 rounds, wins 12%   (+261.95 over +4 rounds since last check)
            v_x64216772   +65.43 over 1160 rounds, wins 58%   (-7.81 over +4 rounds since last check)
            v_x60222032   +34.66 over 1125 rounds, wins 58%   (-7.81 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1062 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  907 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631    -5.03 over 1112 rounds, wins 58%   (-7.81 over +4 rounds since last check)
            v_x12229262   -96.07 over 1104 rounds, wins 58%   (-3.05 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 262.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
