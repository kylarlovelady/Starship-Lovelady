#!/bin/bash
# Kitchen screen Pi, step 2: replace the full-screen kiosk with a normal maximised window, so the desktop, the panel and the touch keyboard button stay usable.
# Starship page opens at login; Desktop icons "Starship" and "Hub" reopen the pages any time. Run as the normal user (no sudo).
STARSHIP="http://loveladymainaihub.taild703ca.ts.net:8095/"
HUB="http://loveladymainaihub.taild703ca.ts.net:8081/hub"
[ "$(id -u)" = 0 ] && { echo "Run this as your normal user, not with sudo."; exit 1; }
FLAGS="--app=%URL% --start-maximized --ozone-platform=wayland --enable-wayland-ime --noerrdialogs --disable-infobars --no-first-run --password-store=basic --check-for-update-interval=31536000"
cat > "$HOME/kiosk.sh" <<K
#!/bin/bash
# waits for the main Pi's page, then opens it in a maximised window (not full screen kiosk)
until curl -fs -m 5 -o /dev/null "$STARSHIP"; do sleep 5; done
exec chromium ${FLAGS//%URL%/$STARSHIP}
K
chmod +x "$HOME/kiosk.sh"
mkdir -p "$HOME/.config/labwc"; grep -q kiosk.sh "$HOME/.config/labwc/autostart" 2>/dev/null || echo "$HOME/kiosk.sh &" >> "$HOME/.config/labwc/autostart"
mkdir -p "$HOME/Desktop"
mk() { cat > "$HOME/Desktop/$1.desktop" <<D
[Desktop Entry]
Type=Application
Name=$1
Exec=chromium ${FLAGS//%URL%/$2}
Icon=chromium
Terminal=false
D
chmod +x "$HOME/Desktop/$1.desktop"; }
mk Starship "$STARSHIP"; mk Hub "$HUB"
pkill chromium 2>/dev/null; sleep 1; nohup "$HOME/kiosk.sh" >/dev/null 2>&1 &
echo "DONE: Starship opens in a window; Desktop icons: Starship, Hub."
