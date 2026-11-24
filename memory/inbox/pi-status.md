# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 1 hour, 42 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 6 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 37da329 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 24 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 5 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    60 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1712 total)
      OK    entry_stats.json updated 10 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 23 min ago
      OK    learn_report.json updated 19 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1570 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1415 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_snipe    -141.69 over 1571 rounds, wins 26%   (+0.00 over +2 rounds since last check)
            v_x64216772  -205.68 over 1668 rounds, wins 56%   (+10.05 over +2 rounds since last check)
            hold       -233.73 over 1771 rounds, wins 59%   (-23.74 over +2 rounds since last check)
            v_x60222032  -236.45 over 1633 rounds, wins 56%   (+10.05 over +2 rounds since last check)
            v_x40223631  -276.14 over 1620 rounds, wins 56%   (+10.05 over +2 rounds since last check)
            v_hold_s10  -291.88 over 1415 rounds, wins 58%   (+5.52 over +2 rounds since last check)
            v_take25_s10  -387.11 over 1415 rounds, wins 68%   (+5.34 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 424.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
