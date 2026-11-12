# Morning brief, Thu 2026-11-12 (written 6:25 am Central)

## What happened since yesterday
- The Pi is healthy: every service running, cool (43 C), disk 11% full, nothing failed, up 6 days. Notes sync worked (last one 6:00 am).
- Kalshi practice agent: running, live trading OFF, practice money only. Best wallets are the "only bet on a big edge" ones: v_edge10_s100 +$1,873 and its throttled twin +$1,210 over 173 rounds, but they win only 16% of rounds, so still a lottery shape, not a proven edge. In the last 24 hours the "hold to the end" wallets did best (v_hold_s500 +$5,397, v_hold_s250 +$2,731, the cheap100 twin +$2,437). The "agree" test is weak (+$190, 68 rounds). These swing a lot, so none of it is proven.
- Home Jarvis: wake-up bar still 0.8. 3 wake-ups in 24 hours, all empty (2 to 3 am). No change needed.
- Phone Jarvis: no chats for about 129 hours (idle, not broken), no errors. No new Jarvis notes to file.
- Hub screen: the new background library server is running on the Pi (port 8110). No photos uploaded yet.
- Pi-hole is up; its stats stay blank until it gets its password.

## What is broken or needs a look
- Kalshi API key expired Nov 9 and is not renewed (3 days). Practice agent does not need it; the real-fills file does.
- The Wed Nov 11 pick-winners review of the Kalshi forward tests was not done yet (due yesterday); I will do it next with the Pi's round counts.
- Home mic clips still end too short, so Jarvis can wait too long for you to finish. Needs a test at home.
- Stalled over 3 days, both waiting on you: Kalshi key, and the KDP re-upload of the 4 new Process Operator covers and interior.

## What you need to do (phone friendly)
1. Tell me "start Kalshi key" when you have a few minutes; I will walk you through it one step at a time.
2. When you can: upload the 4 new Process Operator covers and interior to KDP.
(On the Pi when convenient: bash ~/starship/tasks/pihole_key.sh)

## Coming up
- Safety: the F-250 pitman arm needs torquing before you drive it.
- Nov 24: ElevenLabs decision (renews Nov 26).

## Next thing Claude works on
Kalshi forward-test review (round counts, pick winners, retire losers), then the new API key with you, then the kitchen Pi first boot with you at home.
