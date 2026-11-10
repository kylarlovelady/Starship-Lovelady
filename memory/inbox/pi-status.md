# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 16 hours, 49 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 41%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 45 hours; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 40 minutes (healthy); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: 5870f2a 2 minutes ago: Queue 105: Kalshi wallet curve evening rerun
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (57 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 09 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 10.1 h ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      STUCK 52 of the last 96 rounds were settled by Kalshi and logged
      STUCK +0 new written lessons since the last check (638 total)
      STUCK entry_stats.json updated 10.1 h ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 11 min ago
      OK    learn_report.json updated 10.4 h ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_hold_s500 +5383.23 over  185 rounds, wins 63%   (+0.00 over +0 rounds since last check)
            v_hold_s250 +2631.12 over  185 rounds, wins 63%   (+0.00 over +0 rounds since last check)
            v_hold_s100 +1048.32 over  185 rounds, wins 63%   (+0.00 over +0 rounds since last check)
            v_hold_s50  +532.83 over  185 rounds, wins 63%   (+0.00 over +0 rounds since last check)
            v_hold_s25  +257.38 over  185 rounds, wins 63%   (+0.00 over +0 rounds since last check)
            v_x60222031  +251.68 over  403 rounds, wins 46%   (+0.00 over +0 rounds since last check)
            v_x64216772  +156.61 over  438 rounds, wins 53%   (+0.00 over +0 rounds since last check)
            v_x96220861  +133.58 over  403 rounds, wins 45%   (+0.00 over +0 rounds since last check)
            v_x60222032  +125.84 over  403 rounds, wins 54%   (+0.00 over +0 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 71.5 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
