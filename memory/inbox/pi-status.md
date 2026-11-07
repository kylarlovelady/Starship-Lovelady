# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 10 hours, 45 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 38%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 35 hours; whisper Up 35 hours (healthy); piper Up 35 hours (healthy); pihole Up 35 hours (healthy); homeassistant Up 35 hours

## Sync and schedule
- Pi repo copy at: e73fd0d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 13:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (466 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031  +227.12 over  228 rounds, wins 43%   (-27.65 over +4 rounds since last check)
            v_x96220861  +175.17 over  228 rounds, wins 40%   (+4.06 over +4 rounds since last check)
            v_x64216772  +122.95 over  263 rounds, wins 47%   (-9.97 over +4 rounds since last check)
            v_x60222032   +92.18 over  228 rounds, wins 48%   (-9.97 over +4 rounds since last check)
            v_x40223632   +81.26 over  215 rounds, wins 44%   (-10.41 over +4 rounds since last check)
            v_x88221261   +69.64 over  235 rounds, wins 23%   (-54.08 over +4 rounds since last check)
            v_x40223631   +52.49 over  215 rounds, wins 45%   (-9.97 over +4 rounds since last check)
            v_hold_s100   +51.62 over   10 rounds, wins 70%   (-150.63 over +4 rounds since last check)
            v_hold_s50   +50.08 over   10 rounds, wins 70%   (-73.26 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 17.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
