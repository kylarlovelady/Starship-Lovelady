# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 14 hours, 15 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 38%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 38 hours; whisper Up 38 hours (healthy); piper Up 38 hours (healthy); pihole Up 38 hours (healthy); homeassistant Up 38 hours

## Sync and schedule
- Pi repo copy at: a7b5522 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (482 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 19 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +352.21 over  244 rounds, wins 41%   (-23.65 over +4 rounds since last check)
            v_x60222031  +184.34 over  244 rounds, wins 43%   (-17.30 over +4 rounds since last check)
            v_x64216772  +120.89 over  279 rounds, wins 48%   (-18.53 over +4 rounds since last check)
            v_x40223632  +108.91 over  231 rounds, wins 44%   (+21.48 over +4 rounds since last check)
            v_hold_s100   +90.24 over   26 rounds, wins 69%   (-238.56 over +4 rounds since last check)
            v_x60222032   +90.12 over  244 rounds, wins 49%   (-18.53 over +4 rounds since last check)
            v_hold_s50   +72.49 over   26 rounds, wins 69%   (-117.29 over +4 rounds since last check)
            v_x40223631   +50.43 over  231 rounds, wins 46%   (-18.53 over +4 rounds since last check)
            v_hold_after60   +48.63 over   26 rounds, wins 69%   (-46.74 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 20.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
