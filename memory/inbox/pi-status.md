# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 11 hours, 42 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 8776bcf 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 22:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    60 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1478 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 18 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031   +56.16 over 1361 rounds, wins 47%   (+3.58 over +2 rounds since last check)
            v_edge10_s100   +49.19 over  910 rounds, wins 12%   (+0.00 over +2 rounds since last check)
            v_edge10_s100_dd   +40.07 over  910 rounds, wins 12%   (+0.00 over +2 rounds since last check)
            v_snipe_all    +2.70 over 1298 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1143 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_x64216772   -61.36 over 1396 rounds, wins 58%   (+3.58 over +2 rounds since last check)
            v_x60222032   -92.13 over 1361 rounds, wins 58%   (+3.58 over +2 rounds since last check)
            v_snipe    -121.67 over 1299 rounds, wins 27%   (+0.00 over +2 rounds since last check)
            v_x40223631  -131.82 over 1348 rounds, wins 58%   (+3.58 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 338.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
