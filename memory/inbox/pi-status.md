# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 11 hours, 45 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 30%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 11 days (healthy); piper Up 11 days (healthy); pihole Up 7 days (healthy); homeassistant Up 11 days

## Sync and schedule
- Pi repo copy at: 0e64a20 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 17 Nov 14:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    69 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1266 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 4 min ago
      OK    patterns.json updated 2 min ago
      OK    learn_report.json updated 20 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +535.48 over  657 rounds, wins 12%   (+179.74 over +4 rounds since last check)
            v_edge10_s100_dd  +436.54 over  657 rounds, wins 12%   (+44.53 over +4 rounds since last check)
            v_hold_s250_wild  +101.68 over  121 rounds, wins 64%   (-351.48 over +4 rounds since last check)
            v_x64216772   +66.15 over 1143 rounds, wins 58%   (-13.33 over +4 rounds since last check)
            v_x60222032   +35.38 over 1108 rounds, wins 58%   (-13.33 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1045 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  890 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631    -4.31 over 1095 rounds, wins 58%   (-13.33 over +4 rounds since last check)
            v_x12229262   -94.23 over 1087 rounds, wins 58%   (-51.97 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 258.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
