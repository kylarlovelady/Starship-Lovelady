# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 15 hours, 15 minutes; temp 47.7'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 15 hours; whisper Up 15 hours (healthy); piper Up 15 hours (healthy); pihole Up 15 hours (healthy); homeassistant Up 15 hours

## Sync and schedule
- Pi repo copy at: d617864 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 18:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (390 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +372.75 over  152 rounds, wins 39%   (-4.93 over +4 rounds since last check)
            v_x60222031  +287.96 over  152 rounds, wins 41%   (-30.72 over +4 rounds since last check)
            v_x64216771  +270.58 over  187 rounds, wins 37%   (-23.52 over +4 rounds since last check)
            v_x88221261  +258.80 over  159 rounds, wins 21%   (+28.92 over +4 rounds since last check)
            v_x64216772  +123.42 over  187 rounds, wins 44%   (-10.15 over +4 rounds since last check)
            v_x40223632   +93.27 over  139 rounds, wins 45%   (-15.91 over +4 rounds since last check)
            v_x60222032   +92.65 over  152 rounds, wins 45%   (-10.15 over +4 rounds since last check)
            v_x80218932   +60.85 over  171 rounds, wins 42%   (-10.02 over +4 rounds since last check)
            v_x40223631   +52.96 over  139 rounds, wins 41%   (-10.15 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 28.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
