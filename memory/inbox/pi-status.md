# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 7 hours, 52 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 59%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 23 hours (healthy); homeassistant Up 17 hours

## Sync and schedule
- Pi repo copy at: c11a0f8 4 minutes ago: Queue 049: run keyword scan in background
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (45 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    79 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (295 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 14 min ago
      OK    patterns.json updated 13 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +606.38 over   56 rounds, wins 54%   (-13.13 over +4 rounds since last check)
            v_x60222031  +409.61 over   56 rounds, wins 57%   (-36.58 over +4 rounds since last check)
            v_x88221261  +397.69 over   63 rounds, wins 29%   (-6.51 over +4 rounds since last check)
            v_x64216771  +368.56 over   91 rounds, wins 44%   (-21.87 over +4 rounds since last check)
            v_x16217721  +353.33 over   71 rounds, wins 32%   (-44.55 over +4 rounds since last check)
            v_x32221881  +311.17 over   55 rounds, wins 45%   (-20.66 over +4 rounds since last check)
            v_x52220781  +238.17 over   67 rounds, wins 30%   (-6.61 over +4 rounds since last check)
            v_x80218932  +234.04 over   75 rounds, wins 55%   (+25.08 over +4 rounds since last check)
            v_x96220872  +187.27 over   56 rounds, wins 39%   (-52.47 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 5.0 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
