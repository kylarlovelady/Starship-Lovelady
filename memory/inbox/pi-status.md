# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 2 hours, 15 minutes; temp 38.9'C; throttled flags 0x0 (0x0 is clean); memory 41%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 30 hours; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 3 days (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: f44258f 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 09 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    93 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (623 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +6406.92 over  170 rounds, wins 62%   (-27.86 over +4 rounds since last check)
            v_hold_s250 +3128.50 over  170 rounds, wins 62%   (-10.91 over +4 rounds since last check)
            v_hold_s100 +1230.09 over  170 rounds, wins 62%   (-0.81 over +4 rounds since last check)
            v_hold_s50  +608.99 over  170 rounds, wins 62%   (+2.45 over +4 rounds since last check)
            v_hold_s25  +281.01 over  170 rounds, wins 62%   (+4.24 over +4 rounds since last check)
            v_x60222031  +254.90 over  388 rounds, wins 46%   (+8.95 over +4 rounds since last check)
            v_take100  +132.47 over  170 rounds, wins 65%   (+4.24 over +4 rounds since last check)
            v_x64216772  +117.42 over  423 rounds, wins 52%   (+8.95 over +4 rounds since last check)
            v_hold_after120   +88.25 over  170 rounds, wins 63%   (+29.43 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 56.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
