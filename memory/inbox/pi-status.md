# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 2 days, 23 hours, 15 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 9 days (healthy); piper Up 9 days (healthy); pihole Up 6 days (healthy); homeassistant Up 9 days

## Sync and schedule
- Pi repo copy at: c007e0a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 16 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    74 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1160 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 20 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +836.95 over  526 rounds, wins 12%   (+0.00 over +4 rounds since last check)
            v_edge10_s100_dd  +486.50 over  526 rounds, wins 12%   (+0.00 over +4 rounds since last check)
            v_x64216772   +34.55 over 1012 rounds, wins 57%   (-23.16 over +4 rounds since last check)
            v_x60222031   +16.75 over  977 rounds, wins 45%   (+25.39 over +4 rounds since last check)
            v_x60222032    +3.78 over  977 rounds, wins 58%   (-23.16 over +4 rounds since last check)
            v_snipe_all    +2.70 over  914 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  759 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631   -35.91 over  964 rounds, wins 57%   (-23.16 over +4 rounds since last check)
            v_snipe    -113.89 over  915 rounds, wins 29%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 221.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
