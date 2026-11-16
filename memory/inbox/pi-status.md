# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 4 hours, 45 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 10 days (healthy); piper Up 10 days (healthy); pihole Up 6 days (healthy); homeassistant Up 10 days

## Sync and schedule
- Pi repo copy at: ad1b3de 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 16 Nov 07:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    69 of the last 96 rounds were settled by Kalshi and logged
      OK    +1 new written lessons since the last check (1171 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +693.46 over  544 rounds, wins 11%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  +449.85 over  544 rounds, wins 11%   (+0.00 over +3 rounds since last check)
            v_x64216772   +36.67 over 1030 rounds, wins 57%   (-2.54 over +3 rounds since last check)
            v_x60222032    +5.90 over  995 rounds, wins 58%   (-2.54 over +3 rounds since last check)
            v_snipe_all    +2.70 over  932 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  777 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631   -33.79 over  982 rounds, wins 57%   (-2.54 over +3 rounds since last check)
            v_x60222031   -64.80 over  995 rounds, wins 45%   (+13.84 over +3 rounds since last check)
            v_x12229262   -73.88 over  974 rounds, wins 57%   (+11.90 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 227.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
