# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 3 days, 7 hours, 45 minutes; temp 38.9'C; throttled flags 0x0 (0x0 is clean); memory 41%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 36 hours; whisper Up 3 days (healthy); piper Up 3 days (healthy); pihole Up 28 seconds (health: starting); homeassistant Up 3 days

## Sync and schedule
- Pi repo copy at: b13cb8d 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: push failed (run tasks/pi_push_setup.sh)
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog, jarvis-mic, jarvis-watch

## Markets agent (practice money)
- agent data last written: 1.9 h ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Mon 09 Nov 10:07
    
    1. ALIVE
      OK    service market-agent is active
      STUCK live file updated 63 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    88 of the last 96 rounds were settled by Kalshi and logged
      STUCK +0 new written lessons since the last check (638 total)
      OK    entry_stats.json updated 67 min ago
      OK    exit_rules.json updated 15 min ago
      OK    patterns.json updated 14 min ago
      OK    learn_report.json updated 81 min ago
    
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
- turns: 0; errors: 0; ignored blips: 0; last activity: 62.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is not confirmed, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
