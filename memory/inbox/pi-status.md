# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 15 hours, 45 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 11 days (healthy); piper Up 11 days (healthy); pihole Up 8 days (healthy); homeassistant Up 11 days

## Sync and schedule
- Pi repo copy at: d90fba8 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 17 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 2 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    71 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1278 total)
      OK    entry_stats.json updated 7 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 11 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +1810.61 over  134 rounds, wins 64%   (+981.57 over +4 rounds since last check)
            v_edge10_s100  +772.48 over  670 rounds, wins 12%   (-42.28 over +4 rounds since last check)
            v_edge10_s100_dd  +605.32 over  670 rounds, wins 12%   (-10.44 over +4 rounds since last check)
            v_x64216772   +73.24 over 1156 rounds, wins 58%   (+14.14 over +4 rounds since last check)
            v_x60222032   +42.47 over 1121 rounds, wins 59%   (+14.14 over +4 rounds since last check)
            v_x40223631    +2.78 over 1108 rounds, wins 58%   (+14.14 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1058 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  903 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x12229262   -93.02 over 1100 rounds, wins 58%   (+33.95 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 262.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
