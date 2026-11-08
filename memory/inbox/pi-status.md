# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 8 hours, 45 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 13 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 264fc2d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (553 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031  +203.76 over  316 rounds, wins 45%   (-30.50 over +4 rounds since last check)
            v_x96220861  +187.88 over  316 rounds, wins 42%   (-54.75 over +4 rounds since last check)
            v_x64216772  +103.86 over  351 rounds, wins 50%   (-17.97 over +4 rounds since last check)
            v_x60222032   +73.09 over  316 rounds, wins 51%   (-17.97 over +4 rounds since last check)
            v_hold_after120   +37.33 over   98 rounds, wins 62%   (-25.34 over +4 rounds since last check)
            v_x40223631   +33.40 over  303 rounds, wins 50%   (-17.97 over +4 rounds since last check)
            v_x40223632   +32.77 over  303 rounds, wins 44%   (+7.37 over +4 rounds since last check)
            v_take100   +31.38 over   98 rounds, wins 64%   (-6.95 over +4 rounds since last check)
            v_hold_s50   +26.21 over   98 rounds, wins 63%   (-10.69 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 39.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
