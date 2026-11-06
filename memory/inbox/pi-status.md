# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 13 hours, 45 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 14 hours; whisper Up 14 hours (healthy); piper Up 14 hours (healthy); pihole Up 14 hours (healthy); homeassistant Up 14 hours

## Sync and schedule
- Pi repo copy at: aed154f 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 16:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (382 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +367.45 over  144 rounds, wins 40%   (-14.26 over +4 rounds since last check)
            v_x60222031  +328.14 over  144 rounds, wins 42%   (+26.15 over +4 rounds since last check)
            v_x64216771  +240.72 over  179 rounds, wins 37%   (+1.58 over +4 rounds since last check)
            v_x88221261  +207.56 over  151 rounds, wins 21%   (-24.43 over +4 rounds since last check)
            v_x64216772  +120.69 over  179 rounds, wins 45%   (-0.47 over +4 rounds since last check)
            v_x40223632  +102.08 over  131 rounds, wins 46%   (+21.50 over +4 rounds since last check)
            v_x60222032   +89.92 over  144 rounds, wins 46%   (-0.47 over +4 rounds since last check)
            v_x96220872   +89.70 over  144 rounds, wins 33%   (+60.87 over +4 rounds since last check)
            v_x80218932   +79.66 over  163 rounds, wins 42%   (-14.21 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 27.1 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
