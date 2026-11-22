# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 11 hours, 12 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 3 days (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 0f94792 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 21 Nov 22:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 2 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    65 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1544 total)
      OK    entry_stats.json updated 7 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100_dd   +67.44 over  991 rounds, wins 12%   (+27.60 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1379 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1224 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x64216772   -69.28 over 1477 rounds, wins 57%   (+25.34 over +4 rounds since last check)
            v_edge10_s100   -79.45 over  991 rounds, wins 12%   (+111.15 over +4 rounds since last check)
            v_x60222032  -100.05 over 1442 rounds, wins 58%   (+25.34 over +4 rounds since last check)
            v_x60222031  -101.45 over 1442 rounds, wins 46%   (+1.57 over +4 rounds since last check)
            hold       -129.69 over 1580 rounds, wins 58%   (+5.97 over +4 rounds since last check)
            v_x40223631  -139.74 over 1429 rounds, wins 57%   (+25.34 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 361.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
