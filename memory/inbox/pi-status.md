# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 12 hours, 16 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 34%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 12 hours; whisper Up 12 hours (healthy); piper Up 12 hours (healthy); pihole Up 12 hours (healthy); homeassistant Up 12 hours

## Sync and schedule
- Pi repo copy at: 79b2536 40 seconds ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (378 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +381.71 over  140 rounds, wins 40%   (-14.51 over +4 rounds since last check)
            v_x60222031  +301.99 over  140 rounds, wins 41%   (+2.81 over +4 rounds since last check)
            v_x64216771  +239.14 over  175 rounds, wins 37%   (-8.98 over +4 rounds since last check)
            v_x88221261  +231.99 over  147 rounds, wins 20%   (-17.43 over +4 rounds since last check)
            v_x64216772  +121.16 over  175 rounds, wins 45%   (-7.51 over +4 rounds since last check)
            v_x80218932   +93.87 over  159 rounds, wins 43%   (-23.09 over +4 rounds since last check)
            v_x60222032   +90.39 over  140 rounds, wins 46%   (-7.51 over +4 rounds since last check)
            v_x40223632   +80.58 over  127 rounds, wins 45%   (+25.26 over +4 rounds since last check)
            v_x52220781   +62.94 over  151 rounds, wins 22%   (+8.37 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 25.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
