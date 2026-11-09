# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 1 hour, 45 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 41%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 30 hours; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 3 days (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: a6c7b21 15 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 09 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    93 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (619 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +6434.78 over  166 rounds, wins 62%   (+1190.24 over +4 rounds since last check)
            v_hold_s250 +3139.41 over  166 rounds, wins 62%   (+548.08 over +4 rounds since last check)
            v_hold_s100 +1230.90 over  166 rounds, wins 62%   (+209.99 over +4 rounds since last check)
            v_hold_s50  +606.54 over  166 rounds, wins 62%   (+97.07 over +4 rounds since last check)
            v_hold_s25  +276.77 over  166 rounds, wins 62%   (+41.03 over +4 rounds since last check)
            v_x60222031  +245.95 over  384 rounds, wins 46%   (+59.25 over +4 rounds since last check)
            v_take100  +128.23 over  166 rounds, wins 64%   (-13.57 over +4 rounds since last check)
            v_x64216772  +108.47 over  419 rounds, wins 52%   (-3.96 over +4 rounds since last check)
            v_x96220861   +90.36 over  384 rounds, wins 44%   (-21.53 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 56.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
