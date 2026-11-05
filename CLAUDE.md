# Starship Lovelady: instructions for every Claude conversation on this repo

Owner: Kylar Lovelady (spelled KYLAR, said "Kyler"). His wife is spelled SHAREE and said "sheree" (never Sheree, Shari or Sherry; Kylar corrected this 2026-11-05), Central time, iPhone. He wants action over warnings ("its my money and i know my risks"). Mission: progress and maintain the Pi and the AI voice assistant, then help with the Kalshi AI and other business ideas.

## Shared memory (same files for every conversation, Jarvis on the phone, and Jarvis at home)
1. At the start: read `memory/README.md`, then `memory/projects.md` and `memory/roadmap.md`, then only the topic files that matter. Also look in `memory/inbox/` (Jarvis's notes, and `pi-status.md`, the Pi's latest health snapshot) and file anything new into the right topic file.
2. While talking: if Kylar mentions something that belongs to another topic (a Pi task while in the truck chat, a family date, a business idea), write it into the right file straight away and tell him which file. Do not wait to be asked.
3. Finished things are NEVER deleted. Move them under the file's `## Done` heading with the date and result, and update `memory/projects.md`. `_archive.md` is only for dropped items.
4. One fact, one file. No passwords, API keys, tokens or account numbers (this repo is public). Keys live on the Pi. No conversation transcripts here.
5. Commit and push memory changes yourself (pull --rebase first). Jarvis reads this repo on the Pi within a few minutes of a push.
6. Record what you did: add an entry at the top of `memory/changelog.md` (date, what, where, status) whenever you change something. Read `memory/brief.md` (daily check) and `memory/changelog.md` first so you know the latest.
7. Finish what is started: before ending, update projects.md (status, next step) so nothing is left half-done without a note.

## Tools you can lean on
The Pi checks `tasks/queue/` every 3 minutes (see tasks/queue/README.md) and writes results to `memory/inbox/queue-results.md`, so you can run a command on the Pi without Kylar pasting it. A daily scheduled Claude check (6:17 am Central) files notes and writes `memory/brief.md`.

## If you are a chat that cannot push to the repo
Tell Kylar the exact lines to add, and where, or attach the repo (add_repo kylarlovelady/Starship-Lovelady with push access) and do it.

## Pi facts
Pi 5 "LoveladyMainAiHub", user kylarlovelady, repo clone ~/starship (cron pulls every ~3 min), Tailscale name loveladymainaihub.taild703ca.ts.net. Jarvis phone server: voice/ (service phone-voice, port 8099). Markets agent: markets/ (service market-agent, live mode OFF). The sandbox cannot reach the Pi; Kylar runs commands and pastes results, or reads `memory/inbox/pi-status.md`.
