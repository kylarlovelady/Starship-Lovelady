#!/bin/bash
# One-time (safe to re-run): installs the Phone Voice server on the Pi, starts it as a service, and puts it on Tailscale HTTPS so the iPhone will allow the microphone.
# The home Assist/speaker setup is NOT touched. Keys are typed here (hidden) and stored only in ~/voice-data/keys.env (chmod 600).
set -u
cd ~/starship 2>/dev/null || exit 1
git pull -q 2>&1 | tail -1
V=$HOME/voice-venv
if [ ! -x "$V/bin/python" ]; then
  python3 -m venv "$V" 2>/dev/null || { echo "python venv missing: run  sudo apt install -y python3-venv  then run this again"; exit 1; }
fi
echo "Installing audio packages (a few minutes the first time)..."
"$V/bin/pip" install -q --upgrade pip 2>&1 | tail -1
"$V/bin/pip" install -q numpy scipy tqdm requests scikit-learn onnxruntime 2>&1 | tail -2
"$V/bin/pip" install -q --no-deps openwakeword 2>&1 | tail -2
"$V/bin/python" - <<'PY'
import openwakeword, sys
try:
    openwakeword.utils.download_models(["hey_jarvis"])
except TypeError:
    openwakeword.utils.download_models()
print("wake-word model ready")
PY
mkdir -p ~/voice-data; chmod 700 ~/voice-data
K=~/voice-data/keys.env; touch $K; chmod 600 $K
have() { grep -q "^$1=" $K; }
if ! have OPENAI_API_KEY; then
  echo; echo "Conversation needs your OpenAI key (the one the home assistant already uses). Paste it, then Enter (it will not show). Press Enter alone to skip for now."
  read -rs OK; echo; [ -n "$OK" ] && echo "OPENAI_API_KEY=$OK" >> $K
fi
if ! have ELEVENLABS_API_KEY; then
  echo "ElevenLabs key (same one, for the Brian voice). Enter alone to skip."
  read -rs EK; echo; [ -n "$EK" ] && echo "ELEVENLABS_API_KEY=$EK" >> $K
fi
if have ELEVENLABS_API_KEY && ! have ELEVENLABS_VOICE_ID; then
  "$V/bin/python" - <<'PY'
import json, os, urllib.request
k = dict(l.strip().split("=", 1) for l in open(os.path.expanduser("~/voice-data/keys.env")) if "=" in l)
try:
    r = urllib.request.Request("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key": k["ELEVENLABS_API_KEY"]})
    vs = json.loads(urllib.request.urlopen(r, timeout=20).read())["voices"]
    pick = [v for v in vs if v["name"].lower().startswith("brian")]
    if pick:
        open(os.path.expanduser("~/voice-data/keys.env"), "a").write("ELEVENLABS_VOICE_ID=%s\n" % pick[0]["voice_id"]); print("Found the Brian voice.")
    else:
        print("No voice named Brian on that account. Voices:", ", ".join(v["name"] for v in vs[:12]))
except Exception as e:
    print("Could not look up voices:", e)
PY
fi
sudo tee /etc/systemd/system/phone-voice.service >/dev/null <<UNIT
[Unit]
Description=Phone Voice (wake word + conversation for the phone only)
After=network-online.target
[Service]
User=$USER
WorkingDirectory=$HOME/starship/voice
ExecStart=$V/bin/python $HOME/starship/voice/phone_voice.py 8099
Restart=always
RestartSec=3
[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload && sudo systemctl enable --now phone-voice >/dev/null 2>&1
sudo systemctl restart phone-voice; sleep 3
systemctl is-active phone-voice && journalctl -u phone-voice -n 3 --no-pager 2>/dev/null | tail -3
echo; echo "Putting it on Tailscale HTTPS..."
if ! sudo tailscale serve --bg --https=443 http://127.0.0.1:8099 >/tmp/ts-serve.out 2>&1; then sudo tailscale serve --bg 8099 >/tmp/ts-serve.out 2>&1; fi
tail -4 /tmp/ts-serve.out
NAME=$(tailscale status --json 2>/dev/null | python3 -c "import sys,json;print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))" 2>/dev/null)
echo
echo "OPEN THIS ON YOUR IPHONE:  https://$NAME/"
echo "If that does not load, Tailscale HTTPS is probably not switched on: tailscale.com admin console > DNS > turn on 'HTTPS Certificates', then run this script again."
echo "Add it to your Home Screen (Share > Add to Home Screen) and tap Start listening."
