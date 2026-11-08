# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 2 days, 9 hours, 58 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 38%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 14 hours; whisper Up 2 days (healthy); piper Up 2 days (healthy); pihole Up 2 days (healthy); homeassistant Up 2 days

## Sync and schedule
- Pi repo copy at: 0e6cc85 4 minutes ago: Kitchen screen case v6: generator, print-ready STLs, 3D viewer, blueprint, CAD kit, Pi queue jobs
- last notes sync result: remove the file manually to continue.
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (6 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 08 Nov 13:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (561 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 1 min ago
      OK    patterns.json updated 0 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +1926.69 over  106 rounds, wins 63%   (+328.37 over +4 rounds since last check)
            v_hold_s250 +1060.10 over  106 rounds, wins 63%   (+160.01 over +4 rounds since last check)
            v_hold_s100  +424.11 over  106 rounds, wins 63%   (+59.10 over +4 rounds since last check)
            v_x96220861  +279.06 over  324 rounds, wins 43%   (-3.11 over +4 rounds since last check)
            v_x60222031  +268.21 over  324 rounds, wins 45%   (-24.40 over +4 rounds since last check)
            v_hold_s50  +221.59 over  106 rounds, wins 63%   (+25.62 over +4 rounds since last check)
            v_hold_s25  +100.67 over  106 rounds, wins 63%   (+8.77 over +4 rounds since last check)
            v_x64216772   +95.14 over  359 rounds, wins 50%   (-4.06 over +4 rounds since last check)
            v_take100   +68.71 over  106 rounds, wins 64%   (+8.77 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 40.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
