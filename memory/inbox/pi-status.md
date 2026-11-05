# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 15 hours, 58 minutes; temp 40.0'C; throttled flags 0x0 (0x0 is clean); memory 58%; disk 9%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 7 hours (healthy); homeassistant Up About an hour

## Sync and schedule
- Pi repo copy at: 735dcfa 2 minutes ago: Safe shows real wallet money
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (50 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 02:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    86 of the last 96 rounds were settled by Kalshi and logged
      OK    +3 new written lessons since the last check (238 total)
      OK    entry_stats.json updated 0 min ago
      OK    exit_rules.json updated 19 min ago
      OK    patterns.json updated 18 min ago
      OK    learn_report.json updated 21 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x8220761  +232.93 over   24 rounds, wins 46%   (+84.72 over +4 rounds since last check)
            v_x44219232  +219.31 over   23 rounds, wins 43%   (+75.77 over +4 rounds since last check)
            v_x219212  +162.73 over   31 rounds, wins 39%   (+75.77 over +4 rounds since last check)
            v_x44219231  +153.51 over   23 rounds, wins 39%   (+75.77 over +4 rounds since last check)
            v_x72222452  +135.35 over   24 rounds, wins 38%   (+75.77 over +4 rounds since last check)
            v_x88221262  +107.57 over    7 rounds, wins 71%   (+75.77 over +4 rounds since last check)
            v_x80218932  +104.59 over   19 rounds, wins 53%   (+72.29 over +4 rounds since last check)
            v_x16217722   +83.07 over   15 rounds, wins 53%   (+122.62 over +4 rounds since last check)
            v_x28219981   +74.88 over   39 rounds, wins 36%   (+75.77 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 0; errors: 0; ignored blips: 0; last activity: no file
- hang-ups: none
- time to first words: no answers logged yet

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
