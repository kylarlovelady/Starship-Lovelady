# How everything connects (and what is missing)
Written 2026-11-05. Update when something changes.

## The pieces
- **Pi** (LoveladyMainAiHub): runs everything below. **Repo** (this one): the shared brain (memory/) and the code the Pi pulls every ~3 min.
- **Jarvis server** (voice/phone_voice.py): the one voice brain. Doors into it: voice page (phone), Siri Shortcut, home speaker (via ha/custom_components/jarvis_hub, being installed).
- **Home Assistant**: devices, lights, wake word and speaker satellite, phone alerts.
- **Starship page** (index.html): control room dashboard. Reads status.json (Pi health) and hub-extra.json (voice, markets, sync).
- **LoveladyAiHub site / HomeAiAssistant page**: the hub web pages served from the Pi (dashboard, devices, KDP, memory, janitor panes).
- **Kalshi agent** (markets/): collects data, tests strategies on practice money; Live View page on port 8095.
- **Pi-hole**: DNS blocking and device visibility (see below).
- **Claude**: works through the repo; sees the Pi through memory/inbox/pi-status.md and kalshi-data-status.md; Kylar pastes command output when more is needed.

## Wiring that exists
Memory: Claude <-> repo <-> Jarvis. Status: Pi scripts -> status.json / hub-extra.json -> Starship page; Pi -> pi-status.md -> repo -> Claude. Data: Kalshi/Bitcoin history -> ~/market-data -> agents.

## Gaps and the fix for each (build order)
1. **Jarvis has no tools yet.** He can talk and remember but cannot look up live things. Give him safe tools: Pi status, markets summary, Pi-hole stats, Home Assistant switches/lights, "what changed today". Then "how is the market agent doing?" or "turn off the garage light" works by voice on phone and at home.
2. **One alert channel.** Anything that breaks (service down, market-agent stale, Jarvis errors, Pi-hole down, Pi hot, disk full, Kalshi API verification about to expire) sends one phone alert through Home Assistant, and shows on the Starship Security light.
3. **One front door.** One page with tabs: Starship, Jarvis (voice page), Jarvis Lab, Markets Live View, Pi-hole, Home Assistant, Memory/Projects. Voice page stays a separate always-on URL.
4. **Pi-hole into the status bus.** Blocked count, top clients, unknown devices, DNS answering: into hub-extra.json, the Starship Security light, Jarvis tools and the device list.
5. **Claude can act on the Pi without copy-paste.** A "task queue": Claude pushes a script into tasks/queue/, the Pi (already pulling the repo) runs only whitelisted queue scripts, and writes the output to memory/inbox/queue-results.md. Trade-off: anyone who can push to the repo can run code on the Pi (it already runs repo code); keep GitHub login protected with 2-step.
6. **Daily Claude check.** A scheduled Claude task reads pi-status.md, inbox notes and data status, files notes into the right files, updates projects.md, flags problems, writes a morning brief.
7. **Kalshi into the loop.** Agent status and findings land in memory/kalshi-ai.md automatically (daily summary), Jarvis can report them, alerts for stale data.

## Pi-hole (to-do project, see projects.md)
Status: pilot not started (unconfirmed what is installed). Plan: confirm it answers; set it as DNS on the router or per-device (iPad first, then phones, then TVs); turn off Private Wi-Fi Address, Private Relay, VPN, Private DNS on devices; name the 11 unnamed devices; then feed its stats into the status bus (gap 4).
