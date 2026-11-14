# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 1 hour, 45 minutes; temp 41.7'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 4 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 3ff3bc8 15 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 04:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    82 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1014 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1830.52 over  353 rounds, wins 14%   (+0.00 over +4 rounds since last check)
            v_edge10_s100_dd  +855.05 over  353 rounds, wins 14%   (+0.00 over +4 rounds since last check)
            v_x64216772  +135.71 over  839 rounds, wins 56%   (+5.10 over +4 rounds since last check)
            v_x60222032  +104.94 over  804 rounds, wins 57%   (+5.10 over +4 rounds since last check)
            v_x40223631   +65.25 over  791 rounds, wins 57%   (+5.10 over +4 rounds since last check)
            v_snipe_all    +2.70 over  741 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  586 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x12229262    -1.56 over  783 rounds, wins 56%   (-14.25 over +4 rounds since last check)
            v_hold_s10   -42.02 over  586 rounds, wins 60%   (+5.10 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 176.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
