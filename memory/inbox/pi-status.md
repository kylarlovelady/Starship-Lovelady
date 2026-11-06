# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 10 hours, 15 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 10 hours; whisper Up 10 hours (healthy); piper Up 10 hours (healthy); pihole Up 10 hours (healthy); homeassistant Up 10 hours

## Sync and schedule
- Pi repo copy at: 7bd2597 29 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 13:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (370 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 6 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +415.63 over  132 rounds, wins 39%   (-16.86 over +4 rounds since last check)
            v_x60222031  +360.09 over  132 rounds, wins 41%   (-5.91 over +4 rounds since last check)
            v_x64216771  +323.38 over  167 rounds, wins 37%   (-12.27 over +4 rounds since last check)
            v_x88221261  +257.07 over  139 rounds, wins 20%   (-6.24 over +4 rounds since last check)
            v_x64216772  +150.49 over  167 rounds, wins 46%   (+23.73 over +4 rounds since last check)
            v_x60222032  +119.72 over  132 rounds, wins 47%   (+23.73 over +4 rounds since last check)
            v_x80218932   +97.90 over  151 rounds, wins 42%   (+33.07 over +4 rounds since last check)
            v_x28219981   +84.47 over  171 rounds, wins 35%   (-7.12 over +4 rounds since last check)
            v_x40223631   +80.03 over  119 rounds, wins 42%   (+23.73 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 23.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
