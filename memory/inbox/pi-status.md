# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 1 hour, 42 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 26 hours; whisper Up 26 hours (healthy); piper Up 26 hours (healthy); pihole Up 26 hours (healthy); homeassistant Up 26 hours

## Sync and schedule
- Pi repo copy at: 836d0f6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    61 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1390 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1095.99 over  802 rounds, wins 12%   (-99.87 over +3 rounds since last check)
            v_hold_s250_wild  +842.49 over  266 rounds, wins 64%   (-244.94 over +3 rounds since last check)
            v_edge10_s100_dd  +753.65 over  802 rounds, wins 12%   (-33.83 over +3 rounds since last check)
            v_x60222031  +150.42 over 1253 rounds, wins 47%   (-4.15 over +3 rounds since last check)
            v_x64216772   +37.71 over 1288 rounds, wins 59%   (-1.22 over +3 rounds since last check)
            v_x60222032    +6.94 over 1253 rounds, wins 59%   (-1.22 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1190 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1035 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631   -32.75 over 1240 rounds, wins 59%   (-1.22 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 304.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
