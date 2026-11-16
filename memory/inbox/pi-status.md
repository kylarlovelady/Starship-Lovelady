# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 12 hours, 45 minutes; temp 45.0'C; throttled flags 0x0 (0x0 is clean); memory 26%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 10 days (healthy); piper Up 10 days (healthy); pihole Up 6 days (healthy); homeassistant Up 10 days

## Sync and schedule
- Pi repo copy at: 017d5e2 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 16 Nov 15:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    73 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (1200 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 13 min ago
      OK    patterns.json updated 12 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s250_wild +2155.08 over   37 rounds, wins 70%   (+976.91 over +4 rounds since last check)
            v_edge10_s100  +625.70 over  573 rounds, wins 11%   (+192.72 over +4 rounds since last check)
            v_edge10_s100_dd  +427.00 over  573 rounds, wins 11%   (+47.56 over +4 rounds since last check)
            v_x64216772   +38.76 over 1059 rounds, wins 58%   (+2.98 over +4 rounds since last check)
            v_x12229262   +36.41 over 1003 rounds, wins 57%   (+81.32 over +4 rounds since last check)
            v_x60222032    +7.99 over 1024 rounds, wins 58%   (+2.98 over +4 rounds since last check)
            v_snipe_all    +2.70 over  961 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_hold_s5    +0.00 over  806 rounds, wins 0%   (+0.00 over +4 rounds since last check)
            v_x40223631   -31.70 over 1011 rounds, wins 58%   (+2.98 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 235.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
