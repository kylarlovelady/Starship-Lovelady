# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 18 hours, 15 minutes; temp 42.2'C; throttled flags 0x0 (0x0 is clean); memory 35%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 18 hours; whisper Up 18 hours (healthy); piper Up 18 hours (healthy); pihole Up 18 hours (healthy); homeassistant Up 18 hours

## Sync and schedule
- Pi repo copy at: 45ab89e 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 21:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (402 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 3 min ago
      OK    patterns.json updated 1 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +428.00 over  164 rounds, wins 40%   (+43.47 over +4 rounds since last check)
            v_x60222031  +312.92 over  164 rounds, wins 40%   (+53.96 over +4 rounds since last check)
            v_x88221261  +295.42 over  171 rounds, wins 22%   (+11.77 over +4 rounds since last check)
            v_x64216771  +247.13 over  199 rounds, wins 36%   (+22.87 over +4 rounds since last check)
            v_x64216772  +155.78 over  199 rounds, wins 45%   (+22.99 over +4 rounds since last check)
            v_x52220781  +148.22 over  175 rounds, wins 23%   (+49.10 over +4 rounds since last check)
            v_x60222032  +125.01 over  164 rounds, wins 46%   (+22.99 over +4 rounds since last check)
            v_x36215122  +102.87 over  191 rounds, wins 20%   (+22.80 over +4 rounds since last check)
            v_x12229262   +98.74 over  143 rounds, wins 39%   (+67.60 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 52 min ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
