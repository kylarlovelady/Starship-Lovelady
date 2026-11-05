
## 2026-11-05 01:49:01 tasks/queue/001-diagnose.sh
```
== crontab (names only)
*/3 * * * * ~/crew-update.sh >/dev/null 2>&1
* * * * * # market-watchdog
7 * * * * # market-supervisor
20 */3 * * * # market-lab
*/30 * * * * bash $HOME/starship/tasks/memory_sync.sh >> $HOME/memory_sync.log 2>&1
*/5 * * * * # starship-alerts
10 4 * * * # kalshi-data-sync
1-59/3 * * * * # task-queue
== ha dir
drwxrwxr-x 11 kylarlovelady kylarlovelady 4096 Nov  5 01:47 /home/kylarlovelady/homeassistant
drwxr-xr-x  5 root          root          4096 Nov  5 01:46 /home/kylarlovelady/homeassistant/custom_components
== docker
openwakeword Up 5 days
whisper Up 5 days (healthy)
piper Up 5 days (healthy)
pihole Up 6 hours (healthy)
homeassistant Up About a minute
== ha network
host
== pihole
tasks/queue/001-diagnose.sh: line 8: pihole: command not found
inactive
{"error":{"key":"bad_request","message":"Bad request","hint":"The API is hosted at pi.hole/api, not pi.hole/admin/api"},"took":5.245208740234375e-06}
{"error":{"key":"unauthorized","message":"Unauthorized","hint":null},"took":5.53131103515625e-05}
== services
market-agent active
phone-voice active
tailscaled active
hub-dashboard active
hub-watchdog active
== alerts test (dry)
alerts: 0 active, 0 sent
2026-11-02 23:39:38 ISLAND updated: LIVE · $209.25 | +$1.92 this session · 0/0 rounds won · as of 11:39:36 PM
2026-11-02 23:39:56 SENT to 2 phone(s): Market agent: live ended | LIVE session ended by you. Closing the open bet.
2026-11-02 23:39:57 ISLAND cleared:  | 
== jarvis tools
{"reply": "The Pi is up for 1 week, 3 days, and has a temperature of 40.0\u00b0C, with 58% memory usage and 9% disk space used. All watched services are running smoothly.", "end": false, "followup": false}
== net watchdog
/usr/local/bin/hub-watchdog.py
/usr/local/bin/hub-watchdog.py.bak-du1026-0211
/usr/local/bin/hub-watchdog.py.bak-hn
/usr/local/bin/hub-watchdog.py.bak-pihole
/usr/local/bin/hub-watchdog.py.bak-ts1026-0210
(exit 0)
```

## 2026-11-05 01:55:01 tasks/queue/002-fix-settings.sh
```
{"ok": true, "settings": {"threshold": 0.6, "paused": false, "private": false, "models": ["/home/kylarlovelady/voice-venv/lib/python3.13/site-packages/openwakeword/resources/models/hey_jarvis_v0.1.onnx"], "follow_quiet": 25.0, "follow_question": 40.0, "voice_id": "Brian", "max_utter": 20.0, "speech_
== market-data newest files
total 190112
-rw-r--r-- 1 kylarlovelady kylarlovelady 56782392 Nov  5 01:55 ticks-20261105.jsonl
-rw-r--r-- 1 kylarlovelady kylarlovelady   313092 Nov  5 01:54 state.json
-rw-r--r-- 1 kylarlovelady kylarlovelady  1552060 Nov  5 01:54 snapshots.jsonl
-rw-r--r-- 1 kylarlovelady kylarlovelady 33332209 Nov  5 01:54 trades.jsonl
-rw-r--r-- 1 kylarlovelady kylarlovelady     2224 Nov  5 01:54 kalshi_raw.json
-rw-r--r-- 1 kylarlovelady kylarlovelady      269 Nov  5 01:50 calendar.json
-rw-r--r-- 1 kylarlovelady kylarlovelady     1721 Nov  5 01:50 entry_stats.json
-rw-r--r-- 1 kylarlovelady kylarlovelady      124 Nov  5 01:48 patterns.json
-rw-r--r-- 1 kylarlovelady kylarlovelady   146240 Nov  5 01:47 hindsight.jsonl
-rw-r--r-- 1 kylarlovelady kylarlovelady      971 Nov  5 01:47 exit_rules.json
-rw-r--r-- 1 kylarlovelady kylarlovelady   327922 Nov  5 01:45 run_log.jsonl
-rw-r--r-- 1 kylarlovelady kylarlovelady   370092 Nov  5 01:45 sim_windows.jsonl
-rw-r--r-- 1 kylarlovelady kylarlovelady     2451 Nov  5 01:45 learn_report.json
== crew-web market file
-rw-r--r-- 1 kylarlovelady kylarlovelady 191585 Nov  5 01:54 /home/kylarlovelady/crew-web/
== run.json keys
{'active': True, 'id': 1793858830, 'strategy': '...', 'start': 1000.0}
== pihole
Core version is v6.5 (Latest: N/A)
Web version is v6.6.1 (Latest: N/A)
FTL version is v6.8 (Latest: N/A)
== ha logs (jarvis_hub)
[33m2026-11-05 01:47:07.056 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration hacs which has not been tested by Home Assistant. This component might cause stability problems
[33m2026-11-05 01:50:46.731 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration jarvis_hub which has not been tested by Home Assistant. This component might cause stability pr
[33m2026-11-05 01:50:46.733 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration openai_whisper_cloud which has not been tested by Home Assistant. This component might cause st
[33m2026-11-05 01:50:46.734 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration hacs which has not been tested by Home Assistant. This component might cause stability problems
== jarvis conversations today
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    for l in open(os.path.expanduser('~/voice-data/trace.jsonl')):
             ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/home/kylarlovelady/voice-data/trace.jsonl'
(exit 0)
```
