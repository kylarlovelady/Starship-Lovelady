# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 21 hours, 45 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 4 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 84e5643 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 00:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    82 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (999 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 21 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +2072.52 over  337 rounds, wins 15%   (+13.83 over +4 rounds since last check)
            v_edge10_s100_dd +1001.15 over  337 rounds, wins 15%   (+6.91 over +4 rounds since last check)
            v_x64216772  +109.33 over  823 rounds, wins 56%   (-3.15 over +4 rounds since last check)
            v_x60222032   +78.56 over  788 rounds, wins 57%   (-3.15 over +4 rounds since last check)
            v_x40223631   +38.87 over  775 rounds, wins 56%   (-3.15 over +4 rounds since last check)
            v_x12229262   +25.60 over  767 rounds, wins 56%   (+48.39 over +4 rounds since last check)
            v_snipe_all    +2.70 over  725 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x60222031    +1.75 over  788 rounds, wins 46%   (+2.48 over +4 rounds since last check)
            v_hold_s5    +0.00 over  570 rounds, wins 0%   (+0.00 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 172.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
