# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 9 hours, 16 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 33 hours; whisper Up 33 hours (healthy); piper Up 33 hours (healthy); pihole Up 33 hours (healthy); homeassistant Up 33 hours

## Sync and schedule
- Pi repo copy at: 9ea4085 59 seconds ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (24 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (462 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 9 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500  +339.03 over    6 rounds, wins 83%   (+836.14 over +4 rounds since last check)
            v_x60222031  +254.77 over  224 rounds, wins 43%   (-37.72 over +4 rounds since last check)
            v_hold_s250  +253.61 over    6 rounds, wins 83%   (+500.68 over +4 rounds since last check)
            v_hold_s100  +202.25 over    6 rounds, wins 83%   (+299.35 over +4 rounds since last check)
            v_x96220861  +171.11 over  224 rounds, wins 40%   (-36.98 over +4 rounds since last check)
            v_x64216772  +132.92 over  259 rounds, wins 47%   (+13.87 over +4 rounds since last check)
            v_x88221261  +123.72 over  231 rounds, wins 23%   (-3.10 over +4 rounds since last check)
            v_hold_s50  +123.34 over    6 rounds, wins 83%   (+170.59 over +4 rounds since last check)
            v_x60222032  +102.15 over  224 rounds, wins 48%   (+13.87 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 15.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
