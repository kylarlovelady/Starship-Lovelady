# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 16 hours, 15 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 36%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 16 hours; whisper Up 16 hours (healthy); piper Up 16 hours (healthy); pihole Up 16 hours (healthy); homeassistant Up 16 hours

## Sync and schedule
- Pi repo copy at: e4fa776 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue, series-catalog

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 19:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    94 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (394 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 16 min ago
      OK    patterns.json updated 15 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +372.61 over  156 rounds, wins 39%   (-0.14 over +4 rounds since last check)
            v_x60222031  +266.73 over  156 rounds, wins 40%   (-21.23 over +4 rounds since last check)
            v_x88221261  +249.71 over  163 rounds, wins 21%   (-9.09 over +4 rounds since last check)
            v_x64216771  +226.79 over  191 rounds, wins 37%   (-43.79 over +4 rounds since last check)
            v_x64216772  +143.01 over  191 rounds, wins 45%   (+19.59 over +4 rounds since last check)
            v_x60222032  +112.24 over  156 rounds, wins 46%   (+19.59 over +4 rounds since last check)
            v_x40223632   +95.55 over  143 rounds, wins 45%   (+2.28 over +4 rounds since last check)
            v_x40223631   +72.55 over  143 rounds, wins 42%   (+19.59 over +4 rounds since last check)
            v_x52220781   +63.03 over  167 rounds, wins 22%   (+31.36 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 29.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
