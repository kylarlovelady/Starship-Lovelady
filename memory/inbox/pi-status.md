# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 15 hours, 42 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 96a2d83 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 21 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    62 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1489 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 18 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd   +26.69 over  922 rounds, wins 12%   (+168.89 over +3 rounds since last check)
            v_x60222031    +9.16 over 1373 rounds, wins 47%   (-19.13 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1310 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1155 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_edge10_s100  -101.87 over  922 rounds, wins 12%   (+248.36 over +3 rounds since last check)
            v_x64216772  -103.92 over 1408 rounds, wins 57%   (-25.86 over +3 rounds since last check)
            v_snipe    -118.30 over 1311 rounds, wins 27%   (+1.32 over +3 rounds since last check)
            v_x60222032  -134.69 over 1373 rounds, wins 58%   (-25.86 over +3 rounds since last check)
            v_x40223631  -174.38 over 1360 rounds, wins 58%   (-25.86 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 342.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
