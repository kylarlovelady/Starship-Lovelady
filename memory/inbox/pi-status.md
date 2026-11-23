# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 4 days, 10 hours, 42 minutes; temp 45.0'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 4 days; whisper Up 4 days (healthy); piper Up 4 days (healthy); pihole Up 4 days (healthy); homeassistant Up 4 days

## Sync and schedule
- Pi repo copy at: bc9728b 2 minutes ago: KDP: bubblegum pink covers
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (53 min ago), first lines:
    MARKET AGENT PROGRESS  Sun 22 Nov 21:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    69 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1611 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 21 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 17 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1456 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1301 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_edge10_s100_dd   -64.22 over 1068 rounds, wins 13%   (-0.44 over +3 rounds since last check)
            v_x64216772   -87.65 over 1554 rounds, wins 57%   (-5.78 over +3 rounds since last check)
            v_snipe    -117.21 over 1457 rounds, wins 27%   (+1.32 over +3 rounds since last check)
            v_x60222032  -118.42 over 1519 rounds, wins 57%   (-5.78 over +3 rounds since last check)
            v_x40223631  -158.11 over 1506 rounds, wins 57%   (-5.78 over +3 rounds since last check)
            v_edge10_s100  -216.80 over 1068 rounds, wins 13%   (-0.58 over +3 rounds since last check)
            hold       -252.99 over 1657 rounds, wins 58%   (+25.15 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 385.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
