#!/bin/bash
# QUEUE-OK
# Probe: what can the Pi use to slice STLs for the Bambu printer and send them over the LAN? Prints no secrets.
set -u
echo "arch: $(uname -m)  os: $(. /etc/os-release; echo $PRETTY_NAME)  ram: $(free -m | awk '/Mem:/{print $2" MB"}')  disk free: $(df -h ~ | awk 'NR==2{print $4}')"
for c in flatpak snap orca-slicer bambu-studio prusa-slicer slic3r mosquitto_pub curl; do printf "%s: " "$c"; command -v $c || echo no; done
apt-cache policy prusa-slicer 2>/dev/null | sed -n 1,3p
apt-cache policy slic3r 2>/dev/null | sed -n 1,3p
python3 -c "import paho.mqtt; print('paho-mqtt ok')" 2>&1 | tail -1
ls ~/printer* ~/.bambu* 2>/dev/null | sed 's/^/found: /' | head -3
echo "printers seen on LAN (ssdp, 4s):"
timeout 6 python3 - <<'P'
import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
try:
    s.bind(('',2021))
    s.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,socket.inet_aton('239.255.255.250')+socket.inet_aton('0.0.0.0'))
    s.settimeout(5); t=time.time()
    while time.time()-t<5:
        d,a=s.recvfrom(2048)
        t_=d.decode(errors='ignore')
        print(a[0],[l for l in t_.split('\r\n') if l.startswith(('DevModel','DevName','DevConnect','DevBind'))])
except Exception as e: print("none:",type(e).__name__)
P
