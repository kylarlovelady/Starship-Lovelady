# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 17 hours, 26 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 17 hours; whisper Up 17 hours (healthy); piper Up 17 hours (healthy); pihole Up 17 hours (healthy); homeassistant Up 17 hours

## Sync and schedule
- Pi repo copy at: 9300903 14 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (37 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    61 of the last 96 rounds were settled by Kalshi and logged
      STUCK +0 new written lessons since the last check (1367 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 22 min ago
      OK    patterns.json updated 19 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1669.67 over  776 rounds, wins 13%   (+0.00 over +0 rounds since last check)
            v_edge10_s100_dd  +987.48 over  776 rounds, wins 13%   (+0.00 over +0 rounds since last check)
            v_hold_s250_wild  +761.50 over  240 rounds, wins 62%   (+0.00 over +0 rounds since last check)
            v_x60222031  +234.68 over 1227 rounds, wins 47%   (+0.00 over +0 rounds since last check)
            v_x64216772   +23.53 over 1262 rounds, wins 58%   (+0.00 over +0 rounds since last check)
            v_snipe_all    +2.70 over 1164 rounds, wins 0%   (+0.00 over +0 rounds since last check)
            v_hold_s5    +0.00 over 1009 rounds, wins 0%   (+0.00 over +0 rounds since last check)
            v_x60222032    -7.24 over 1227 rounds, wins 59%   (+0.00 over +0 rounds since last check)
            v_x12229262   -30.87 over 1206 rounds, wins 58%   (+0.00 over +0 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 296.1 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
