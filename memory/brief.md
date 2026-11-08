# Morning brief, Sun 2026-11-08 (written 6:20 am Central)

## What happened since yesterday
- The Pi is healthy: every service is running, cool (40.6 C), disk 10% full, nothing failed, up over 2 days. Notes sync is working (last one 6:00 am).
- Home Jarvis: the wake-up tuner raised the sensitivity bar from 0.7 to 0.8 at 11 pm Saturday (it worked and restarted cleanly). In the last 24 hours there were 11 wake-ups: 8 were empty (nobody talking, mostly 2 to 3 am), 1 was probably you two talking, and 2 were real commands. Last 7 days: 19 of 27 were false. I cannot tell yet if the 2 to 3 am ones came before or after the change; the 8 am check will look again.
- Phone Jarvis: quiet, no chats in the last 33 hours, no errors. First words still come in about 1.6 seconds. No family voices enrolled yet.
- Kalshi practice agent: running, live trading OFF, recording. Over the last day the "hold to the end" bets did best (for example the $500 version up about $1,100, the $100 version up about $410) while selling early at +25% was flat to negative. That is one good day on pretend money, not a proven edge. The $1K-Snipe test is stopped at $1,219.
- Pi-hole is up and healthy; its stats are still blank until it gets its password.

## What is broken or needs a look
- Home Jarvis slowness: the home mic clips are noisy with short quiet at the end (20 of 28 clips had under 0.8 s of quiet), so Jarvis often keeps waiting for you to finish. Needs a test at home from you, or the better mic idea.
- Starship page: the room-by-room bug pass is still not started. Mouse drag/zoom on desktop and the Hub layout editor drag bug are still open.
- Stalled soon: KDP has waited on your review report since Friday night (Nov 5, 11:28 pm). It becomes "stalled" tomorrow. The living room build waits on your cubby measurements.

## What you need to do (phone friendly)
1. Tell me how the KDP review on the navy and green books turned out.
2. Send the Note 20 Ultra model number and your SIM choice for the cell Wi-Fi unit.
(On the Pi when convenient: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- TOMORROW (Mon Nov 9): redo the Kalshi API location check and make a new API key.
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
The Starship room-by-room bug pass, then the home mic test and Hub tab clean-up.
