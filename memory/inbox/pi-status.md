# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 19 hours, 45 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 44 hours; whisper Up 44 hours (healthy); piper Up 44 hours (healthy); pihole Up 44 hours (healthy); homeassistant Up 44 hours

## Sync and schedule
- Pi repo copy at: 19ec94c 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 22:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (502 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +255.36 over  264 rounds, wins 41%   (-47.73 over +4 rounds since last check)
            v_x60222031  +242.28 over  264 rounds, wins 43%   (-18.27 over +4 rounds since last check)
            v_hold_s250  +211.97 over   46 rounds, wins 67%   (-21.97 over +4 rounds since last check)
            v_hold_s100  +191.68 over   46 rounds, wins 67%   (-6.71 over +4 rounds since last check)
            v_hold_after60  +174.60 over   46 rounds, wins 70%   (+0.29 over +4 rounds since last check)
            v_hold_after120  +129.90 over   46 rounds, wins 65%   (-19.63 over +4 rounds since last check)
            v_x64216772  +123.95 over  299 rounds, wins 49%   (+2.86 over +4 rounds since last check)
            v_hold_s50  +122.35 over   46 rounds, wins 67%   (-1.73 over +4 rounds since last check)
            v_x60222032   +93.18 over  264 rounds, wins 50%   (+2.86 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 26.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
