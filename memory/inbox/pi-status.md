# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 7 hours, 42 minutes; temp 45.5'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: dcf807d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 3 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    62 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1468 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 21 min ago
      OK    patterns.json updated 19 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +290.51 over  899 rounds, wins 12%   (-99.82 over +4 rounds since last check)
            v_edge10_s100_dd  +117.41 over  899 rounds, wins 12%   (-33.82 over +4 rounds since last check)
            v_x60222031   +68.91 over 1350 rounds, wins 47%   (-8.48 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1287 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1132 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x64216772   -74.08 over 1385 rounds, wins 58%   (+2.54 over +4 rounds since last check)
            v_x60222032  -104.85 over 1350 rounds, wins 58%   (+2.54 over +4 rounds since last check)
            v_snipe    -118.82 over 1288 rounds, wins 27%   (-4.38 over +4 rounds since last check)
            v_x40223631  -144.54 over 1337 rounds, wins 58%   (+2.54 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 334.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
