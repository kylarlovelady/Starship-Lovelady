# Pi status (auto, no secrets)
Freshness = the git commit time of this file. Ages below are counted at the moment of the snapshot.

## Pi
- up 1 week, 3 days, 19 hours, 30 minutes; temp 39.5'C; throttled flags 0x0 (0x0 is clean); memory 59%; disk 9%

## Services
- active: market-agent, phone-voice, tailscaled, docker, hub-dashboard, hub-devices, hub-kdp, hub-lights, hub-memlog, hub-oled, hub-outage, hub-satellite, hub-voice, hub-watchdog
- NOT active: none
- failed units: none
- containers: openwakeword Up 5 days; whisper Up 5 days (healthy); piper Up 5 days (healthy); pihole Up 11 hours (healthy); homeassistant Up 5 hours

## Sync and schedule
- Pi repo copy at: 238aeb0 9 minutes ago: Daily check 2026-11-05: brief, projects, changelog
- last notes sync result: notes pushed to the repo
- cron jobs (script names): crew-update.sh, market-watchdog, market-supervisor, market-lab, memory_sync.sh, starship-alerts, kalshi-data-sync, task-queue

## Markets agent (practice money)
- agent data last written: 0 min ago; mode shown by the agent: ?; live-run flags: {"live_run_active": false, "last_run_live": false}
- supervisor report (23 min ago), first lines:
    MARKET AGENT PROGRESS  Thu 05 Nov 06:07
    
    1. ALIVE
      OK    service market-agent is active
      OK    live file updated 0 min ago
      OK    per-second recording last wrote 0 min ago
    
    2. LEARNING (rounds turned into lessons)
      OK    78 of the last 96 rounds were settled by Kalshi and logged
      OK    +4 new written lessons since the last check (247 total)
      OK    entry_stats.json updated 4 min ago
      OK    exit_rules.json updated 8 min ago
      OK    patterns.json updated 7 min ago
      OK    learn_report.json updated 6 min ago
    
    3. PRACTICE SCOREBOARD (fake money, after fees)
            v_x44219232  +217.36 over   31 rounds, wins 45%   (+68.16 over +4 rounds since last check)
            v_x8220761  +173.21 over   32 rounds, wins 44%   (+3.82 over +4 rounds since last check)
            v_x219212  +157.08 over   39 rounds, wins 41%   (+68.16 over +4 rounds since last check)
            v_x88221261  +116.60 over   15 rounds, wins 47%   (+124.89 over +4 rounds since last check)
            v_x44219231  +104.25 over   31 rounds, wins 39%   (+16.76 over +4 rounds since last check)
            v_x80218932   +90.03 over   27 rounds, wins 56%   (-23.62 over +4 rounds since last check)
            v_x72222452   +86.09 over   32 rounds, wins 38%   (+16.76 over +4 rounds since last check)
            v_x64216772   +62.51 over   43 rounds, wins 51%   (+17.38 over +4 rounds since last check)
            v_x88221262   +58.31 over   15 rounds, wins 53%   (+16.76 over +4 rounds since last check)

## Jarvis (phone voice), last 24 h
- turns: 71; errors: 0; ignored blips: 10; last activity: 34 min ago
- hang-ups: you ended it x9, quiet x2
- time to first words: avg 1.6s, slowest 4.2s over 69 answers

## Pi-hole
- Pi-hole container is up and healthy, but I need its password to read stats (run tasks/pihole_key.sh once).

## Notes
- Jarvis note files: 0 (synced to memory/inbox)
