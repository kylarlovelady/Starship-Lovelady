# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 12 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 3 days (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 3b75369 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 21 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    66 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1515 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +317.75 over  953 rounds, wins 12%   (-199.73 over +4 rounds since last check)
            v_edge10_s100_dd  +293.43 over  953 rounds, wins 12%   (-106.51 over +4 rounds since last check)
            v_x60222031  +134.44 over 1404 rounds, wins 47%   (-15.76 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1341 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1186 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x64216772   -52.21 over 1439 rounds, wins 57%   (-12.16 over +4 rounds since last check)
            hold        -55.64 over 1542 rounds, wins 58%   (+10.44 over +4 rounds since last check)
            v_x60222032   -82.98 over 1404 rounds, wins 58%   (-12.16 over +4 rounds since last check)
            v_x40223631  -122.67 over 1391 rounds, wins 57%   (-12.16 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 350.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
