# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 4 hours, 42 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 22%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 29 hours; whisper Up 29 hours (healthy); piper Up 29 hours (healthy); pihole Up 29 hours (healthy); homeassistant Up 29 hours

## Sync and schedule
- Pi repo copy at: 0a85f85 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 58 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1397 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1003.35 over  811 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  +724.54 over  811 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_hold_s250_wild  +375.13 over  275 rounds, wins 64%   (-6.05 over +3 rounds since last check)
            v_x60222031  +115.26 over 1262 rounds, wins 47%   (-27.80 over +3 rounds since last check)
            v_x64216772   +25.11 over 1297 rounds, wins 59%   (-9.75 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1199 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1044 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032    -5.66 over 1262 rounds, wins 59%   (-9.75 over +3 rounds since last check)
            v_x40223631   -45.35 over 1249 rounds, wins 59%   (-9.75 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 307.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
