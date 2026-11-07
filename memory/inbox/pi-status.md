# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 13 hours, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 38%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 37 hours; whisper Up 37 hours (healthy); piper Up 37 hours (healthy); pihole Up 37 hours (healthy); homeassistant Up 37 hours

## Sync and schedule
- Pi repo copy at: 1d82237 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 16:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (478 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 5 min ago
      OK    patterns.json updated 3 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250  +559.24 over   22 rounds, wins 77%   (-493.34 over +4 rounds since last check)
            v_hold_s500  +474.04 over   22 rounds, wins 77%   (-993.19 over +4 rounds since last check)
            v_x96220861  +375.86 over  240 rounds, wins 41%   (+61.34 over +4 rounds since last check)
            v_hold_s100  +328.80 over   22 rounds, wins 77%   (-192.90 over +4 rounds since last check)
            v_x60222031  +201.64 over  240 rounds, wins 43%   (-28.22 over +4 rounds since last check)
            v_hold_s50  +189.78 over   22 rounds, wins 77%   (-93.19 over +4 rounds since last check)
            v_x64216772  +139.42 over  275 rounds, wins 48%   (-4.63 over +4 rounds since last check)
            v_x60222032  +108.65 over  240 rounds, wins 49%   (-4.63 over +4 rounds since last check)
            v_hold_after60   +95.37 over   22 rounds, wins 77%   (-43.25 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 19.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
