# Morning brief, Wed 2026-11-11 (written 6:25 am Central)

## What happened since yesterday
- The Pi is healthy: every service running, cool (40 C), disk 10% full, nothing failed, up 5 days. Notes sync is working (last one 6:00 am).
- Kalshi practice agent: running, live trading OFF, practice money only. The two new "only bet on a big edge" tests (v_edge10_s100 and its throttled twin) are the best wallets: about +$782 and +$524 over 87 rounds, but they win only 13% of rounds, so it is still a lottery shape, not a proven edge. They also lost about $52 and $81 in the last 4 rounds. The $250/$500 "hold" wallets did not show in the snapshot I could read.
- Home Jarvis: wake-up bar still 0.8. 3 wake-ups in 24 hours, all empty (2 to 3 am). No change needed.
- Phone Jarvis: no chats for about 105 hours, no errors. No new voice notes from Jarvis to file.
- Pi-hole is up; its stats stay blank until it gets its password.
- Kitchen screen Pi plan is filed (you are writing the SD card).

## What is broken or needs a look
- Kalshi API key expired Nov 9 and is not renewed (2 days). Practice agent does not need it; the real-fills file does.
- Kalshi data files last wrote about 4 am; the agent itself says it is alive, so probably just their schedule.
- Home mic clips still end too short, so Jarvis can wait too long for you to finish. Needs a test at home.
- Nothing stalled over 3 days except the key and the KDP re-upload, both waiting on you.

## What you need to do (phone friendly)
1. Tell me "start Kalshi key" when you have a few minutes; I will walk you through it one step at a time.
2. When you can: upload the 4 new Process Operator covers and interior to KDP.
3. Tell me when the kitchen Pi SD card is written.
(On the Pi when convenient: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- Today: pick winners and retire losers among the Kalshi forward tests once they have about 100 rounds (the round counts for the cheap100, agree and throttle wallets were not in today's files; I will ask the Pi for them).
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
Kalshi forward-test review (counts and winners), then the new API key with you, then the kitchen Pi first boot with you at home.
