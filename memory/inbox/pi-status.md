# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 17 hours, 45 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 27%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 4 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 4b26114 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 13 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    83 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (985 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 14 min ago
      OK    patterns.json updated 12 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +1759.90 over  322 rounds, wins 15%   (+29.89 over +4 rounds since last check)
            v_edge10_s100_dd  +887.50 over  322 rounds, wins 15%   (+35.11 over +4 rounds since last check)
            v_x64216772  +103.94 over  808 rounds, wins 56%   (+1.93 over +4 rounds since last check)
            v_x60222032   +73.17 over  773 rounds, wins 57%   (+1.93 over +4 rounds since last check)
            v_x40223631   +33.48 over  760 rounds, wins 56%   (+1.93 over +4 rounds since last check)
            v_snipe_all    +2.70 over  710 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  555 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s10   -64.50 over  555 rounds, wins 60%   (+1.80 over +4 rounds since last check)
            v_x60222031   -71.36 over  773 rounds, wins 46%   (+111.67 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 168.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
