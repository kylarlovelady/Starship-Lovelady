# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 14 hours, 49 minutes; temp 38.9'C; throttled flags 0x0 (0x0 is clean); memory 57%; disk 9%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 6 hours (healthy); homeassistant Up 2 minutes

## Sync and schedule
- Pi repo copy at: a8fbcf9 4 minutes ago: HA installer uses sudo for root-owned config; first task-queue diagnostic; changelog
- last notes sync result: notes pushed to the repo
- cron jobs (script names): e.sh, g.py, r.py, b.py, c.sh, k.py, c.sh, r.sh

## Markets agent (practice money)
- data last written: no file; live flags: {}
- supervisor report (42 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 01:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    87 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (235 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x8220761  +148.21 over   20 rounds, wins 40%   (+90.43 over +4 rounds since last check)
            v_x44219232  +143.54 over   19 rounds, wins 37%   (+88.50 over +4 rounds since last check)
            v_x219212   +86.96 over   27 rounds, wins 33%   (+88.50 over +4 rounds since last check)
            v_x44219231   +77.74 over   19 rounds, wins 32%   (+88.50 over +4 rounds since last check)
            v_x72222452   +59.58 over   20 rounds, wins 30%   (+88.50 over +4 rounds since last check)
            v_x80218932   +32.30 over   15 rounds, wins 40%   (+6.35 over +4 rounds since last check)
            v_x88221262   +31.80 over    3 rounds, wins 67%
            v_x36215122   +21.82 over   23 rounds, wins 13%   (-26.50 over +4 rounds since last check)
            v_x64216772   +21.71 over   31 rounds, wins 35%   (+1.85 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: no file
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole did not answer from the Pi, or it needs a login I do not have.

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
