# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 5 hours, 15 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 20%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 4 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 9f973bc 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    85 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1029 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1908.89 over  369 rounds, wins 14%   (-73.17 over +4 rounds since last check)
            v_edge10_s100_dd  +903.19 over  369 rounds, wins 14%   (-16.58 over +4 rounds since last check)
            v_x64216772  +107.79 over  855 rounds, wins 56%   (-4.76 over +4 rounds since last check)
            v_x60222032   +77.02 over  820 rounds, wins 57%   (-4.76 over +4 rounds since last check)
            v_x40223631   +37.33 over  807 rounds, wins 56%   (-4.76 over +4 rounds since last check)
            v_snipe_all    +2.70 over  757 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  602 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x60222031   -24.55 over  820 rounds, wins 45%   (-5.68 over +4 rounds since last check)
            v_x12229262   -77.90 over  799 rounds, wins 56%   (-4.76 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 179.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
