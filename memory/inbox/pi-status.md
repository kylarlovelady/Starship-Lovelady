# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 45 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 41%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 29 hours; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 3 days (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 72fb3c6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 09 Nov 03:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    92 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (615 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 21 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +5244.54 over  162 rounds, wins 62%   (+1973.78 over +4 rounds since last check)
            v_hold_s250 +2591.33 over  162 rounds, wins 62%   (+978.74 over +4 rounds since last check)
            v_hold_s100 +1020.91 over  162 rounds, wins 62%   (+381.72 over +4 rounds since last check)
            v_hold_s50  +509.47 over  162 rounds, wins 62%   (+182.71 over +4 rounds since last check)
            v_hold_s25  +235.74 over  162 rounds, wins 62%   (+82.81 over +4 rounds since last check)
            v_x60222031  +186.70 over  380 rounds, wins 46%   (+40.47 over +4 rounds since last check)
            v_take100  +141.80 over  162 rounds, wins 65%   (+37.98 over +4 rounds since last check)
            v_x64216772  +112.43 over  415 rounds, wins 52%   (+10.04 over +4 rounds since last check)
            v_x96220861  +111.89 over  380 rounds, wins 44%   (+46.98 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 55.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
