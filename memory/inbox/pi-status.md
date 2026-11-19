# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 day, 12 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 24 hours; whisper Up 24 hours (healthy); piper Up 24 hours (healthy); pihole Up 24 hours (healthy); homeassistant Up 24 hours

## Sync and schedule
- Pi repo copy at: 510f9b2 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 19 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    62 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1388 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 4 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1195.86 over  799 rounds, wins 12%   (-141.99 over +3 rounds since last check)
            v_hold_s250_wild +1087.43 over  263 rounds, wins 64%   (+5.17 over +3 rounds since last check)
            v_edge10_s100_dd  +787.48 over  799 rounds, wins 12%   (-44.56 over +3 rounds since last check)
            v_x60222031  +154.57 over 1250 rounds, wins 47%   (+0.68 over +3 rounds since last check)
            v_x64216772   +38.93 over 1285 rounds, wins 59%   (+6.53 over +3 rounds since last check)
            v_x60222032    +8.16 over 1250 rounds, wins 59%   (+6.53 over +3 rounds since last check)
            v_snipe_all    +2.70 over 1187 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1032 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_x12229262   -27.61 over 1229 rounds, wins 59%   (+10.10 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 302.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
