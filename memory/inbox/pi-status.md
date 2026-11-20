# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 13 hours, 12 minutes; temp 47.7'C; throttled flags 0x0 (0x0 is clean); memory 28%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 37 hours; whisper Up 37 hours (healthy); piper Up 37 hours (healthy); pihole Up 37 hours (healthy); homeassistant Up 37 hours

## Sync and schedule
- Pi repo copy at: 80cd88a 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 00:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 58 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1421 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 8 min ago
      OK    learn_report.json updated 35 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1062.54 over  840 rounds, wins 12%   (-99.89 over +3 rounds since last check)
            v_edge10_s100_dd  +795.55 over  840 rounds, wins 12%   (-79.87 over +3 rounds since last check)
            v_x60222031  +230.27 over 1291 rounds, wins 47%   (+21.48 over +3 rounds since last check)
            v_x64216772   +15.51 over 1326 rounds, wins 59%   (+15.36 over +3 rounds since last check)
            v_hold_s250_wild   +10.96 over  304 rounds, wins 64%   (+1.11 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1228 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1073 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032   -15.26 over 1291 rounds, wins 59%   (+15.36 over +3 rounds since last check)
            v_x40223631   -54.95 over 1278 rounds, wins 59%   (+15.36 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 315.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
