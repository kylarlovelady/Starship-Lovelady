# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 days, 6 hours, 12 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 25%; disk 12%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 5 days (healthy); homeassistant Up 5 days

## Sync and schedule
- Pi repo copy at: 6b6c3ec 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 23 Nov 17:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 3 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    63 of the last 96 rounds were settled by Kalshi and logged
      OK    +2 new written lessons since the last check (1664 total)
      OK    entry_stats.json updated 8 min ago
      OK    exit_rules.json updated 20 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 17 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_snipe_all    +2.70 over 1517 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_hold_s5    +0.00 over 1362 rounds, wins 0%   (+0.00 over +3 rounds since last check)
            v_snipe    -147.46 over 1518 rounds, wins 26%   (+0.41 over +3 rounds since last check)
            v_x64216772  -152.88 over 1615 rounds, wins 57%   (-15.52 over +3 rounds since last check)
            v_x60222032  -183.65 over 1580 rounds, wins 57%   (-15.52 over +3 rounds since last check)
            v_x40223631  -223.34 over 1567 rounds, wins 57%   (-15.52 over +3 rounds since last check)
            hold       -229.98 over 1718 rounds, wins 58%   (+10.08 over +3 rounds since last check)
            v_hold_s10  -302.01 over 1362 rounds, wins 58%   (+5.63 over +3 rounds since last check)
            v_x60222031  -332.62 over 1580 rounds, wins 46%   (-34.88 over +3 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 404.9 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
