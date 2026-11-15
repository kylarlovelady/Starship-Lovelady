# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 19 hours, 45 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 5 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 549f66a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 22:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    82 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1074 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 22 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1204.97 over  423 rounds, wins 13%   (-199.35 over +4 rounds since last check)
            v_edge10_s100_dd  +667.54 over  423 rounds, wins 13%   (-66.96 over +4 rounds since last check)
            v_x64216772   +98.74 over  909 rounds, wins 56%   (-5.18 over +4 rounds since last check)
            v_x60222032   +67.97 over  874 rounds, wins 57%   (-5.18 over +4 rounds since last check)
            v_x40223631   +28.28 over  861 rounds, wins 56%   (-5.18 over +4 rounds since last check)
            v_snipe_all    +2.70 over  811 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  656 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x12229262   -46.55 over  853 rounds, wins 56%   (-19.87 over +4 rounds since last check)
            v_x60222031   -68.15 over  874 rounds, wins 45%   (-43.23 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 194.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
