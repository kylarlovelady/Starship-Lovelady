# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 3 hours, 15 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 39%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 06edb8e 12 minutes ago: Daily check 2026-11-08: brief, projects, changelog
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 06:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (533 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1271.47 over   78 rounds, wins 65%   (+1058.12 over +4 rounds since last check)
            v_hold_s250  +811.20 over   78 rounds, wins 65%   (+529.06 over +4 rounds since last check)
            v_hold_s100  +368.63 over   78 rounds, wins 65%   (+211.64 over +4 rounds since last check)
            v_x60222031  +331.79 over  296 rounds, wins 45%   (+34.45 over +4 rounds since last check)
            v_x96220861  +290.49 over  296 rounds, wins 43%   (-4.97 over +4 rounds since last check)
            v_hold_s50  +198.02 over   78 rounds, wins 65%   (+105.46 over +4 rounds since last check)
            v_hold_after60  +147.00 over   78 rounds, wins 67%   (+54.14 over +4 rounds since last check)
            v_x64216772  +129.43 over  331 rounds, wins 50%   (+16.17 over +4 rounds since last check)
            v_x60222032   +98.66 over  296 rounds, wins 51%   (+16.17 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 33.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
