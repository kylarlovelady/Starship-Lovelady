# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 22 hours, 30 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 60%; disk 9%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 14 hours (healthy); homeassistant Up 8 hours

## Sync and schedule
- Pi repo copy at: 528671f 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 09:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (259 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 20 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +450.32 over   27 rounds, wins 48%   (+40.29 over +4 rounds since last check)
            v_x52220781  +185.86 over   31 rounds, wins 39%   (+29.46 over +4 rounds since last check)
            v_x96220861  +177.82 over   20 rounds, wins 70%   (+68.41 over +4 rounds since last check)
            v_x219212  +157.16 over   51 rounds, wins 45%   (+57.92 over +4 rounds since last check)
            v_x8220761  +155.78 over   44 rounds, wins 48%   (+25.65 over +4 rounds since last check)
            v_x28219982  +154.92 over   59 rounds, wins 46%   (+92.82 over +4 rounds since last check)
            v_x44219232  +144.62 over   43 rounds, wins 47%   (-17.21 over +4 rounds since last check)
            v_x28219981  +134.72 over   59 rounds, wins 44%   (+61.56 over +4 rounds since last check)
            v_x36215122  +129.76 over   47 rounds, wins 23%   (-7.77 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 3.6 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
