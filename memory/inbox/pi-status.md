# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 12 hours, 42 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 13 hours; whisper Up 13 hours (healthy); piper Up 13 hours (healthy); pihole Up 13 hours (healthy); homeassistant Up 13 hours

## Sync and schedule
- Pi repo copy at: 264b8ab 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 23:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    67 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1360 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1161.45 over  767 rounds, wins 12%   (-99.93 over +3 rounds since last check)
            v_hold_s250_wild  +841.99 over  231 rounds, wins 62%   (-246.48 over +3 rounds since last check)
            v_edge10_s100_dd  +814.78 over  767 rounds, wins 12%   (-80.40 over +3 rounds since last check)
            v_x60222031  +216.63 over 1218 rounds, wins 47%   (-9.20 over +3 rounds since last check)
            v_x64216772   +41.06 over 1253 rounds, wins 58%   (-2.42 over +3 rounds since last check)
            v_x60222032   +10.29 over 1218 rounds, wins 59%   (-2.42 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1155 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1000 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631   -29.40 over 1205 rounds, wins 58%   (-2.42 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 291.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
