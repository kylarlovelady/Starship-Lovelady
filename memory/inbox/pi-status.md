# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 7 hours, 45 minutes; temp 38.9'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 16 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: e3e4938 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 10 Nov 10:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 53 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (692 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +286.39 over   11 rounds, wins 9%   (-99.93 over +4 rounds since last check)
            v_edge10_s100_dd  +286.39 over   11 rounds, wins 9%   (-99.93 over +4 rounds since last check)
            v_hold_s250  +278.13 over  244 rounds, wins 61%   (+233.52 over +4 rounds since last check)
            v_x60222031  +230.45 over  462 rounds, wins 45%   (-6.60 over +4 rounds since last check)
            v_x64216772  +100.02 over  497 rounds, wins 53%   (+13.98 over +4 rounds since last check)
            v_x60222032   +69.25 over  462 rounds, wins 54%   (+13.98 over +4 rounds since last check)
            v_hold_s100   +43.94 over  244 rounds, wins 61%   (+98.85 over +4 rounds since last check)
            v_hold_s50   +40.80 over  244 rounds, wins 61%   (+54.44 over +4 rounds since last check)
            v_x40223631   +29.56 over  449 rounds, wins 53%   (+13.98 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 86.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
