# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 15 minutes; temp 43.3'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 4 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 7d29de4 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 03:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    82 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1010 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 22 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1830.52 over  349 rounds, wins 14%   (-99.96 over +4 rounds since last check)
            v_edge10_s100_dd  +855.05 over  349 rounds, wins 14%   (-34.05 over +4 rounds since last check)
            v_x64216772  +130.61 over  835 rounds, wins 56%   (+7.28 over +4 rounds since last check)
            v_x60222032   +99.84 over  800 rounds, wins 57%   (+7.28 over +4 rounds since last check)
            v_x40223631   +60.15 over  787 rounds, wins 56%   (+7.28 over +4 rounds since last check)
            v_x12229262   +12.69 over  779 rounds, wins 56%   (-12.33 over +4 rounds since last check)
            v_snipe_all    +2.70 over  737 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  582 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -47.12 over  582 rounds, wins 60%   (+7.28 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 174.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
