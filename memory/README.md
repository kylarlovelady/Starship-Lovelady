# Shared memory (Claude + Jarvis + Kylar)

One topic per file. Read this index first, then only the files that matter for the conversation.

| File | What goes in it |
|---|---|
| family.md | family people, plans, preferences, routines |
| pi-home-assistant.md | the Pi, Home Assistant, Tailscale, home screen, voice assistant (Jarvis) setup and status |
| kalshi-ai.md | the Kalshi BTC practice agent: rules, findings, status, next steps |
| amazon-kdp.md | Amazon KDP publishing work |
| business.md | business ideas, tasks, numbers (no account passwords) |
| todo.md | things to do with dates; check things off by moving them to _archive.md |
| truck-project.md | the truck and other vehicle projects: parts, steps, notes |
| projects.md | THE TRACKER: every project, its status (idea / in progress / stalled / done), next step, last touched. Keep it current; finish what is started |
| roadmap.md | the Starship's missions in order, and what must be true before moving to the next one |
| _archive.md | dropped items only (Kylar said drop it, or it was wrong). Nothing is permanently deleted |
| projects/ | one file per big project or topic (freeze-drying.md, 3d-printing.md, ...). New big project = new file here (or a folder with notes.md if it grows) and a one-line pointer in the topic file it relates to |
| inbox/ | raw notes Jarvis saved by voice on the Pi (jarvis-<topic>.md). Claude files them into the right topic file |

## Rules (same for Claude and Jarvis)
1. One fact lives in one file. Put it where it belongs; if it fits two, put it in the main one and mention it in the other in one line.
2. Never store passwords, API keys, tokens or account numbers. Say where they live instead ("keys are in ~/voice-data/keys.env on the Pi").
3. **Completed is not deleted.** Finished items stay in the file they belong to under that file's `## Done` heading, with the date finished and a short result (so each project keeps its history). `_archive.md` is only for things Kylar says to drop or that turned out wrong. Git history keeps older versions too.
4. Keep entries short, dated (YYYY-MM-DD) when time matters, and mark guesses as "(unconfirmed)".
5. If something changes, edit the old entry instead of adding a contradicting one.
6. Kylar's say-so beats a note. If a note looks wrong, ask.
7. This repo is public. Keep sensitive personal details minimal.
8. **Every conversation shares these files** (any Claude chat attached to this repo, Jarvis on the phone, Jarvis at home). If Kylar mentions something for another topic while talking about one (a Pi task in the truck chat), write it in the right file right away and tell him where it went. Before starting work on a topic, read its file; before ending, record what changed and what is next.
9. When something is finished: move its line under `## Done` with the date, update projects.md, and say so.
