# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 1 hour, 45 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 26 hours; whisper Up 26 hours (healthy); piper Up 26 hours (healthy); pihole Up 26 hours (healthy); homeassistant Up 26 hours

## Sync and schedule
- Pi repo copy at: a0b72f3 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 07 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (430 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 6 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x88221261  +229.97 over  199 rounds, wins 22%   (-53.02 over +4 rounds since last check)
            v_x96220861  +219.84 over  192 rounds, wins 39%   (-26.59 over +4 rounds since last check)
            v_x64216772  +162.51 over  227 rounds, wins 45%   (-2.92 over +4 rounds since last check)
            v_x60222032  +131.74 over  192 rounds, wins 46%   (-2.92 over +4 rounds since last check)
            v_x60222031  +128.69 over  192 rounds, wins 40%   (+8.83 over +4 rounds since last check)
            v_x40223631   +92.05 over  179 rounds, wins 43%   (-2.92 over +4 rounds since last check)
            v_x12229262   +69.08 over  171 rounds, wins 41%   (-23.58 over +4 rounds since last check)
            v_x96220872   +46.77 over  192 rounds, wins 32%   (+22.96 over +4 rounds since last check)
            v_x40223632   +45.27 over  179 rounds, wins 45%   (-36.79 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 8.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
