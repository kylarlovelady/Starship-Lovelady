# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 8 hours, 15 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 21%; disk 11%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 4 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 8602533 28 minutes ago: Note: queue stuck by media server lock; README warning
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Sat 14 Nov 11:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    87 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1039 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 7 min ago
      OK    patterns.json updated 5 min ago
      OK    learn_report.json updated 5 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_edge10_s100 +2019.56 over  381 rounds, wins 14%   (-199.77 over +4 rounds since last check)
            v_edge10_s100_dd  +896.40 over  381 rounds, wins 14%   (-96.64 over +4 rounds since last check)
            v_x64216772   +96.87 over  867 rounds, wins 56%   (+4.35 over +4 rounds since last check)
            v_x60222032   +66.10 over  832 rounds, wins 57%   (+4.35 over +4 rounds since last check)
            v_x40223631   +26.41 over  819 rounds, wins 56%   (+4.35 over +4 rounds since last check)
            v_snipe_all    +2.70 over  769 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  614 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x60222031    -2.55 over  832 rounds, wins 45%   (-64.31 over +4 rounds since last check)
            v_x12229262   -65.04 over  811 rounds, wins 56%   (+20.18 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 182.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
