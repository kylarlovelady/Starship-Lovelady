# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 20 hours, 42 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 5 days (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: bb68f1d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 24 Nov 07:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 4 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    60 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1699 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 23 min ago
      OK    learn_report.json updated 17 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1556 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1401 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_snipe    -143.16 over 1557 rounds, wins 26%   (+0.00 over +2 rounds since last check)
            v_x64216772  -170.82 over 1654 rounds, wins 56%   (+0.73 over +2 rounds since last check)
            hold       -181.71 over 1757 rounds, wins 59%   (+1.31 over +2 rounds since last check)
            v_x60222032  -201.59 over 1619 rounds, wins 57%   (+0.73 over +2 rounds since last check)
            v_x40223631  -241.28 over 1606 rounds, wins 56%   (+0.73 over +2 rounds since last check)
            v_hold_s10  -298.77 over 1401 rounds, wins 58%   (+6.95 over +2 rounds since last check)
            v_edge10_s100_dd  -386.30 over 1168 rounds, wins 13%   (-73.55 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 419.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
