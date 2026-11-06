#!/bin/bash
# QUEUE-OK
# read-only: is any camera attached to the Pi, and does the Hailo chip run a quick test model
echo "== cameras (Pi camera)"; rpicam-hello --list-cameras 2>&1 | head -8
echo "== video devices"; ls /dev/video* 2>&1 | head -6
echo "== usb devices"; lsusb 2>/dev/null | head -12
echo "== hailo quick benchmark (resnet, 5 s)"; timeout 40 hailortcli benchmark --time-to-run 5 /usr/share/hailo-models/resnet_v1_50_h8.hef 2>&1 | tail -8
ls /usr/share/hailo-models | grep -c h8
