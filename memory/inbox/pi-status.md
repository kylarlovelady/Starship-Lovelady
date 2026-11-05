# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 0 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 59%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 15 hours (healthy); homeassistant Up 9 hours

## Sync and schedule
- Pi repo copy at: 38de54a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 10:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (263 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +529.67 over   31 rounds, wins 48%   (+79.35 over +4 rounds since last check)
            v_x96220861  +454.46 over   24 rounds, wins 71%   (+276.64 over +4 rounds since last check)
            v_x28219981  +379.47 over   63 rounds, wins 48%   (+244.75 over +4 rounds since last check)
            v_x60222031  +353.02 over   24 rounds, wins 71%   (+271.70 over +4 rounds since last check)
            v_x32221882  +342.91 over   23 rounds, wins 70%   (+244.75 over +4 rounds since last check)
            v_x219212  +335.78 over   55 rounds, wins 47%   (+178.62 over +4 rounds since last check)
            v_x44219232  +323.24 over   47 rounds, wins 49%   (+178.62 over +4 rounds since last check)
            v_x52220781  +318.70 over   35 rounds, wins 40%   (+132.84 over +4 rounds since last check)
            v_x72222451  +297.04 over   48 rounds, wins 44%   (+284.92 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 5.1 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
