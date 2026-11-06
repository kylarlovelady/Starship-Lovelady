# Home network: addresses to remember (private LAN addresses only, no passwords)

Last updated 2026-11-06. Addresses can change if a device is not reserved in the router; check Pi-hole > Network if something stops working.

| Device | Address | Notes |
|---|---|---|
| Pi (LoveladyMainAiHub) | 192.168.1.107 | DNS server for the house (Pi-hole). Also has .106 on wlan0 (two addresses; fix by reserving one in the router). On Wi-Fi, not cable yet |
| Kylar's iPhone | 192.168.1.142 | DNS set manually to 192.168.1.107; Tailscale on works fine |
| Sharee's iPhone | 192.168.1.228 | DNS set manually to 192.168.1.107 |
| iPad | to add | not done yet |
| Living room TV (Sony Google TV, Wi-Fi "Lovelady") | 192.168.1.130 | DONE 2026-11-06: Static IP, gateway 192.168.1.1, DNS 192.168.1.107, no DNS 2. Confirmed in Pi-hole (logs.netflix.com blocked). YouTube may bypass Pi-hole (not tested) |
| TV 2, 3, 4 | to add | after Pi hardening |

DNS setting used everywhere: Manual, one server, 192.168.1.107. Pi-hole dashboard is on the Pi (port 80, /admin). See pi-home-assistant.md for rollout notes and todo.md "HARDEN THE PI".

## Sony Google TV cleanup (living room), 2026-11-06
- Apps-only mode ON. Disabled: YouTube Music, Lifetime, Sony Pictures Core, Music (and My Bravia / Sony Tab if they offered Disable). Locked by Sony (cannot disable): Bravia notifications, Eco Dashboard, Sony Select. Left on purpose: Help, TV control with smart speakers, Media player, Tubi.
- Storage was nearly full: 518 MB free, cleared cached data to 841 MB free (internal storage about 4.4 GB, apps 3.4 GB). Restart pending/done; ask how it feels.
- Next ideas if still slow: Developer options animation scales to 0.5x or off, ADB bloat removal from the desktop (reversible), or an external streaming box (Google TV Streamer) for the apps.
- iPad (Kylar's son's, Safari disabled by parental controls): DNS set to 192.168.1.107 on 2026-11-06; address still to add after checking Pi-hole Recent Queries (5 active clients at 17:01).
