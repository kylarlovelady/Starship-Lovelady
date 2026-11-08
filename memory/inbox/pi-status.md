# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 6 hours, 15 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 10 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 77f831d 22 minutes ago: Living room: kitchen screen plan
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (545 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 4 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +285.16 over  308 rounds, wins 43%   (+8.31 over +4 rounds since last check)
            v_x60222031  +269.72 over  308 rounds, wins 45%   (-3.80 over +4 rounds since last check)
            v_hold_s250  +187.07 over   90 rounds, wins 64%   (-99.93 over +4 rounds since last check)
            v_hold_s500  +156.13 over   90 rounds, wins 64%   (-207.53 over +4 rounds since last check)
            v_x64216772  +124.65 over  343 rounds, wins 50%   (+4.63 over +4 rounds since last check)
            v_hold_after60  +114.08 over   90 rounds, wins 66%   (+12.82 over +4 rounds since last check)
            v_x60222032   +93.88 over  308 rounds, wins 52%   (+4.63 over +4 rounds since last check)
            v_hold_s100   +89.75 over   90 rounds, wins 64%   (-35.75 over +4 rounds since last check)
            v_hold_s50   +67.11 over   90 rounds, wins 64%   (-14.47 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 36.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
