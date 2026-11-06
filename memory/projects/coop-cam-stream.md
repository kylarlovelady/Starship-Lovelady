# Coop cam: live stream with donate-to-feed (idea, Kylar 2026-11-06, voice)

Idea: put a live-streaming camera on the chicken coop and the rabbit coop, stream to TikTok, YouTube or another live platform, and build a machine that feeds the animals and drops snacks according to what viewers gift or donate.

## How it could work
- Camera per coop (weatherproof, with night view) feeding OBS or a Pi/ffmpeg stream to YouTube or TikTok Live.
- A small controller (ESP32 or the Pi) drives a feeder or treat dropper (servo or auger).
- YouTube Super Chats and TikTok gifts both have developer hooks/events that tell our code when someone pays; code maps gift size to a small treat.

## Rules to build in
- Small, safe treats only; a daily cap and a cooldown so donors cannot empty the hopper or overfeed (rabbits get sick easily; check safe treats for each species).
- Always keep the normal feeding schedule separate from the gift treats.
- Platform rules: TikTok Live needs a minimum follower count; YouTube is easier to start. Check each platform's rules on payouts, animal streams and monetization before launching.
- Weatherproofing, predators and power at the coops; a local fallback if the internet drops.

## Next steps
1. Pick the platform to start with (YouTube is easier) and make a channel under the Lovelady LLC plan.
2. Test one camera on one coop, no feeder yet.
3. Prototype the treat dropper on the bench; then hook gift events to it.
Linked: business.md (parked ideas), the Lovelady family page idea (no separate note existed yet when this was written).
