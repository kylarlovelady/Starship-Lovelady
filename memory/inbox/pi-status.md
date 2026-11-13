# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 14 hours, 45 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 2 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: 6c62ba5 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 12 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (891 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 18 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1521.00 over  218 rounds, wins 15%   (+45.65 over +3 rounds since last check)
            v_edge10_s100_dd  +929.56 over  218 rounds, wins 15%   (+15.34 over +3 rounds since last check)
            v_x64216772   +81.25 over  704 rounds, wins 55%   (-4.58 over +3 rounds since last check)
            v_x96220861   +63.34 over  669 rounds, wins 45%   (-2.48 over +3 rounds since last check)
            v_x60222032   +50.48 over  669 rounds, wins 55%   (-4.58 over +3 rounds since last check)
            v_x60222031   +45.99 over  669 rounds, wins 46%   (-2.55 over +3 rounds since last check)
            v_x40223631   +10.79 over  656 rounds, wins 55%   (-4.58 over +3 rounds since last check)
            v_snipe_all    +2.70 over  606 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  451 rounds, wins 0%   (+0.00 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 141.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
