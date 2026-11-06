# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 8 hours, 30 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 60%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 24 hours (healthy); homeassistant Up 18 hours

## Sync and schedule
- Pi repo copy at: 84aed4a 5 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    83 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (299 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +574.73 over   60 rounds, wins 52%   (-31.65 over +4 rounds since last check)
            v_x88221261  +386.70 over   67 rounds, wins 27%   (-10.99 over +4 rounds since last check)
            v_x60222031  +379.54 over   60 rounds, wins 57%   (-30.07 over +4 rounds since last check)
            v_x64216771  +323.51 over   95 rounds, wins 44%   (-45.05 over +4 rounds since last check)
            v_x16217721  +253.81 over   75 rounds, wins 31%   (-99.52 over +4 rounds since last check)
            v_x32221881  +249.53 over   59 rounds, wins 44%   (-61.64 over +4 rounds since last check)
            v_x80218932  +234.51 over   79 rounds, wins 54%   (+0.47 over +4 rounds since last check)
            v_x52220781  +223.90 over   71 rounds, wins 28%   (-14.27 over +4 rounds since last check)
            v_hold     +193.77 over  171 rounds, wins 45%   (+18.16 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 5.6 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
