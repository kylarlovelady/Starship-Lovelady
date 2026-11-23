# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 3 hours, 12 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 5 days (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: 00d00db 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 23 Nov 14:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 4 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    63 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1656 total)
      OK    entry_stats.json updated 9 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 23 min ago
      OK    learn_report.json updated 18 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1508 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1353 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_x64216772   -97.86 over 1606 rounds, wins 57%   (-10.15 over +2 rounds since last check)
            v_x60222032  -128.63 over 1571 rounds, wins 57%   (-10.15 over +2 rounds since last check)
            v_snipe    -148.81 over 1509 rounds, wins 26%   (+0.00 over +2 rounds since last check)
            v_x40223631  -168.32 over 1558 rounds, wins 57%   (-10.15 over +2 rounds since last check)
            hold       -226.51 over 1709 rounds, wins 58%   (+15.07 over +2 rounds since last check)
            v_x60222031  -242.56 over 1571 rounds, wins 46%   (+4.44 over +2 rounds since last check)
            v_hold_s10  -291.17 over 1353 rounds, wins 58%   (-11.18 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 401.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
