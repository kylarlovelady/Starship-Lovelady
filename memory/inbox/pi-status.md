# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 1 hour, 15 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 11 days (healthy); piper Up 11 days (healthy); pihole Up 7 days (healthy); homeassistant Up 11 days

## Sync and schedule
- Pi repo copy at: 7a3f35a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 17 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    64 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1233 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +2320.21 over   84 rounds, wins 67%   (-413.65 over +4 rounds since last check)
            v_edge10_s100  +579.51 over  620 rounds, wins 12%   (-59.00 over +4 rounds since last check)
            v_edge10_s100_dd  +504.59 over  620 rounds, wins 12%   (-14.82 over +4 rounds since last check)
            v_x64216772   +61.28 over 1106 rounds, wins 58%   (-5.34 over +4 rounds since last check)
            v_x60222032   +30.51 over 1071 rounds, wins 58%   (-5.34 over +4 rounds since last check)
            v_x12229262    +4.36 over 1050 rounds, wins 58%   (-37.95 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1008 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  853 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631    -9.18 over 1058 rounds, wins 58%   (-5.34 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 247.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
