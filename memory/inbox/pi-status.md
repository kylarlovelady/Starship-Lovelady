# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 2 days, 2 hours, 42 minutes; temp 45.5'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 9 days (healthy); piper Up 9 days (healthy); pihole Up 9 days (healthy); homeassistant Up 9 days

## Sync and schedule
- Pi repo copy at: a79dd5d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 4 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 27 Nov 13:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 55 of the last 96 rounds were settled by Kalshi and logged
      OK    +1 new written lessons since the last check (1880 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 19 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +267.86 over 1387 rounds, wins 14%   (-10.06 over +3 rounds since last check)
            v_edge10_s100   +22.17 over 1387 rounds, wins 14%   (-41.16 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1775 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1620 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -128.80 over 1776 rounds, wins 26%   (+0.22 over +3 rounds since last check)
            v_hold_s10  -374.19 over 1620 rounds, wins 57%   (-9.43 over +3 rounds since last check)
            v_x64216772  -391.10 over 1873 rounds, wins 55%   (-17.83 over +3 rounds since last check)
            v_x60222032  -421.87 over 1838 rounds, wins 55%   (-17.83 over +3 rounds since last check)
            v_x40223631  -463.60 over 1825 rounds, wins 55%   (-17.83 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 497.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
