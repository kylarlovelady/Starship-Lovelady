# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 15 hours, 42 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 23%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 40 hours; whisper Up 40 hours (healthy); piper Up 40 hours (healthy); pihole Up 40 hours (healthy); homeassistant Up 40 hours

## Sync and schedule
- Pi repo copy at: 78617ed 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 59 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1426 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 18 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 34 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1016.22 over  847 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  +744.64 over  847 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_hold_s250_wild  +363.54 over  311 rounds, wins 64%   (+278.56 over +3 rounds since last check)
            v_x60222031  +174.14 over 1298 rounds, wins 47%   (-11.71 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1235 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1080 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x64216772   -26.01 over 1333 rounds, wins 58%   (-13.55 over +3 rounds since last check)
            v_x60222032   -56.78 over 1298 rounds, wins 59%   (-13.55 over +3 rounds since last check)
            v_x40223631   -96.47 over 1285 rounds, wins 59%   (-13.55 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 318.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
