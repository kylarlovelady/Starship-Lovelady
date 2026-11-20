# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 8 hours, 12 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 32 hours; whisper Up 32 hours (healthy); piper Up 32 hours (healthy); pihole Up 32 hours (healthy); homeassistant Up 32 hours

## Sync and schedule
- Pi repo copy at: b7d678d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 2 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 59 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1408 total)
      OK    entry_stats.json updated 7 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100  +716.12 over  824 rounds, wins 12%   (-157.27 over +3 rounds since last check)
            v_edge10_s100_dd  +528.76 over  824 rounds, wins 12%   (-59.38 over +3 rounds since last check)
            v_hold_s250_wild  +359.78 over  288 rounds, wins 64%   (+79.92 over +3 rounds since last check)
            v_x60222031  +150.59 over 1275 rounds, wins 47%   (-16.01 over +3 rounds since last check)
            v_x64216772   +29.56 over 1310 rounds, wins 59%   (+5.96 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1212 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1057 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x60222032    -1.21 over 1275 rounds, wins 59%   (+5.96 over +3 rounds since last check)
            v_x40223631   -40.90 over 1262 rounds, wins 59%   (+5.96 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 310.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
