#!/bin/bash
# Flip the kitchen screen 180 degrees now and at every login. Works over SSH. Undo: bash rotate.sh normal
T="${1:-180}"
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
export WAYLAND_DISPLAY="$(cd "$XDG_RUNTIME_DIR" 2>/dev/null && ls -d wayland-[0-9] 2>/dev/null | head -1)"; export WAYLAND_DISPLAY="${WAYLAND_DISPLAY:-wayland-0}"
command -v wlr-randr >/dev/null || { echo "wlr-randr is missing (sudo apt install wlr-randr)"; exit 1; }
OUT="$(wlr-randr | awk '/^[^ ]/{print $1; exit}')"
[ -z "$OUT" ] && { echo "Could not find the display."; exit 1; }
wlr-randr --output "$OUT" --transform "$T" && echo "Display $OUT set to $T."
mkdir -p "$HOME/.config/labwc"; A="$HOME/.config/labwc/autostart"; touch "$A"
sed -i '/wlr-randr --output/d' "$A"
[ "$T" = normal ] || echo "wlr-randr --output $OUT --transform $T &" >> "$A"
echo "Saved for next login. Now touch the screen to test that touch matches the picture."
