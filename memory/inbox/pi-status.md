# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 7 hours, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 40%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 39 hours (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: e3c9349 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 11 Nov 10:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    91 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (784 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 4 min ago
      OK    patterns.json updated 2 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +774.99 over  107 rounds, wins 11%   (-34.03 over +4 rounds since last check)
            v_edge10_s100  +702.34 over  107 rounds, wins 11%   (-99.83 over +4 rounds since last check)
            v_x60222031  +262.24 over  558 rounds, wins 46%   (-39.59 over +4 rounds since last check)
            v_x64216772   +76.19 over  593 rounds, wins 53%   (+3.98 over +4 rounds since last check)
            v_x60222032   +45.42 over  558 rounds, wins 54%   (+3.98 over +4 rounds since last check)
            v_x40223631    +5.73 over  545 rounds, wins 53%   (+3.98 over +4 rounds since last check)
            v_snipe_all    +2.70 over  495 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  340 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -77.61 over  340 rounds, wins 58%   (-6.22 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 109.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
