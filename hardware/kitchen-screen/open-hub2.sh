#!/bin/bash
# Screen Pi: open the new glass Hub (hub2) in a window, and add a "Glass Hub" desktop icon. Run as the normal user (no sudo).
URL="http://loveladymainaihub.taild703ca.ts.net:8095/hub2/index.html"
[ "$(id -u)" = 0 ] && { echo "Run this as your normal user, not with sudo."; exit 1; }
FLAGS="--app=$URL --start-maximized --ozone-platform=wayland --enable-wayland-ime --noerrdialogs --disable-infobars --no-first-run --password-store=basic"
mkdir -p "$HOME/Desktop"
printf '[Desktop Entry]\nType=Application\nName=Glass Hub\nExec=chromium %s\nIcon=chromium\nTerminal=false\n' "$FLAGS" > "$HOME/Desktop/Glass Hub.desktop"; chmod +x "$HOME/Desktop/Glass Hub.desktop"
export XDG_RUNTIME_DIR="/run/user/$(id -u)"; export WAYLAND_DISPLAY="$(cd "$XDG_RUNTIME_DIR" 2>/dev/null && ls -d wayland-[0-9] 2>/dev/null | head -1)"; export WAYLAND_DISPLAY="${WAYLAND_DISPLAY:-wayland-0}"
pkill chromium 2>/dev/null; sleep 1
nohup chromium $FLAGS >/dev/null 2>&1 &
echo "DONE: Glass Hub should be on the screen now."
