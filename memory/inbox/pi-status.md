# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 9 hours, 12 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 28%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 hours; whisper Up 9 hours (healthy); piper Up 9 hours (healthy); pihole Up 9 hours (healthy); homeassistant Up 9 hours

## Sync and schedule
- Pi repo copy at: 90ef155 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 2 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    67 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1350 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1261.38 over  757 rounds, wins 13%   (+79.88 over +3 rounds since last check)
            v_hold_s250_wild +1239.37 over  221 rounds, wins 62%   (+36.03 over +3 rounds since last check)
            v_edge10_s100_dd  +895.18 over  757 rounds, wins 13%   (+10.84 over +3 rounds since last check)
            v_x60222031  +232.43 over 1208 rounds, wins 47%   (-5.80 over +3 rounds since last check)
            v_x64216772   +60.10 over 1243 rounds, wins 58%   (-8.10 over +3 rounds since last check)
            v_x60222032   +29.33 over 1208 rounds, wins 59%   (-8.10 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1145 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  990 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631   -10.36 over 1195 rounds, wins 58%   (-8.10 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 287.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
