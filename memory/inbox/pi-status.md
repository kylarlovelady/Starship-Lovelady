# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 16 hours, 15 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 41%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 20 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: c5d09e8 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (585 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +4784.41 over  130 rounds, wins 65%   (-490.16 over +4 rounds since last check)
            v_hold_s250 +2369.85 over  130 rounds, wins 65%   (-240.11 over +4 rounds since last check)
            v_hold_s100  +941.23 over  130 rounds, wins 65%   (-90.19 over +4 rounds since last check)
            v_hold_s50  +477.92 over  130 rounds, wins 65%   (-40.21 over +4 rounds since last check)
            v_x96220861  +328.21 over  348 rounds, wins 44%   (+15.25 over +4 rounds since last check)
            v_x60222031  +297.36 over  348 rounds, wins 46%   (-37.02 over +4 rounds since last check)
            v_hold_after120  +231.64 over  130 rounds, wins 65%   (+11.17 over +4 rounds since last check)
            v_hold_s25  +228.41 over  130 rounds, wins 65%   (-15.14 over +4 rounds since last check)
            v_take100  +215.64 over  130 rounds, wins 67%   (+55.92 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 46.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
