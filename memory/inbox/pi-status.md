# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 1 day, 12 hours, 42 minutes; temp 44.4'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 13%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 8 days; whisper Up 8 days (healthy); piper Up 8 days (healthy); pihole Up 8 days (healthy); homeassistant Up 8 days

## Sync and schedule
- Pi repo copy at: 010d4cd 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 26 Nov 23:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 50 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1847 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 16 min ago
      OK    learn_report.json updated 2 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1736 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_hold_s5    +0.00 over 1581 rounds, wins 0%   (+0.00 over +2 rounds since last check)
            v_snipe    -157.42 over 1737 rounds, wins 26%   (+1.12 over +2 rounds since last check)
            v_edge10_s100_dd  -197.39 over 1348 rounds, wins 13%   (+53.58 over +2 rounds since last check)
            v_hold_s10  -381.60 over 1581 rounds, wins 57%   (-10.96 over +2 rounds since last check)
            v_x64216772  -439.46 over 1834 rounds, wins 55%   (-20.21 over +2 rounds since last check)
            v_x60222032  -470.23 over 1799 rounds, wins 55%   (-20.21 over +2 rounds since last check)
            v_take25_s10  -492.64 over 1581 rounds, wins 67%   (-3.88 over +2 rounds since last check)
            v_x40223631  -509.92 over 1786 rounds, wins 55%   (-20.21 over +2 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 483.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
