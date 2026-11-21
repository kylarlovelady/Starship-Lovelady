# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 18 hours, 12 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 days; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 3d47b2f 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 21 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    63 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1496 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x60222031   +49.93 over 1381 rounds, wins 47%   (+1.21 over +3 rounds since last check)
            v_edge10_s100_dd   +39.68 over  930 rounds, wins 12%   (+35.45 over +3 rounds since last check)
            v_edge10_s100    +6.71 over  930 rounds, wins 12%   (+92.64 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1318 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1163 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x64216772   -99.68 over 1416 rounds, wins 57%   (+14.41 over +3 rounds since last check)
            v_snipe    -116.02 over 1319 rounds, wins 27%   (+0.36 over +3 rounds since last check)
            v_x60222032  -130.45 over 1381 rounds, wins 58%   (+14.41 over +3 rounds since last check)
            v_x40223631  -170.14 over 1368 rounds, wins 57%   (+14.41 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 344.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
