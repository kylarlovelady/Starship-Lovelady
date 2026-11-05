#!/bin/bash
# Installs a network watchdog (root cron, every 2 min) and persistent logs.
# If the internet is down 3 checks in a row: restart NetworkManager (wifi).
# If the internet is fine but Tailscale is not connected: restart tailscaled.
# Logs each action to /var/log/net_watchdog.log so outages are visible later.
set -e
sudo tee /usr/local/bin/net_watchdog.sh >/dev/null <<'EOS'
#!/bin/bash
LOG=/var/log/net_watchdog.log; ST=/run/net_watchdog.fail
log(){ echo "$(date '+%F %T') $*" >> "$LOG"; }
if ping -c1 -W3 1.1.1.1 >/dev/null 2>&1 || ping -c1 -W3 8.8.8.8 >/dev/null 2>&1; then
  n=$(cat "$ST" 2>/dev/null || echo 0)
  [ "$n" -ge 3 ] && log "internet back after $n failed checks"
  rm -f "$ST"
  if command -v tailscale >/dev/null; then
    s=$(tailscale status --json 2>/dev/null | grep -o '"BackendState": *"[A-Za-z]*"' | head -1)
    case "$s" in *Running*) : ;; *) log "tailscale not running ($s), restarting"; systemctl restart tailscaled;; esac
  fi
else
  n=$(( $(cat "$ST" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$ST"
  log "internet check failed ($n)"
  if [ "$n" -eq 3 ]; then log "restarting NetworkManager"; systemctl restart NetworkManager; fi
  if [ "$n" -eq 6 ]; then log "restarting tailscaled"; systemctl restart tailscaled; fi
fi
EOS
sudo chmod +x /usr/local/bin/net_watchdog.sh
( sudo crontab -l 2>/dev/null | grep -v net_watchdog; echo "*/2 * * * * /usr/local/bin/net_watchdog.sh" ) | sudo crontab -
sudo mkdir -p /var/log/journal && sudo systemctl restart systemd-journald
echo "Watchdog installed. Log: /var/log/net_watchdog.log  (check: tail /var/log/net_watchdog.log)"
