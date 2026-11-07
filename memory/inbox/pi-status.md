# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 12 hours, 15 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 38%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 36 hours; whisper Up 36 hours (healthy); piper Up 36 hours (healthy); pihole Up 36 hours (healthy); homeassistant Up 36 hours

## Sync and schedule
- Pi repo copy at: b9cb6f4 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (474 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1467.23 over   18 rounds, wins 83%   (+1029.38 over +4 rounds since last check)
            v_hold_s250 +1052.58 over   18 rounds, wins 83%   (+710.11 over +4 rounds since last check)
            v_hold_s100  +521.70 over   18 rounds, wins 83%   (+281.65 over +4 rounds since last check)
            v_take25_s500  +355.48 over   18 rounds, wins 83%   (+556.03 over +4 rounds since last check)
            v_take25_s250  +315.64 over   18 rounds, wins 83%   (+370.01 over +4 rounds since last check)
            v_x96220861  +314.52 over  236 rounds, wins 41%   (+34.53 over +4 rounds since last check)
            v_hold_s50  +282.97 over   18 rounds, wins 83%   (+138.73 over +4 rounds since last check)
            v_x60222031  +229.86 over  236 rounds, wins 43%   (+27.63 over +4 rounds since last check)
            v_x64216772  +144.05 over  271 rounds, wins 48%   (+14.83 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 18.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
