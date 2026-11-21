# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 22 hours, 12 minutes; temp 45.5'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 36cb1ec 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 21 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    65 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1508 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +179.42 over  945 rounds, wins 12%   (+53.57 over +4 rounds since last check)
            v_edge10_s100_dd  +133.33 over  945 rounds, wins 12%   (+13.39 over +4 rounds since last check)
            v_x60222031  +119.02 over 1396 rounds, wins 47%   (-22.43 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1333 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1178 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x64216772   -41.60 over 1431 rounds, wins 57%   (-9.54 over +4 rounds since last check)
            hold        -56.50 over 1534 rounds, wins 58%   (-27.24 over +4 rounds since last check)
            v_x60222032   -72.37 over 1396 rounds, wins 58%   (-9.54 over +4 rounds since last check)
            v_x40223631  -112.06 over 1383 rounds, wins 58%   (-9.54 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 348.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
