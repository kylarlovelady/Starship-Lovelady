# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 4 hours, 15 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 5d6170a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 07:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (537 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1509.31 over   82 rounds, wins 66%   (+237.84 over +4 rounds since last check)
            v_hold_s250  +932.64 over   82 rounds, wins 66%   (+121.44 over +4 rounds since last check)
            v_hold_s100  +420.73 over   82 rounds, wins 66%   (+52.10 over +4 rounds since last check)
            v_x60222031  +311.58 over  300 rounds, wins 45%   (-20.21 over +4 rounds since last check)
            v_x96220861  +279.98 over  300 rounds, wins 43%   (-10.51 over +4 rounds since last check)
            v_hold_s50  +227.02 over   82 rounds, wins 66%   (+29.00 over +4 rounds since last check)
            v_hold_after60  +145.13 over   82 rounds, wins 67%   (-1.87 over +4 rounds since last check)
            v_x64216772  +136.68 over  335 rounds, wins 50%   (+7.25 over +4 rounds since last check)
            v_hold_s25  +109.81 over   82 rounds, wins 66%   (+16.80 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 34.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
