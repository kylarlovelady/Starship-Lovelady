# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 10 hours, 59 minutes; temp 43.9'C; throttled flags 0x0 (0x0 is clean); memory 32%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 11 hours; whisper Up 11 hours (healthy); piper Up 11 hours (healthy); pihole Up 11 hours (healthy); homeassistant Up 11 hours

## Sync and schedule
- Pi repo copy at: ac73b63 5 minutes ago: Maker study v2, wallet back to Auto (queues 079, 080), idea list
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (6 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 14:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (374 total)
      OK    entry_stats.json updated 3 min ago
      OK    exit_rules.json updated 0 min ago
      OK    patterns.json updated 22 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +396.22 over  136 rounds, wins 40%   (-19.41 over +4 rounds since last check)
            v_x60222031  +299.18 over  136 rounds, wins 40%   (-60.91 over +4 rounds since last check)
            v_x88221261  +249.42 over  143 rounds, wins 21%   (-7.65 over +4 rounds since last check)
            v_x64216771  +248.12 over  171 rounds, wins 36%   (-75.26 over +4 rounds since last check)
            v_x64216772  +128.67 over  171 rounds, wins 44%   (-21.82 over +4 rounds since last check)
            v_x80218932  +116.96 over  155 rounds, wins 43%   (+19.06 over +4 rounds since last check)
            v_x60222032   +97.90 over  136 rounds, wins 46%   (-21.82 over +4 rounds since last check)
            v_x24220781   +60.24 over  139 rounds, wins 43%   (+19.06 over +4 rounds since last check)
            v_x40223631   +58.21 over  123 rounds, wins 41%   (-21.82 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 24.3 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
