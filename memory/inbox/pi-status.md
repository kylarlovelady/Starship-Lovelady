# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 9 hours, 15 minutes; temp 41.1'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 9 hours; whisper Up 9 hours (healthy); piper Up 9 hours (healthy); pihole Up 9 hours (healthy); homeassistant Up 9 hours

## Sync and schedule
- Pi repo copy at: f274f38 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 12:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (367 total)
      OK    entry_stats.json updated 1 min ago
      OK    exit_rules.json updated 12 min ago
      OK    patterns.json updated 11 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +432.49 over  128 rounds, wins 40%   (+48.95 over +4 rounds since last check)
            v_x60222031  +366.00 over  128 rounds, wins 41%   (+62.72 over +4 rounds since last check)
            v_x64216771  +335.65 over  163 rounds, wins 37%   (+157.81 over +4 rounds since last check)
            v_x88221261  +263.31 over  135 rounds, wins 20%   (+10.25 over +4 rounds since last check)
            v_x64216772  +126.76 over  163 rounds, wins 45%   (+15.39 over +4 rounds since last check)
            v_x60222032   +95.99 over  128 rounds, wins 46%   (+15.39 over +4 rounds since last check)
            v_x28219981   +91.59 over  167 rounds, wins 35%   (+157.81 over +4 rounds since last check)
            v_x52220781   +79.88 over  139 rounds, wins 21%   (-16.55 over +4 rounds since last check)
            v_x80218932   +64.83 over  147 rounds, wins 41%   (+2.07 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 22.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
