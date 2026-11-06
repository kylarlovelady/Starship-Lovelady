#!/bin/bash
# QUEUE-OK
# read-only: find the AI accelerator, check its driver/firmware/software, and what is using it
echo "== model"; tr -d '\0' < /proc/device-tree/model; echo
echo "== PCIe devices"; lspci 2>/dev/null | head -10
echo "== device nodes"; ls -l /dev/hailo* 2>&1 | head -3
echo "== kernel"; dmesg 2>/dev/null | grep -i "hailo" | tail -6 | cut -c1-200; uname -r
echo "== hailo packages"; dpkg -l 2>/dev/null | grep -i "hailo" | awk '{print $2, $3}' | head -12
echo "== hailortcli"; which hailortcli 2>&1; hailortcli fw-control identify 2>&1 | head -12
echo "== python hailo"; python3 -c "import hailo_platform; print('hailo_platform', hailo_platform.__version__)" 2>&1 | tail -1
echo "== models and examples on disk"; ls /usr/share/hailo-models 2>&1 | head -12; ls ~/hailo* 2>/dev/null | head -5
echo "== processes touching hailo"; (lsof /dev/hailo0 2>/dev/null || fuser -v /dev/hailo0 2>&1) | head -6
echo "== services that might use it"; systemctl list-units --no-legend 2>/dev/null | grep -i "hailo\|frigate\|rpicam\|whisper\|wyoming\|ollama" | cut -c1-120
echo "== docker"; docker ps --format '{{.Names}} {{.Image}}' 2>/dev/null | head -10
echo "== cpu/temp now"; uptime; vcgencmd measure_temp
