# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 17 hours, 45 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 5 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 1ac303b 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    81 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1067 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 23 min ago
      OK    patterns.json updated 20 min ago
      OK    learn_report.json updated 19 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1404.32 over  415 rounds, wins 13%   (-84.45 over +3 rounds since last check)
            v_edge10_s100_dd  +734.50 over  415 rounds, wins 13%   (-20.94 over +3 rounds since last check)
            v_x64216772  +105.92 over  901 rounds, wins 56%   (-0.11 over +3 rounds since last check)
            v_x60222032   +75.15 over  866 rounds, wins 57%   (-0.11 over +3 rounds since last check)
            v_x40223631   +35.46 over  853 rounds, wins 56%   (-0.11 over +3 rounds since last check)
            v_x60222031    +3.68 over  866 rounds, wins 46%   (+25.07 over +3 rounds since last check)
            v_snipe_all    +2.70 over  803 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  648 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x12229262    -6.09 over  845 rounds, wins 56%   (-3.99 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 192.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
