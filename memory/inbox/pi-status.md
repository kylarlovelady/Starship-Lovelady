# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 8 hours, 42 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 hours; whisper Up 9 hours (healthy); piper Up 9 hours (healthy); pihole Up 9 hours (healthy); homeassistant Up 9 hours

## Sync and schedule
- Pi repo copy at: 76e5595 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Wed 18 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    67 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1348 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 9 min ago
      OK    patterns.json updated 6 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +1203.34 over  218 rounds, wins 63%   (-246.46 over +3 rounds since last check)
            v_edge10_s100 +1181.50 over  754 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  +884.34 over  754 rounds, wins 12%   (+0.00 over +3 rounds since last check)
            v_x60222031  +238.23 over 1205 rounds, wins 47%   (+3.44 over +3 rounds since last check)
            v_x64216772   +68.20 over 1240 rounds, wins 58%   (-2.08 over +3 rounds since last check)
            v_x60222032   +37.43 over 1205 rounds, wins 59%   (-2.08 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1142 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  987 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631    -2.26 over 1192 rounds, wins 58%   (-2.08 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 287.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
