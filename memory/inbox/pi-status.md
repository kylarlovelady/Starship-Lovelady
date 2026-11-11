# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 22 hours, 15 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 40%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 30 hours (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: 9fb5d9e 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 11 Nov 01:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    88 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (749 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 11 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd  +996.36 over   71 rounds, wins 13%   (-41.68 over +4 rounds since last check)
            v_edge10_s100  +925.64 over   71 rounds, wins 13%   (-83.53 over +4 rounds since last check)
            v_x60222031  +242.17 over  522 rounds, wins 46%   (+66.77 over +4 rounds since last check)
            v_x64216772   +98.14 over  557 rounds, wins 54%   (+15.30 over +4 rounds since last check)
            v_x60222032   +67.37 over  522 rounds, wins 55%   (+15.30 over +4 rounds since last check)
            v_x40223631   +27.68 over  509 rounds, wins 54%   (+15.30 over +4 rounds since last check)
            v_x12229262   +12.26 over  501 rounds, wins 53%   (+105.35 over +4 rounds since last check)
            v_snipe_all    +2.70 over  459 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  304 rounds, wins 0%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 100.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
