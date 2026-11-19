# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 2 hours, 12 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 26 hours; whisper Up 26 hours (healthy); piper Up 26 hours (healthy); pihole Up 26 hours (healthy); homeassistant Up 26 hours

## Sync and schedule
- Pi repo copy at: d4ee298 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 13:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    60 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1392 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 17 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1045.63 over  805 rounds, wins 12%   (-50.36 over +3 rounds since last check)
            v_edge10_s100_dd  +734.98 over  805 rounds, wins 12%   (-18.67 over +3 rounds since last check)
            v_hold_s250_wild  +596.11 over  269 rounds, wins 64%   (-246.38 over +3 rounds since last check)
            v_x60222031  +143.79 over 1256 rounds, wins 47%   (-6.63 over +3 rounds since last check)
            v_x64216772   +35.59 over 1291 rounds, wins 59%   (-2.12 over +3 rounds since last check)
            v_x60222032    +4.82 over 1256 rounds, wins 59%   (-2.12 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1193 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1038 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x40223631   -34.87 over 1243 rounds, wins 59%   (-2.12 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 304.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
