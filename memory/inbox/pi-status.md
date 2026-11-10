# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 9 hours, 45 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 18 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: cb93886 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    61 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (700 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 6 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031  +197.36 over  470 rounds, wins 45%   (-44.26 over +4 rounds since last check)
            v_edge10_s100_dd  +138.51 over   19 rounds, wins 5%   (-63.54 over +4 rounds since last check)
            v_edge10_s100  +117.33 over   19 rounds, wins 5%   (-84.72 over +4 rounds since last check)
            v_x64216772  +100.05 over  505 rounds, wins 53%   (-7.37 over +4 rounds since last check)
            v_x60222032   +69.28 over  470 rounds, wins 54%   (-7.37 over +4 rounds since last check)
            v_x40223631   +29.59 over  457 rounds, wins 53%   (-7.37 over +4 rounds since last check)
            v_snipe_all    +2.70 over  407 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  252 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -14.56 over  252 rounds, wins 61%   (-12.96 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 88.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
