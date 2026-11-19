# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 14 hours, 12 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 14 hours; whisper Up 14 hours (healthy); piper Up 14 hours (healthy); pihole Up 14 hours (healthy); homeassistant Up 14 hours

## Sync and schedule
- Pi repo copy at: 0653e21 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 01:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    67 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1365 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1427.56 over  773 rounds, wins 13%   (+170.38 over +3 rounds since last check)
            v_edge10_s100_dd  +904.40 over  773 rounds, wins 13%   (+64.07 over +3 rounds since last check)
            v_hold_s250_wild  +670.15 over  237 rounds, wins 62%   (-253.05 over +3 rounds since last check)
            v_x60222031  +227.00 over 1224 rounds, wins 47%   (+23.22 over +3 rounds since last check)
            v_x64216772   +26.81 over 1259 rounds, wins 58%   (-12.67 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1161 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1006 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032    -3.96 over 1224 rounds, wins 59%   (-12.67 over +3 rounds since last check)
            v_x12229262   -17.63 over 1203 rounds, wins 58%   (-28.19 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 292.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
