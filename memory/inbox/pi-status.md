# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 12 hours, 15 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 16 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: ea02965 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (569 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 9 min ago
      OK    patterns.json updated 8 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +4385.37 over  114 rounds, wins 65%   (+1938.91 over +4 rounds since last check)
            v_hold_s250 +2285.10 over  114 rounds, wins 65%   (+962.89 over +4 rounds since last check)
            v_hold_s100  +909.67 over  114 rounds, wins 65%   (+377.77 over +4 rounds since last check)
            v_hold_s50  +459.60 over  114 rounds, wins 65%   (+181.89 over +4 rounds since last check)
            v_x96220861  +288.08 over  332 rounds, wins 43%   (+36.35 over +4 rounds since last check)
            v_x60222031  +229.81 over  332 rounds, wins 46%   (-4.99 over +4 rounds since last check)
            v_hold_s25  +216.35 over  114 rounds, wins 65%   (+85.06 over +4 rounds since last check)
            v_take100  +119.18 over  114 rounds, wins 66%   (+19.85 over +4 rounds since last check)
            v_x64216772  +118.86 over  367 rounds, wins 51%   (+12.80 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 42.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
