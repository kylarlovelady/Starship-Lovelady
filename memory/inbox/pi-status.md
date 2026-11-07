# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 19 hours, 45 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 20 hours; whisper Up 20 hours (healthy); piper Up 20 hours (healthy); pihole Up 20 hours (healthy); homeassistant Up 20 hours

## Sync and schedule
- Pi repo copy at: 462c1d6 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (52 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 22:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (406 total)
      OK    entry_stats.json updated 5 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 17 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +486.44 over  168 rounds, wins 41%   (+58.44 over +4 rounds since last check)
            v_x60222031  +367.50 over  168 rounds, wins 42%   (+54.58 over +4 rounds since last check)
            v_x88221261  +309.76 over  175 rounds, wins 22%   (+14.34 over +4 rounds since last check)
            v_x64216771  +267.99 over  203 rounds, wins 37%   (+20.86 over +4 rounds since last check)
            v_x64216772  +186.38 over  203 rounds, wins 46%   (+30.60 over +4 rounds since last check)
            v_x12229262  +165.72 over  147 rounds, wins 41%   (+66.98 over +4 rounds since last check)
            v_x52220781  +162.56 over  179 rounds, wins 23%   (+14.34 over +4 rounds since last check)
            v_x60222032  +155.61 over  168 rounds, wins 47%   (+30.60 over +4 rounds since last check)
            v_x40223631  +115.92 over  155 rounds, wins 43%   (+30.60 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 2.4 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
