# Home network: addresses to remember (private LAN addresses only, no passwords)

Last updated 2026-11-06. Addresses can change if a device is not reserved in the router; check Pi-hole > Network if something stops working.

| Device | Address | Notes |
|---|---|---|
| Pi (LoveladyMainAiHub) | 192.168.1.107 | DNS server for the house (Pi-hole). Also has .106 on wlan0 (two addresses; fix by reserving one in the router). On Wi-Fi, not cable yet |
| Kylar's iPhone | 192.168.1.142 | DNS set manually to 192.168.1.107; Tailscale on works fine |
| Sharee's iPhone | 192.168.1.228 | DNS set manually to 192.168.1.107 |
| iPad | to add | not done yet |
| Living room TV (Sony Google TV, Wi-Fi "Lovelady") | 192.168.1.130 | was DHCP; switching to Static with DNS 192.168.1.107 (in progress 2026-11-06) |
| TV 2, 3, 4 | to add | after Pi hardening |

DNS setting used everywhere: Manual, one server, 192.168.1.107. Pi-hole dashboard is on the Pi (port 80, /admin). See pi-home-assistant.md for rollout notes and todo.md "HARDEN THE PI".
