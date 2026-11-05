# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 3 hours, 28 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 57%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 19 hours (healthy); homeassistant Up 13 hours

## Sync and schedule
- Pi repo copy at: a412194 2 minutes ago: KDP design brief
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (21 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 14:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (279 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 6 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +620.12 over   40 rounds, wins 62%   (-53.19 over +4 rounds since last check)
            v_x16217721  +543.64 over   55 rounds, wins 36%   (+34.48 over +4 rounds since last check)
            v_x88221261  +450.86 over   47 rounds, wins 34%   (-8.05 over +4 rounds since last check)
            v_x64216771  +411.83 over   75 rounds, wins 48%   (+73.93 over +4 rounds since last check)
            v_x60222031  +363.28 over   40 rounds, wins 58%   (+12.49 over +4 rounds since last check)
            v_x32221881  +349.53 over   39 rounds, wins 54%   (-8.52 over +4 rounds since last check)
            v_x96220872  +251.88 over   40 rounds, wins 42%   (+89.12 over +4 rounds since last check)
            v_hold     +217.24 over  151 rounds, wins 45%   (+33.29 over +4 rounds since last check)
            v_x52220781  +215.65 over   51 rounds, wins 29%   (-2.35 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 34 min ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
