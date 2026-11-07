# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 45 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 25 hours; whisper Up 25 hours (healthy); piper Up 25 hours (healthy); pihole Up 25 hours (healthy); homeassistant Up 25 hours

## Sync and schedule
- Pi repo copy at: 82be1cd 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 03:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (426 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 11 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +282.99 over  195 rounds, wins 22%   (-51.97 over +4 rounds since last check)
            v_x96220861  +246.43 over  188 rounds, wins 39%   (-32.16 over +4 rounds since last check)
            v_x64216772  +165.43 over  223 rounds, wins 45%   (-9.68 over +4 rounds since last check)
            v_x60222032  +134.66 over  188 rounds, wins 46%   (-9.68 over +4 rounds since last check)
            v_x60222031  +119.86 over  188 rounds, wins 39%   (-32.31 over +4 rounds since last check)
            v_x40223631   +94.97 over  175 rounds, wins 43%   (-9.68 over +4 rounds since last check)
            v_x12229262   +92.66 over  167 rounds, wins 41%   (-3.88 over +4 rounds since last check)
            v_x40223632   +82.06 over  175 rounds, wins 46%   (-0.47 over +4 rounds since last check)
            v_x80218932   +31.73 over  207 rounds, wins 41%   (-2.40 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 7.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
