# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 21 hours, 12 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 3 days (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 09f5bda 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 22 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    70 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1575 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 6 min ago
      OK    learn_report.json updated 21 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1414 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1259 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_x64216772  -118.87 over 1512 rounds, wins 57%   (+6.73 over +2 rounds since last check)
            hold       -133.24 over 1615 rounds, wins 58%   (+23.11 over +2 rounds since last check)
            v_snipe    -135.27 over 1415 rounds, wins 27%   (+0.00 over +2 rounds since last check)
            v_x60222032  -149.64 over 1477 rounds, wins 57%   (+6.73 over +2 rounds since last check)
            v_x40223631  -189.33 over 1464 rounds, wins 57%   (+6.73 over +2 rounds since last check)
            v_x60222031  -207.13 over 1477 rounds, wins 46%   (+11.33 over +2 rounds since last check)
            v_edge10_s100_dd  -213.73 over 1026 rounds, wins 12%   (+0.00 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 371.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
