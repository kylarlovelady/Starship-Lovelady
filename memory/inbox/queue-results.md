
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
