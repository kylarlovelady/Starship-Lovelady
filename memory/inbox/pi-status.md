# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 4 days, 15 hours, 30 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 63%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 6 days; whisper Up 6 days (healthy); piper Up 6 days (healthy); pihole Up 31 hours (healthy); homeassistant Up 25 hours

## Sync and schedule
- Pi repo copy at: b836a17 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    88 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (327 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 2 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +529.26 over   88 rounds, wins 44%   (-33.12 over +4 rounds since last check)
            v_x60222031  +453.11 over   88 rounds, wins 48%   (-59.73 over +4 rounds since last check)
            v_x88221261  +301.15 over   95 rounds, wins 22%   (-4.09 over +4 rounds since last check)
            v_x80218932  +202.15 over  107 rounds, wins 47%   (-7.70 over +4 rounds since last check)
            v_x52220781  +188.94 over   99 rounds, wins 24%   (-29.84 over +4 rounds since last check)
            v_x24220781  +145.43 over   91 rounds, wins 47%   (-7.70 over +4 rounds since last check)
            v_x64216771  +143.40 over  123 rounds, wins 37%   (-48.17 over +4 rounds since last check)
            v_x64216772  +129.20 over  123 rounds, wins 47%   (-18.54 over +4 rounds since last check)
            v_hold     +116.18 over  199 rounds, wins 42%   (-24.47 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 12.6 h ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
