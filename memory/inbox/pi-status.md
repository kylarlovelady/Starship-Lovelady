# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 2 hours, 45 minutes; temp 42.8'C; throttled flags 0x0 (0x0 is clean); memory 24%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 10 days (healthy); piper Up 10 days (healthy); pihole Up 6 days (healthy); homeassistant Up 10 days

## Sync and schedule
- Pi repo copy at: 46b4fa9 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 16 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    75 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1170 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 34 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +816.97 over  537 rounds, wins 12%   (-42.26 over +3 rounds since last check)
            v_edge10_s100_dd  +481.33 over  537 rounds, wins 12%   (-10.47 over +3 rounds since last check)
            v_x64216772   +28.32 over 1023 rounds, wins 57%   (-4.53 over +3 rounds since last check)
            v_snipe_all    +2.70 over  925 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over  770 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032    -2.45 over  988 rounds, wins 58%   (-4.53 over +3 rounds since last check)
            v_x40223631   -42.14 over  975 rounds, wins 57%   (-4.53 over +3 rounds since last check)
            v_x60222031   -48.59 over  988 rounds, wins 45%   (-68.84 over +3 rounds since last check)
            v_snipe    -112.96 over  926 rounds, wins 28%   (+0.73 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 225.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
