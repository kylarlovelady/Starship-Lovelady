# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 22 hours, 42 minutes; temp 45.5'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 5 days (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: a2d3820 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 24 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    61 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1705 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 4 min ago
      OK    learn_report.json updated 2 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1563 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1408 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_snipe    -141.99 over 1564 rounds, wins 26%   (+1.17 over +4 rounds since last check)
            v_x64216772  -176.12 over 1661 rounds, wins 56%   (+2.16 over +4 rounds since last check)
            hold       -190.56 over 1764 rounds, wins 59%   (-2.54 over +4 rounds since last check)
            v_x60222032  -206.89 over 1626 rounds, wins 57%   (+2.16 over +4 rounds since last check)
            v_x40223631  -246.58 over 1613 rounds, wins 56%   (+2.16 over +4 rounds since last check)
            v_hold_s10  -296.16 over 1408 rounds, wins 58%   (+8.27 over +4 rounds since last check)
            v_take25_s10  -386.33 over 1408 rounds, wins 69%   (+4.02 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 421.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
