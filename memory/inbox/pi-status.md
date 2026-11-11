# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 1 hour, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 40%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 33 hours (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: ab38b36 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 11 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    87 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (760 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +834.92 over   83 rounds, wins 12%   (-21.14 over +4 rounds since last check)
            v_edge10_s100  +605.71 over   83 rounds, wins 12%   (-42.28 over +4 rounds since last check)
            v_x60222031  +202.12 over  534 rounds, wins 45%   (+3.88 over +4 rounds since last check)
            v_x64216772   +86.24 over  569 rounds, wins 53%   (-16.28 over +4 rounds since last check)
            v_x60222032   +55.47 over  534 rounds, wins 54%   (-16.28 over +4 rounds since last check)
            v_x40223631   +15.78 over  521 rounds, wins 53%   (-16.28 over +4 rounds since last check)
            v_snipe_all    +2.70 over  471 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  316 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -44.75 over  316 rounds, wins 59%   (-11.82 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 103.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
