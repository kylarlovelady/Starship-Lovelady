#!/bin/bash
# Kitchen screen Pi setup (run as the normal user, NOT with sudo; it asks for the password when it needs it).
# Does: SSH on, no screen blanking, Tailscale installed and joined, Chromium kiosk that opens the Hub from the main Pi.
# No software upgrade here on purpose (do that on home Wi-Fi). No passwords or keys are stored in this file.
URL="http://loveladymainaihub.taild703ca.ts.net:8081/hub"     # the page the screen shows; change this one line to switch pages
[ "$(id -u)" = 0 ] && { echo "Run this as your normal user, not with sudo."; exit 1; }
echo "== 1/5 SSH on"; sudo systemctl enable --now ssh
echo "== 2/5 screen never blanks"; sudo raspi-config nonint do_blanking 1
echo "== 3/5 Tailscale"
command -v tailscale >/dev/null || curl -fsSL https://tailscale.com/install.sh | sh
echo "== 4/5 join the tailnet (open the link it prints on your phone and sign in)"
sudo tailscale up --hostname=loveladymainaihubscreen
echo "== 5/5 kiosk"
cat > "$HOME/kiosk.sh" <<K
#!/bin/bash
# waits for the main Pi's page to answer, then opens it full screen
until curl -fs -m 5 -o /dev/null "$URL"; do sleep 5; done
exec chromium --kiosk --noerrdialogs --disable-infobars --no-first-run --password-store=basic --check-for-update-interval=31536000 "$URL"
K
chmod +x "$HOME/kiosk.sh"
mkdir -p "$HOME/.config/labwc"
grep -q kiosk.sh "$HOME/.config/labwc/autostart" 2>/dev/null || echo "$HOME/kiosk.sh &" >> "$HOME/.config/labwc/autostart"
echo "DONE. Tailscale name: $(tailscale status --self 2>/dev/null | head -1)"; echo "Reboot with: sudo reboot"
