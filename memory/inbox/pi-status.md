# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 9 hours, 30 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 57%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 25 hours (healthy); homeassistant Up 19 hours

## Sync and schedule
- Pi repo copy at: ed21ec7 14 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    86 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (303 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 12 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +620.05 over   64 rounds, wins 50%   (+45.32 over +4 rounds since last check)
            v_x60222031  +415.41 over   64 rounds, wins 55%   (+35.87 over +4 rounds since last check)
            v_x88221261  +361.43 over   71 rounds, wins 25%   (-25.27 over +4 rounds since last check)
            v_x16217721  +293.89 over   79 rounds, wins 32%   (+40.08 over +4 rounds since last check)
            v_x64216771  +281.93 over   99 rounds, wins 42%   (-41.58 over +4 rounds since last check)
            v_x80218932  +229.63 over   83 rounds, wins 53%   (-4.88 over +4 rounds since last check)
            v_hold     +214.56 over  175 rounds, wins 45%   (+20.79 over +4 rounds since last check)
            v_x32221881  +204.49 over   63 rounds, wins 41%   (-45.04 over +4 rounds since last check)
            v_x52220781  +196.85 over   75 rounds, wins 27%   (-27.05 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 6.6 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
