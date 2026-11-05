# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 21 hours, 30 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 60%; disk 9%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 13 hours (healthy); homeassistant Up 7 hours

## Sync and schedule
- Pi repo copy at: cf0fd11 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (255 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +410.03 over   23 rounds, wins 43%   (+308.34 over +4 rounds since last check)
            v_x44219232  +161.83 over   39 rounds, wins 46%   (-91.72 over +4 rounds since last check)
            v_x52220781  +156.40 over   27 rounds, wins 33%   (+173.01 over +4 rounds since last check)
            v_x36215122  +137.53 over   43 rounds, wins 23%   (+168.87 over +4 rounds since last check)
            v_x8220761  +130.13 over   40 rounds, wins 48%   (-98.25 over +4 rounds since last check)
            v_x96220861  +109.41 over   16 rounds, wins 69%   (+230.14 over +4 rounds since last check)
            v_x16217722  +104.73 over   31 rounds, wins 48%   (-30.33 over +4 rounds since last check)
            v_x80218932   +99.32 over   35 rounds, wins 57%   (-21.48 over +4 rounds since last check)
            v_x219212   +99.24 over   47 rounds, wins 43%   (-94.03 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 2.6 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
