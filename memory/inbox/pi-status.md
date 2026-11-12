# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 6 days, 1 hour, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 31%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 2 days (healthy); homeassistant Up 6 days

## Sync and schedule
- Pi repo copy at: a24218a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 12 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    82 of the last 96 rounds were settled by Kalshi and logged
      STUCK +0 new written lessons since the last check (844 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1872.61 over  169 rounds, wins 17%   (+0.00 over +0 rounds since last check)
            v_edge10_s100_dd +1210.40 over  169 rounds, wins 17%   (+0.00 over +0 rounds since last check)
            v_x60222031  +195.68 over  620 rounds, wins 46%   (+0.00 over +0 rounds since last check)
            v_x96220861  +182.54 over  620 rounds, wins 46%   (+0.00 over +0 rounds since last check)
            v_x64216772   +98.46 over  655 rounds, wins 54%   (+0.00 over +0 rounds since last check)
            v_x60222032   +67.69 over  620 rounds, wins 55%   (+0.00 over +0 rounds since last check)
            v_x12229262   +34.57 over  599 rounds, wins 54%   (+0.00 over +0 rounds since last check)
            v_x40223631   +28.00 over  607 rounds, wins 54%   (+0.00 over +0 rounds since last check)
            v_snipe_all    +2.70 over  557 rounds, wins 0%   (+0.00 over +0 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 127.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
