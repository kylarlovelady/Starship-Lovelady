# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 18 hours, 12 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 18 hours; whisper Up 18 hours (healthy); piper Up 18 hours (healthy); pihole Up 18 hours (healthy); homeassistant Up 18 hours

## Sync and schedule
- Pi repo copy at: 91024a7 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    61 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1370 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 14 min ago
      OK    patterns.json updated 12 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1569.77 over  779 rounds, wins 13%   (-99.90 over +3 rounds since last check)
            v_edge10_s100_dd  +925.01 over  779 rounds, wins 13%   (-62.47 over +3 rounds since last check)
            v_hold_s250_wild  +721.15 over  243 rounds, wins 62%   (-40.35 over +3 rounds since last check)
            v_x60222031  +231.48 over 1230 rounds, wins 47%   (-3.20 over +3 rounds since last check)
            v_x64216772   +22.19 over 1265 rounds, wins 58%   (-1.34 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1167 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1012 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032    -8.58 over 1230 rounds, wins 59%   (-1.34 over +3 rounds since last check)
            v_x12229262   -24.51 over 1209 rounds, wins 58%   (+6.36 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 296.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
