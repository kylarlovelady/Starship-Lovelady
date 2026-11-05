# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 2 hours, 22 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 57%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 18 hours (healthy); homeassistant Up 12 hours

## Sync and schedule
- Pi repo copy at: fefb480 2 minutes ago: queue 023: verify Kalshi changes
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (15 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 13:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (275 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +673.31 over   36 rounds, wins 67%   (+168.81 over +4 rounds since last check)
            v_x16217721  +509.16 over   51 rounds, wins 35%   (+592.80 over +4 rounds since last check)
            v_x88221261  +458.91 over   43 rounds, wins 37%   (-53.39 over +4 rounds since last check)
            v_x32221881  +358.05 over   35 rounds, wins 57%   (+115.61 over +4 rounds since last check)
            v_x60222031  +350.79 over   36 rounds, wins 61%   (-70.37 over +4 rounds since last check)
            v_x64216771  +337.90 over   71 rounds, wins 48%   (+114.95 over +4 rounds since last check)
            v_x80218932  +219.76 over   55 rounds, wins 58%   (+63.66 over +4 rounds since last check)
            v_x52220781  +218.00 over   47 rounds, wins 30%   (-67.51 over +4 rounds since last check)
            v_hold     +183.95 over  147 rounds, wins 46%   (+135.97 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 7.4 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
