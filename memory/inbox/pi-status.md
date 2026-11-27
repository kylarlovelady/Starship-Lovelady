# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 23 hours, 12 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 8 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: dd4b672 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 2 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 27 Nov 10:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 1 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 57 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1874 total)
      OK    entry_stats.json updated 6 min ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 17 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +465.47 over 1379 rounds, wins 14%   (+389.29 over +3 rounds since last check)
            v_edge10_s100  +362.78 over 1379 rounds, wins 14%   (+552.28 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1767 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1612 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -129.31 over 1768 rounds, wins 26%   (+0.00 over +3 rounds since last check)
            v_x64216772  -343.28 over 1865 rounds, wins 55%   (+24.71 over +3 rounds since last check)
            v_hold_s10  -354.97 over 1612 rounds, wins 57%   (+24.60 over +3 rounds since last check)
            v_x60222032  -374.05 over 1830 rounds, wins 55%   (+24.71 over +3 rounds since last check)
            v_x40223631  -415.78 over 1817 rounds, wins 55%   (+24.71 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 493.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
