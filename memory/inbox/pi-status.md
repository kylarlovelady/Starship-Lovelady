# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 7 hours, 9 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 38%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 31 hours; whisper Up 31 hours (healthy); piper Up 31 hours (healthy); pihole Up 31 hours (healthy); homeassistant Up 31 hours

## Sync and schedule
- Pi repo copy at: 1650f0c 5 minutes ago: queue 091: long Kalshi practice review (read-only)
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (16 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 10:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (454 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031  +327.96 over  216 rounds, wins 43%   (-3.94 over +4 rounds since last check)
            v_x96220861  +241.79 over  216 rounds, wins 40%   (-48.37 over +4 rounds since last check)
            v_x88221261  +176.73 over  223 rounds, wins 23%   (+5.29 over +4 rounds since last check)
            v_x64216772  +128.28 over  251 rounds, wins 46%   (-4.00 over +4 rounds since last check)
            v_x60222032   +97.51 over  216 rounds, wins 47%   (-4.00 over +4 rounds since last check)
            v_x40223632   +76.75 over  203 rounds, wins 45%   (-6.41 over +4 rounds since last check)
            v_x40223631   +57.82 over  203 rounds, wins 44%   (-4.00 over +4 rounds since last check)
            v_x12229262   +28.91 over  195 rounds, wins 42%   (-7.00 over +4 rounds since last check)
            v_snipe_all    +2.70 over  153 rounds, wins 1%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 13.8 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
