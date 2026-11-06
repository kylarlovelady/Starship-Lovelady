# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 hours, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 32%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 hours; whisper Up 4 hours (healthy); piper Up 4 hours (healthy); pihole Up 4 hours (healthy); homeassistant Up 4 hours

## Sync and schedule
- Pi repo copy at: b49aaf5 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 07:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (347 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +463.76 over  108 rounds, wins 40%   (+62.04 over +4 rounds since last check)
            v_x60222031  +357.26 over  108 rounds, wins 43%   (+16.65 over +4 rounds since last check)
            v_x88221261  +259.43 over  115 rounds, wins 19%   (-6.51 over +4 rounds since last check)
            v_x64216771  +150.32 over  143 rounds, wins 36%   (-53.25 over +4 rounds since last check)
            v_x80218932  +148.59 over  127 rounds, wins 44%   (-18.76 over +4 rounds since last check)
            v_x64216772  +139.16 over  143 rounds, wins 45%   (-10.13 over +4 rounds since last check)
            v_x60222032  +108.39 over  108 rounds, wins 47%   (-10.13 over +4 rounds since last check)
            v_hold     +107.92 over  219 rounds, wins 41%   (-1.55 over +4 rounds since last check)
            v_x24220781   +91.87 over  111 rounds, wins 44%   (-18.76 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 17.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
