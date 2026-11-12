# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 15 hours, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 3 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 47 hours (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: 66df04d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 11 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 1 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    92 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (815 total)
      OK    entry_stats.json updated 6 min ago
      OK    exit_rules.json updated 18 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1459.69 over  139 rounds, wins 13%   (+48.97 over +4 rounds since last check)
            v_edge10_s100_dd +1013.96 over  139 rounds, wins 13%   (+24.13 over +4 rounds since last check)
            v_x60222031  +291.35 over  590 rounds, wins 46%   (+2.54 over +4 rounds since last check)
            v_x64216772   +61.05 over  625 rounds, wins 54%   (+8.61 over +4 rounds since last check)
            v_x60222032   +30.28 over  590 rounds, wins 54%   (+8.61 over +4 rounds since last check)
            v_x96220861   +18.45 over  590 rounds, wins 45%   (+57.88 over +4 rounds since last check)
            v_snipe_all    +2.70 over  527 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  372 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631    -9.41 over  577 rounds, wins 54%   (+8.61 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 117.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
