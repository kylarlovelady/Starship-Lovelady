# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 1 hour, 42 minutes; temp 45.5'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 4 days (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: 450d319 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 22 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    69 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1587 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 18 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1428 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1273 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x64216772   -98.76 over 1526 rounds, wins 57%   (+15.26 over +3 rounds since last check)
            v_x60222032  -129.53 over 1491 rounds, wins 57%   (+15.26 over +3 rounds since last check)
            hold       -134.50 over 1629 rounds, wins 58%   (-18.39 over +3 rounds since last check)
            v_snipe    -134.96 over 1429 rounds, wins 27%   (+0.00 over +3 rounds since last check)
            v_x60222031  -163.98 over 1491 rounds, wins 46%   (+18.76 over +3 rounds since last check)
            v_x40223631  -169.22 over 1478 rounds, wins 57%   (+15.26 over +3 rounds since last check)
            v_edge10_s100_dd  -207.33 over 1040 rounds, wins 12%   (+16.84 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 376.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
