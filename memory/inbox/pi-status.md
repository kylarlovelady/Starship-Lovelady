# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 5 hours, 15 minutes; temp 38.9'C; throttled flags 0x0 (0x0 is clean); memory 32%; disk 10%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 hours; whisper Up 5 hours (healthy); piper Up 5 hours (healthy); pihole Up 5 hours (healthy); homeassistant Up 5 hours

## Sync and schedule
- Pi repo copy at: 22da2f9 30 minutes ago: Jarvis notes and feedback summary sync
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Fri 06 Nov 08:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    95 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (351 total)
      OK    entry_stats.json updated 2 min ago
      OK    exit_rules.json updated 10 min ago
      OK    patterns.json updated 9 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x96220861  +448.92 over  112 rounds, wins 39%   (-14.84 over +4 rounds since last check)
            v_x60222031  +362.57 over  112 rounds, wins 42%   (+5.31 over +4 rounds since last check)
            v_x88221261  +259.43 over  119 rounds, wins 18%   (+0.00 over +4 rounds since last check)
            v_x80218932  +140.70 over  131 rounds, wins 44%   (-7.89 over +4 rounds since last check)
            v_x64216772  +138.92 over  147 rounds, wins 45%   (-0.24 over +4 rounds since last check)
            v_x64216771  +132.51 over  147 rounds, wins 36%   (-17.81 over +4 rounds since last check)
            v_x60222032  +108.15 over  112 rounds, wins 46%   (-0.24 over +4 rounds since last check)
            v_hold      +88.44 over  223 rounds, wins 41%   (-19.48 over +4 rounds since last check)
            v_x24220781   +83.98 over  115 rounds, wins 43%   (-7.89 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: 18.6 h ago
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
