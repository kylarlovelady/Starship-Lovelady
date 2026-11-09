# Morning brief, Mon 2026-11-09 (written 6:25 am Central)

## What happened since yesterday
- The Pi is healthy: every service running, cool (40 C), disk 10% full, nothing failed, up 3 days. Notes sync is working (last one 6:00 am).
- Home Jarvis: wake-up bar is still 0.8. Last 24 hours had 6 wake-ups: 4 empty (all 2 to 3 am), 2 real commands. Better than the 11 the day before. No change needed.
- Phone Jarvis: no chats for about 57 hours, no errors. First words still about 1.6 seconds.
- Kalshi practice agent: running, live trading OFF. The $500 "hold to the end" version is up about $6,400 over 170 rounds, but nearly all of that came from cheap-side bets that win about 1 in 3. Promising, not proven. Today's tests: selling early for profit lost about 10% in every setting, and the long-shot and maker tests were inconclusive.
- KDP: you said all four Process Operator colours are live. Nice. It is no longer waiting.
- Pi-hole is up; its stats stay blank until it gets its password.

## What is broken or needs a look
- Kalshi data files (snapshots, sim windows) last wrote around 4 am. The agent itself is alive, so likely just their schedule. I will check again tomorrow.
- Home mic clips still end too short, so Jarvis can wait too long for you to finish. Needs a test at home.

## What you need to do (phone friendly)
1. TODAY: redo the Kalshi API location check on kalshi.com (Profile, API keys) and make a new key. It expires today. Tell me when you start and I will walk you through it one step at a time.
2. Send the Note 20 Ultra model number and your SIM choice for the cell Wi-Fi unit.
(On the Pi when convenient: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- Tomorrow (Nov 10): dry fit of the kitchen screen case (plate 1 is being reprinted with supports).
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
Read the Kalshi agent code and report each signal, its weight, and whether bet size follows agreement. Then the new API key with you, then the Starship room-by-room bug pass.
