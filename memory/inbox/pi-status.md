# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 21 hours, 12 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 21 hours; whisper Up 21 hours (healthy); piper Up 21 hours (healthy); pihole Up 21 hours (healthy); homeassistant Up 21 hours

## Sync and schedule
- Pi repo copy at: 222e110 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 2 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    63 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1379 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1437.70 over  789 rounds, wins 13%   (-42.17 over +3 rounds since last check)
            v_hold_s250_wild  +888.53 over  253 rounds, wins 62%   (+469.75 over +3 rounds since last check)
            v_edge10_s100_dd  +883.26 over  789 rounds, wins 13%   (-10.45 over +3 rounds since last check)
            v_x60222031  +165.65 over 1240 rounds, wins 47%   (-41.01 over +3 rounds since last check)
            v_x64216772   +15.70 over 1275 rounds, wins 58%   (-4.10 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1177 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1022 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032   -15.07 over 1240 rounds, wins 59%   (-4.10 over +3 rounds since last check)
            v_x40223631   -54.76 over 1227 rounds, wins 58%   (-4.10 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 299.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
