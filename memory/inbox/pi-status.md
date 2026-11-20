# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 7 hours, 12 minutes; temp 46.1'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 31 hours; whisper Up 31 hours (healthy); piper Up 31 hours (healthy); pihole Up 31 hours (healthy); homeassistant Up 31 hours

## Sync and schedule
- Pi repo copy at: 0d0f7e7 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 1 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 58 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1405 total)
      OK    entry_stats.json updated 6 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +873.39 over  821 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  +588.14 over  821 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_hold_s250_wild  +279.86 over  285 rounds, wins 64%   (-0.66 over +3 rounds since last check)
            v_x60222031  +166.60 over 1272 rounds, wins 47%   (+77.79 over +3 rounds since last check)
            v_x64216772   +23.60 over 1307 rounds, wins 59%   (-0.66 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1209 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1054 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032    -7.17 over 1272 rounds, wins 59%   (-0.66 over +3 rounds since last check)
            v_x40223631   -46.86 over 1259 rounds, wins 59%   (-0.66 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 309.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
