# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 1 hour, 0 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 59%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 16 hours (healthy); homeassistant Up 10 hours

## Sync and schedule
- Pi repo copy at: 135054d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (267 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 14 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +525.80 over   35 rounds, wins 46%   (-3.87 over +4 rounds since last check)
            v_x96220861  +461.07 over   28 rounds, wins 68%   (+6.61 over +4 rounds since last check)
            v_x32221881  +389.61 over   27 rounds, wins 67%   (+124.88 over +4 rounds since last check)
            v_x64216771  +383.18 over   63 rounds, wins 51%   (+99.17 over +4 rounds since last check)
            v_x60222031  +380.52 over   28 rounds, wins 68%   (+27.50 over +4 rounds since last check)
            v_x28219981  +347.83 over   67 rounds, wins 48%   (-31.64 over +4 rounds since last check)
            v_x32221882  +311.27 over   27 rounds, wins 67%   (-31.64 over +4 rounds since last check)
            v_x52220781  +290.99 over   39 rounds, wins 36%   (-27.71 over +4 rounds since last check)
            v_x219212  +228.15 over   59 rounds, wins 46%   (-107.63 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 6.1 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
