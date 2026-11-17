# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 12 hours, 45 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 28%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 days; whisper Up 11 days (healthy); piper Up 11 days (healthy); pihole Up 7 days (healthy); homeassistant Up 11 days

## Sync and schedule
- Pi repo copy at: 3a3cad0 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Tue 17 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    67 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1268 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +1081.21 over  123 rounds, wins 64%   (+979.53 over +2 rounds since last check)
            v_edge10_s100  +493.20 over  659 rounds, wins 12%   (-42.28 over +2 rounds since last check)
            v_edge10_s100_dd  +426.05 over  659 rounds, wins 12%   (-10.49 over +2 rounds since last check)
            v_x64216772   +72.18 over 1145 rounds, wins 58%   (+6.03 over +2 rounds since last check)
            v_x60222032   +41.41 over 1110 rounds, wins 58%   (+6.03 over +2 rounds since last check)
            v_snipe_all    +2.70 over 1047 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_x40223631    +1.72 over 1097 rounds, wins 58%   (+6.03 over +2 rounds since last check)
            v_hold_s5    +0.00 over  892 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_x12229262   -88.20 over 1089 rounds, wins 58%   (+6.03 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 259.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
