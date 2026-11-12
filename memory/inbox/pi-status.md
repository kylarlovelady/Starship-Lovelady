# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 9 hours, 15 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 2 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: c145814 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 12 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    81 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (875 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1463.39 over  201 rounds, wins 14%   (-42.36 over +4 rounds since last check)
            v_edge10_s100_dd  +920.66 over  201 rounds, wins 14%   (-10.51 over +4 rounds since last check)
            v_x60222031  +109.25 over  652 rounds, wins 45%   (-22.44 over +4 rounds since last check)
            v_x64216772   +79.67 over  687 rounds, wins 54%   (+2.97 over +4 rounds since last check)
            v_x96220861   +70.45 over  652 rounds, wins 45%   (-38.02 over +4 rounds since last check)
            v_x60222032   +48.90 over  652 rounds, wins 55%   (+2.97 over +4 rounds since last check)
            v_x40223631    +9.21 over  639 rounds, wins 54%   (+2.97 over +4 rounds since last check)
            v_snipe_all    +2.70 over  589 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  434 rounds, wins 0%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 135.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
