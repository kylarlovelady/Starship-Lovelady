# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 16 hours, 52 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 42%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 45 hours; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 43 minutes (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 0f10f2b 2 minutes ago: Kalshi: signal check tool + queue 106 (read-only)
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (0 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 09 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 51 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (641 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +5385.24 over  188 rounds, wins 63%   (+2.01 over +3 rounds since last check)
            v_hold_s250 +2633.13 over  188 rounds, wins 63%   (+2.01 over +3 rounds since last check)
            v_hold_s100 +1050.33 over  188 rounds, wins 63%   (+2.01 over +3 rounds since last check)
            v_hold_s50  +534.84 over  188 rounds, wins 63%   (+2.01 over +3 rounds since last check)
            v_hold_s25  +259.39 over  188 rounds, wins 63%   (+2.01 over +3 rounds since last check)
            v_x60222031  +178.87 over  406 rounds, wins 46%   (-72.81 over +3 rounds since last check)
            v_x64216772  +158.31 over  441 rounds, wins 53%   (+1.70 over +3 rounds since last check)
            v_x60222032  +127.54 over  406 rounds, wins 54%   (+1.70 over +3 rounds since last check)
            v_x96220861  +125.00 over  406 rounds, wins 45%   (-8.58 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 71.5 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
