# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 2 hours, 45 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 27 hours; whisper Up 27 hours (healthy); piper Up 27 hours (healthy); pihole Up 27 hours (healthy); homeassistant Up 27 hours

## Sync and schedule
- Pi repo copy at: f330d18 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (434 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +305.82 over  196 rounds, wins 39%   (+85.98 over +4 rounds since last check)
            v_x60222031  +288.30 over  196 rounds, wins 41%   (+159.61 over +4 rounds since last check)
            v_x88221261  +255.92 over  203 rounds, wins 23%   (+25.95 over +4 rounds since last check)
            v_x64216772  +158.09 over  231 rounds, wins 45%   (-4.42 over +4 rounds since last check)
            v_x60222032  +127.32 over  196 rounds, wins 46%   (-4.42 over +4 rounds since last check)
            v_x12229262  +117.94 over  175 rounds, wins 41%   (+48.86 over +4 rounds since last check)
            v_x40223631   +87.63 over  183 rounds, wins 43%   (-4.42 over +4 rounds since last check)
            v_x40223632   +22.73 over  183 rounds, wins 44%   (-22.54 over +4 rounds since last check)
            v_x80218932   +15.50 over  215 rounds, wins 41%   (-8.73 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 9.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
