# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 17 hours, 45 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 2 days (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: 90c1ac8 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 11 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 1 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    92 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (823 total)
      OK    entry_stats.json updated 6 min ago
      OK    exit_rules.json updated 5 min ago
      OK    patterns.json updated 4 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1885.52 over  147 rounds, wins 14%   (+495.45 over +4 rounds since last check)
            v_edge10_s100_dd +1273.43 over  147 rounds, wins 14%   (+301.75 over +4 rounds since last check)
            v_x60222031  +360.28 over  598 rounds, wins 46%   (+78.11 over +4 rounds since last check)
            v_x96220861   +85.07 over  598 rounds, wins 45%   (+82.32 over +4 rounds since last check)
            v_x64216772   +65.90 over  633 rounds, wins 54%   (+16.99 over +4 rounds since last check)
            v_x60222032   +35.13 over  598 rounds, wins 55%   (+16.99 over +4 rounds since last check)
            v_hold_after120    +2.96 over  380 rounds, wins 64%   (+107.63 over +4 rounds since last check)
            v_snipe_all    +2.70 over  535 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  380 rounds, wins 0%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 120.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
