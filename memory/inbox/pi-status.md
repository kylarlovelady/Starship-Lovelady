# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 18 hours, 12 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 7 days; whisper Up 7 days (healthy); piper Up 7 days (healthy); pihole Up 7 days (healthy); homeassistant Up 7 days

## Sync and schedule
- Pi repo copy at: 3d79b8d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 26 Nov 05:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 51 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (1805 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 5 min ago
      OK    patterns.json updated 3 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1684 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1529 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd  -113.53 over 1296 rounds, wins 13%   (-47.33 over +3 rounds since last check)
            v_snipe    -176.94 over 1685 rounds, wins 25%   (-10.42 over +3 rounds since last check)
            v_x64216772  -372.06 over 1782 rounds, wins 55%   (+8.21 over +3 rounds since last check)
            v_hold_s10  -382.27 over 1529 rounds, wins 57%   (+1.47 over +3 rounds since last check)
            v_edge10_s100  -401.72 over 1296 rounds, wins 13%   (-6.55 over +3 rounds since last check)
            v_x60222032  -402.83 over 1747 rounds, wins 56%   (+8.21 over +3 rounds since last check)
            v_x40223631  -442.52 over 1734 rounds, wins 55%   (+8.21 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 464.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
