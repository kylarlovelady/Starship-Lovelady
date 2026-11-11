# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 6 hours, 15 minutes; temp 38.9'C; throttled flags 0x0 (0x0 is clean); memory 40%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 38 hours (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: 879250c 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 11 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    91 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (780 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +809.02 over  103 rounds, wins 12%   (-91.10 over +4 rounds since last check)
            v_edge10_s100  +802.17 over  103 rounds, wins 12%   (-99.85 over +4 rounds since last check)
            v_x60222031  +301.83 over  554 rounds, wins 45%   (+64.46 over +4 rounds since last check)
            v_x64216772   +72.21 over  589 rounds, wins 53%   (-3.36 over +4 rounds since last check)
            v_x60222032   +41.44 over  554 rounds, wins 54%   (-3.36 over +4 rounds since last check)
            v_snipe_all    +2.70 over  491 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631    +1.75 over  541 rounds, wins 53%   (-3.36 over +4 rounds since last check)
            v_hold_s5    +0.00 over  336 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -71.39 over  336 rounds, wins 58%   (-2.38 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 108.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
