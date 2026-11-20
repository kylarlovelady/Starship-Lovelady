# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 14 hours, 42 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 39 hours; whisper Up 39 hours (healthy); piper Up 39 hours (healthy); pihole Up 39 hours (healthy); homeassistant Up 39 hours

## Sync and schedule
- Pi repo copy at: cc01303 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 20 Nov 01:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 4 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 57 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1424 total)
      OK    entry_stats.json updated 10 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1016.22 over  844 rounds, wins 12%   (-46.32 over +4 rounds since last check)
            v_edge10_s100_dd  +744.64 over  844 rounds, wins 12%   (-50.91 over +4 rounds since last check)
            v_x60222031  +185.85 over 1295 rounds, wins 47%   (-44.42 over +4 rounds since last check)
            v_hold_s250_wild   +84.98 over  308 rounds, wins 64%   (+74.02 over +4 rounds since last check)
            v_snipe_all    +2.70 over 1232 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over 1077 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x64216772   -12.46 over 1330 rounds, wins 58%   (-27.97 over +4 rounds since last check)
            v_x60222032   -43.23 over 1295 rounds, wins 59%   (-27.97 over +4 rounds since last check)
            v_x40223631   -82.92 over 1282 rounds, wins 59%   (-27.97 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 317.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
