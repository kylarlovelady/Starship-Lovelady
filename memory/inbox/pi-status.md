# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 5 hours, 30 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 58%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 21 hours (healthy); homeassistant Up 15 hours

## Sync and schedule
- Pi repo copy at: febdd0d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 16:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (287 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 20 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +620.68 over   48 rounds, wins 58%   (+25.26 over +4 rounds since last check)
            v_x16217721  +479.34 over   63 rounds, wins 35%   (-6.92 over +4 rounds since last check)
            v_x64216771  +458.91 over   83 rounds, wins 47%   (+15.14 over +4 rounds since last check)
            v_x60222031  +428.25 over   48 rounds, wins 60%   (+48.89 over +4 rounds since last check)
            v_x88221261  +421.08 over   55 rounds, wins 31%   (+1.27 over +4 rounds since last check)
            v_x32221881  +392.25 over   47 rounds, wins 51%   (+13.94 over +4 rounds since last check)
            v_x96220872  +283.87 over   48 rounds, wins 44%   (+50.32 over +4 rounds since last check)
            v_hold     +234.68 over  159 rounds, wins 45%   (+42.01 over +4 rounds since last check)
            v_x80218932  +233.57 over   67 rounds, wins 55%   (+30.55 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 2.6 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
