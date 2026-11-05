# Changelog: what Claude did (newest first)
Claude adds an entry every time it changes something, so any conversation, Jarvis, or Kylar can see the history. Format: date, what, where, status (built / tested here / installed on Pi / confirmed by Kylar).

## 2026-11-05 (late night, install)
- Kylar ran tasks/pi_update.sh ha: alert checker, Kalshi daily sync, task queue installed and notes sync ran (CONFIRMED by his screenshot). Home-speaker add-on copy failed: ~/homeassistant is root-owned (Docker); installer now uses sudo for the copy. First task-queue script (tasks/queue/001-diagnose.sh) pushed to check Pi-hole, HA network mode, crontab and Jarvis tools; results land in memory/inbox/queue-results.md.

## 2026-11-05 (night): making everything work together
- Jarvis tools (voice/tools.py): live facts pulled in when asked (Pi status, Kalshi agent, Pi-hole, what Claude changed) and spoken device control for lights, switches and fans via Home Assistant (locks and doors deliberately excluded). Works on phone page, Shortcut, and home speaker. Status: built, tested here with a fake Home Assistant; needs install on Pi (pi_update.sh); uses HA_TOKEN already in ~/market-data/env.
- One alert channel (tasks/alerts_check.py, every 5 min): services down, Pi hot/full, Kalshi data stale, Jarvis errors, Pi-hole down, stuck repo pull, and dated to-dos (lines starting "- YYYY-MM-DD" in memory/todo.md Open). Phone alert through Home Assistant, re-alert every 6 h, "Cleared" message, shows on Starship Mission board and Security light. Status: built, tested here; needs install on Pi.
- Front door page (voice/home.html at https://loveladymainaihub.taild703ca.ts.net/home): status chips, links to Starship, Jarvis, Lab, Live View, Hub, Pi-hole, Home Assistant, and a viewer for the memory files. Status: built, tested here.
- Task queue (tasks/queue/, tasks/queue_runner.sh): Claude leaves a script, the Pi runs it once and writes output to memory/inbox/queue-results.md. Guards: header check, deny list (speed bump, not a sandbox), no sudo, 5 min limit, kill switch ~/queue.off. Status: built, tested here; needs install; keep GitHub 2-step login on.
- Daily Claude check (scheduled task, 6:17 am Central): files inbox notes, flags problems, updates projects.md, writes memory/brief.md and a changelog entry. Status: created; first run 2026-11-05 6:17 am Central; auto-approval mode.
- Kalshi into memory: daily digest (memory/inbox/kalshi-digest.md) and data coverage (kalshi-data-status.md) from tasks/kalshi_data_sync.sh. Status: built; needs install.
- Pi-hole stats added to status snapshot, Jarvis, Starship and front door (shows "did not answer" if its API needs a login; then Claude needs the exact Pi-hole version).
- tasks/pi_update.sh: one command to install all of the above on the Pi.

## 2026-11-05 (evening)
- Rules: finished items stay under "## Done" (never deleted); memory/projects.md tracker; memory/roadmap.md (Mission 1 Pi + voice, Mission 2 Kalshi betting help); CLAUDE.md so every attached conversation follows the same rules; architecture.md. Jarvis learned "mark ... done" and memory commands now work on the voice page too.
- Home speaker uses the same Jarvis: ha/custom_components/jarvis_hub + tasks/ha_jarvis_install.sh. Status: built, untested on real Home Assistant, not installed.
- Kalshi daily data sync (tasks/kalshi_data_sync.sh).
- Status snapshot (tasks/status_report.sh -> memory/inbox/pi-status.md and hub-extra.json), Starship Mission board with the real mission, README refresh.
- Jarvis replay log (/report, Lab "Replay for Claude") and hang-up fixes (blank/noise no longer ends the chat, longer waits, echo guard). Status: built, tested with fake mic; Kylar saw hanging up before the fix; needs truck retest.
- Pi can push notes to the repo (deploy key, memory_sync every 30 min). Status: confirmed working by Kylar's output.

## 2026-11-04
- Voice server on the Pi (Brian voice, OpenAI transcription), Siri Shortcut, streaming replies, barge-in, truck mode, Lab, voice recognition basics, shared memory split into topic files, Hub Notes migrated, net watchdog script, markets review and $50 cap. See pi-home-assistant.md and kalshi-ai.md.
