# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 9 hours, 42 minutes; temp 45.0'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 8 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 2da61de 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 26 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 2 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 51 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1840 total)
      OK    entry_stats.json updated 7 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 17 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1727 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1572 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_edge10_s100_dd  -100.24 over 1339 rounds, wins 13%   (+0.00 over +2 rounds since last check)
            v_snipe    -148.79 over 1728 rounds, wins 26%   (+0.00 over +2 rounds since last check)
            v_hold_s10  -382.25 over 1572 rounds, wins 57%   (+1.32 over +2 rounds since last check)
            v_x64216772  -406.31 over 1825 rounds, wins 55%   (+2.26 over +2 rounds since last check)
            v_x60222032  -437.08 over 1790 rounds, wins 55%   (+2.26 over +2 rounds since last check)
            v_x40223631  -476.77 over 1777 rounds, wins 55%   (+2.26 over +2 rounds since last check)
            v_take25_s10  -491.55 over 1572 rounds, wins 67%   (+1.32 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 480.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
