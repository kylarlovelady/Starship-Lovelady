# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 4 hours, 45 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 29 hours; whisper Up 29 hours (healthy); piper Up 29 hours (healthy); pihole Up 29 hours (healthy); homeassistant Up 29 hours

## Sync and schedule
- Pi repo copy at: 7088024 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 07:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (442 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +324.34 over  204 rounds, wins 40%   (-51.58 over +4 rounds since last check)
            v_x60222031  +275.67 over  204 rounds, wins 42%   (-22.05 over +4 rounds since last check)
            v_x88221261  +222.82 over  211 rounds, wins 23%   (-30.44 over +4 rounds since last check)
            v_x64216772  +144.69 over  239 rounds, wins 46%   (-0.04 over +4 rounds since last check)
            v_x60222032  +113.92 over  204 rounds, wins 47%   (-0.04 over +4 rounds since last check)
            v_x12229262   +81.28 over  183 rounds, wins 42%   (+5.10 over +4 rounds since last check)
            v_x40223631   +74.23 over  191 rounds, wins 43%   (-0.04 over +4 rounds since last check)
            v_x40223632   +45.57 over  191 rounds, wins 45%   (-7.68 over +4 rounds since last check)
            v_snipe_all    +2.70 over  141 rounds, wins 1%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 11.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
