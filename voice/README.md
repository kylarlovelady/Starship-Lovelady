# Phone Voice (Kylar's plan, built in phases)

Goal (from the Nov 2-4 voice calls): wear AirPods at work, keep the phone on a charger with the page open, and have the assistant listen for its name all night, log every wake-word
candidate so Kylar can mark it good / false / missed, and tune the threshold from that. After the name it holds a real conversation, answers ONLY on the phone (never the home speakers,
never the Pi screen), keeps listening for follow-ups (10 s quiet, 20 s after a question; "that's all" ends it; soft tone on close).

## What iPhone allows (checked Nov 4)
The Home Assistant iPhone app has no wake word and no background listening (only a button, Action button, Siri shortcut, lock-screen widget, Back Tap). A web page cannot listen with the screen
locked. So Phase 1 is a web page (Add to Home Screen) kept open with the screen awake, on a charger. True pocket/locked listening needs a native iPhone app (needs a Mac + Apple developer account); not built.

## Phases
1. DONE (needs a real-phone test): wake-word listener + event log + Good / False / "I said it, it missed" + threshold tuning from the labels. voice/phone_voice.py + voice/phone.html.
2. DONE (needs keys on the Pi): conversation after the wake word, phone-only replies, follow-up timing, end phrases. Uses OpenAI (speech to text, chat) and ElevenLabs (Brian). Prompt in ~/voice-data/prompt.txt.
3. NOT BUILT: voice ID (voiceprints, "who am I speaking with?", trust levels, kids' voices changing). Hook: speaker_check() in phone_voice.py. Everything is "owner (unverified)" until then.
4. NOT BUILT: AirPods voice-isolation / direction, home-mic direction and echo cancellation. Home mic (MXL AC-44) has no array; try software first, buy a ReSpeaker XVF3800 only if needed.
5. NOT BUILT: home Pi speaker path routing ("one place only": the device that heard the voice answers). The phone path never touches the home speakers by construction.

## Setup on the Pi
    bash ~/starship/tasks/voice_setup.sh      # installs, asks for keys (hidden), starts the service, puts it on Tailscale HTTPS, prints the phone URL
    bash ~/starship/tasks/voice_probe.sh      # read-only inventory of the Pi's voice stack
Data: ~/voice-data (events.jsonl, labels.jsonl, conversations.jsonl, clips/, replies/, settings.json, keys.env chmod 600). Clips older than 21 days are deleted. Private mode keeps no clips.
