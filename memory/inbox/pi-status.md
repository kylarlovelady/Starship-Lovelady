# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 17 hours, 15 minutes; temp 40.6'C; throttled flags 0x0 (0x0 is clean); memory 37%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 17 hours; whisper Up 17 hours (healthy); piper Up 17 hours (healthy); pihole Up 17 hours (healthy); homeassistant Up 17 hours

## Sync and schedule
- Pi repo copy at: 1b432a7 7 minutes ago: Names confirmed in Pi-hole table
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (22 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 20:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (398 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 11 min ago
      OK    patterns.json updated 10 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +384.53 over  160 rounds, wins 39%   (+11.92 over +4 rounds since last check)
            v_x88221261  +283.65 over  167 rounds, wins 22%   (+33.94 over +4 rounds since last check)
            v_x60222031  +258.96 over  160 rounds, wins 40%   (-7.77 over +4 rounds since last check)
            v_x64216771  +224.26 over  195 rounds, wins 36%   (-2.53 over +4 rounds since last check)
            v_x64216772  +132.79 over  195 rounds, wins 45%   (-10.22 over +4 rounds since last check)
            v_x60222032  +102.02 over  160 rounds, wins 46%   (-10.22 over +4 rounds since last check)
            v_x52220781   +99.12 over  171 rounds, wins 23%   (+36.09 over +4 rounds since last check)
            v_x40223632   +85.38 over  147 rounds, wins 45%   (-10.17 over +4 rounds since last check)
            v_x36215122   +80.07 over  187 rounds, wins 20%   (+34.90 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 30.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
