# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 hour, 42 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 2 hours; whisper Up 2 hours (healthy); piper Up 2 hours (healthy); pihole Up 2 hours (healthy); homeassistant Up 2 hours

## Sync and schedule
- Pi repo copy at: 1b612cc 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    66 of the last 96 rounds were settled by Kalshi and logged
      OK    +6 new written lessons since the last check (1327 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 23 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +2889.34 over  194 rounds, wins 65%   (+329.83 over +6 rounds since last check)
            v_edge10_s100  +995.38 over  730 rounds, wins 12%   (-26.27 over +6 rounds since last check)
            v_edge10_s100_dd  +794.27 over  730 rounds, wins 12%   (-3.69 over +6 rounds since last check)
            v_x60222031  +146.46 over 1181 rounds, wins 47%   (+32.08 over +6 rounds since last check)
            v_x64216772   +70.61 over 1216 rounds, wins 58%   (+22.59 over +6 rounds since last check)
            v_x12229262   +49.06 over 1160 rounds, wins 58%   (+51.06 over +6 rounds since last check)
            v_x60222032   +39.84 over 1181 rounds, wins 59%   (+22.59 over +6 rounds since last check)
            v_snipe_all    +2.70 over 1118 rounds, wins 0%   (+0.00 over +6 rounds since last check)
            v_x40223631    +0.15 over 1168 rounds, wins 59%   (+22.59 over +6 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 280.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
