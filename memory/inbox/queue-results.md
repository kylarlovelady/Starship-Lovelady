ment there is nothing to buy below 99c.

## 4. Our own z-rule: first moment the model's side is z standard deviations from the target

| z | rounds | median s before close | median ask | share with an ask under 99c | median $ buyable | win rate | profit per $ (ask under 99c only) |
|---|---|---|---|---|---|---|---|
| 2.0 | 262 | 278 | 0.940 | 82% | $8757 | 90.8% | +0.9% (216 bets) |
| 2.5 | 254 | 187 | 0.963 | 61% | $4892 | 94.1% | +1.0% (156 bets) |
| 3.0 | 252 | 135 | 0.972 | 46% | $0 | 95.2% | +1.9% (116 bets) |
| 3.5 | 246 | 122 | 0.975 | 39% | $0 | 95.5% | +1.4% (96 bets) |
| 4.0 | 242 | 89 | 0.981 | 32% | $0 | 96.7% | +2.3% (78 bets) |

Win = real settled result when known, otherwise the average of the last 60 Coinbase prices vs the target (stand-in for Kalshi's average).
(exit 0)
```

## 2026-11-05 21:31:01 tasks/queue/059-send-interior.sh
```
(exit 0)
```

## 2026-11-05 22:04:02 tasks/queue/060-send-cover-b.sh
```
(exit 0)
```

## 2026-11-05 22:58:02 tasks/queue/061-send-covers-ce.sh
```
(exit 0)
```

## 2026-11-05 23:19:01 tasks/queue/062-build-orchid.sh
```
orchid build started in the background
(exit 0)
```

## 2026-11-05 23:25:01 tasks/queue/063-kdp-series-check.sh
```
fonts found: ['Bitstream Vera', 'Caladea', 'Carlito', 'DejaVu Sans', 'DejaVu Serif', 'FreeSans', 'FreeSerif', 'Lato', 'Liberation Mono', 'Liberation Sans', 'Liberation Serif', 'Open Sans', 'Playfair Display', 'Roboto']
title font: Liberation Serif | interior font: Lato
would build process-operator a #18233D #CDB360
would build process-operator b #1F372A #CDB360
would build process-operator c #4D1E28 #CDB360
would build process-operator e #5B2A6E #CDB360
would build lab-operator a #18233D #CDB360
would build lab-operator b #1F372A #CDB360
would build lab-operator c #4D1E28 #CDB360
would build lab-operator e #5B2A6E #CDB360
partial build or check, no contact sheet
== Process Operator
Title: Process Operator | Author: Lovelady LLC | no subtitle | price $18.99
Description: A durable hardcover notebook for process operators: 120 numbered, lined pages (6 x 9 in) on cream paper, with an owner page for name, phone, email and company. Keep shift notes, readings, handoffs, checklists and daily logs in one place built to hold up on the job.
Keywords: Notebook for work; Hardcover lined notebook; Tradesman notebook; Work notebook for men; Blue collar gifts; Plant operator gifts; Blue collar gifts for women
Colours: Navy (A), Forest green (B), Burgundy (C), Orchid purple (E)

== Lab Operator
Title: Lab Operator | Author: Lovelady LLC | no subtitle | price $18.99
Description: A durable hardcover notebook for lab operators: 120 numbered, lined pages (6 x 9 in) on cream paper, with an owner page for name, phone, email and company. Keep shift notes, readings, samples, results, checklists and daily logs in one place built to hold up on the job.
Keywords: Notebook for work; Hardcover lined notebook; Tradesman notebook; Work notebook for men; Blue collar gifts; Lab technician gifts; Blue collar gifts for women
Colours: Navy (A), Forest green (B), Burgundy (C), Orchid purple (E)

(exit 0)
```

## 2026-11-06 00:01:01 tasks/queue/064-starship-check2.sh
```
y Jarvis voice assistant (phone) | in progress. Next: Truck test with the replay log; tune speed, hang-ups, voice ID
y Jarvis at home (Home Assistant speaker) | in progress. Next: Add-on installed; Jarvis Hub integration added in Home Assistant (Kylar, 2026-11-05); test at home, t
y Shared memory (Claude, Jarvis, Pi) | in progress. Next: Run for a week; daily Claude check to file inbox notes
y Pi health and network | in progress. Next: Net watchdog installed 2026-11-05; at-home tasks (router reservations, Pi-hole pilot)
crew.json written
page copy: same as repo
projects rows in served json: 14
page 200 147167b
(exit 0)
```

## 2026-11-06 00:31:01 tasks/queue/065-diag-5-7.sh
```
== sniper log tail
{"t":1793945730,"ticker":"KXBTC15M-26NOV060115-15","result":"ROUND","max_abs_z":68.12,"left_at_max_z":1.4,"z_ever_ge_min":true,"bought":false}
{"t":1793946456,"ticker":"KXBTC15M-26NOV060130-30","result":"Z_NOBUY","z":4.12,"left":143.9,"sigma_per_s":3.53,"why":"z reached the trigger but nothing for sale at or below 98.5c"}
{"t":1793946598,"ticker":"KXBTC15M-26NOV060130-30","left_at_book":1.19,"book_ms":170,"status":{"status":"active","close_time":"2026-11-06T06:30:00Z","can_close_early":true,"yes_bid_dollars":"0.9990","yes_ask_dollars":"1.0000","no_bid_dollars":"0.0000","no_ask_dollars":"0.0010"},"px":75552.6,"strike"
{"t":1793946617,"ticker":"KXBTC15M-26NOV060130-30","result":"ROUND","max_abs_z":26.68,"left_at_max_z":1.9,"z_ever_ge_min":true,"bought":false}
== agent restarts
== hub-dashboard files
total 364
drwxrwxr-x 2 kylarlovelady kylarlovelady  4096 Nov  4 14:52 backgrounds
-rw-rw-r-- 1 kylarlovelady kylarlovelady  4348 Oct 20 20:23 crop_api.py
-rw-r--r-- 1 kylarlovelady kylarlovelady  1147 Oct 26 22:14 device-names.json
-rw-r--r-- 1 kylarlovelady kylarlovelady   138 Oct 26 22:11 device-names.json.bak-oct26
drwxrwxr-x 2 kylarlovelady kylarlovelady  4096 Oct 20 21:15 fontcache
-rw-rw-r-- 1 kylarlovelady kylarlovelady  1841 Oct 25 22:21 health_api.py
-rw-r--r-- 1 kylarlovelady kylarlovelady  3025 Oct 26 22:23 hub_api.py
-rw-r--r-- 1 kylarlovelady kylarlovelady  2913 Oct 22 16:25 hub_api.py.bak-jh
-rw-r--r-- 1 kylarlovelady kylarlovelady  2949 Oct 26 22:23 hub_api.py.bak-names
-rw-r--r-- 1 kylarlovelady kylarlovelady 11098 Nov  5 03:04 hub.html
-rw-r--r-- 1 kylarlovelady kylarlovelady  7400 Oct 30 14:51 hub.html.bak-cr
-rw-r--r-- 1 kylarlovelady kylarlovelady  8936 Oct 30 15:25 hub.html.bak-crop
-rw-r--r-- 1 kylarlovelady kylarlovelady  8936 Oct 30 15:20 hub.html.bak-dbg
-rw-r--r-- 1 kylarlovelady kylarlovelady  8992 Oct 30 15:28 hub.html.bak-ha
-rw-r--r-- 1 kylarlovelady kylarlovelady  7093 Oct 25 22:22 hub.html.bak-hl
-rw-r--r-- 1 kylarlovelady kylarlovelady  7550 Oct 30 15:01 hub.html.bak-imm
-rw-r--r-- 1 kylarlovelady kylarlovelady  8850 Oct 30 15:10 hub.html.bak-imm2
-rw-r--r-- 1 kylarlovelady kylarlovelady  7291 Oct 25 23:00 hub.html.bak-ly
-rw-r--r-- 1 kylarlovelady kylarlovelady 10776 Nov  2 00:51 hub.html.bak-markets
== font settings
1:{"version": 1793826125, "font": "Great Vibes", "clock_color": "#000000", "date_color": "#000000", "weather_color": "#000000", "text_color": "#000000", "bg_mode": "image", "bg_color": "#05080f", "bg_image": "bg-1793825570392.jpg", "dim": 0.0, "reload": 1793825746749, "layout": {"on": true, "clock": {"x": 49.83436622241936, "y": 80.02630104285585, "k": 0.56}, "date": {"x": 65.18151689283918, "y": 88.76360052796805, "k": 1.0}, "wx": {"x": 98.01980198019801, "y": 75.93233328576865, "k": 0.81}}}
== popup/reply markup in index.html
28:#you{font-size:2.6vw;color:var(--cyan);min-height:3.4vw;margin-bottom:1.5vh}
31:/*glass*/#bubble{display:flex;flex-direction:column;align-items:center;padding:2.2vh 5vw 2.4vh;border-radius:34px;background:rgba(255,255,255,.5);max-width:92vw;
34:#bubble #clock{text-shadow:none!important}#bubble #date{margin-bottom:1.6vh}
37:<div id="bubble"><div id="clock">--:--</div><div id="date"></div>
40:<div class="lbl">You</div><div id="you"></div><div class="lbl">Alexa</div><div id="ai"></div><img id="pic" alt=""></div>
121:var bu=g('bubble');if(bu){if(s.glass===false){bu.style.cssText='background:none;border:0;box-shadow:none;-webkit-backdrop-filter:none;backdrop-filter:none;padding:0';}
(exit 0)
```

## 2026-11-06 00:34:02 tasks/queue/066-diag-5-7b.sh
```
== log lines for the 01:00 (00:00 local) round
{"t":1793944799,"ticker":"KXBTC15M-26NOV060100-00","left_at_book":0.97,"book_ms":346,"status":{"status":"active","close_time":"2026-11-06T06:00:00Z","can_close_early":true,"yes_bid_dollars":"0.9990","yes_ask_dollars":"1.0000","no_bid_dollars":"0.0000","no_ask_dollars":"0.0010"},"px":75585.38,"strike":75529.93,"result":"SKIP","why":"one side of the book is empty (nobody to buy from): yes levels 10,
{"t":1793944806,"ticker":"KXBTC15M-26NOV060100-00","result":"MISSED","why":"no book reply landed with 1.3 s or less to go; last status None"}
== agent journal 23:57 to 00:03
== tick coverage 23:59:00 to 00:00:10 (rows per second)
seconds with a row: 78 of 80; last row (left, ticker, has book): (590, 'KXBTC15M-26NOV060130-30', True)
== font in index.html
8: font-family:"Segoe UI",system-ui,sans-serif;height:100vh;overflow:hidden;display:flex;
10:#clock{font-size:15vw;font-weight:200;letter-spacing:.02em;color:var(--cyan);
12:#date{font-size:2.6vw;color:var(--dim);letter-spacing:.2em;text-transform:uppercase;margin-bottom:4vh}
13:#wx{display:flex;gap:4vw;align-items:baseline;font-size:2.4vw;color:var(--dim)}
14:#temp{font-size:7vw;font-weight:200;color:#e8f4ff}
15:#cond{font-size:3vw;color:#e8f4ff}
21:#status{display:flex;align-items:center;gap:1.2vw;font-size:2vw;letter-spacing:.2em;
27:.lbl{font-size:1.7vw;color:var(--dim);text-transform:uppercase;letter-spacing:.15em}
28:#you{font-size:2.6vw;color:var(--cyan);min-height:3.4vw;margin-bottom:1.5vh}
29:#ai{font-size:3vw;line-height:1.3;min-height:4vw}
83:#mutebtn{position:fixed;right:18px;bottom:18px;padding:12px 20px;border-radius:999px;border:1px solid rgba(255,255,255,.4);background:rgba(255,255,255,.12);color:#fff;font:600 16px sans-serif;letter-spacing:.08em;cursor:pointer;z-index:9999;}
113:b.fontFamily=s.font?'"'+s.font+'",system-ui,sans-serif':'';
(exit 0)
```

## 2026-11-06 00:37:01 tasks/queue/067-popup-font.sh
```
patched: pop-up text now uses the normal font
1
(exit 0)
```

## 2026-11-06 01:22:01 tasks/queue/068-ai-chip-check.sh
```
== model
Raspberry Pi 5 Model B Rev 1.1
== PCIe devices
0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 30)
0001:01:00.0 Co-processor: Hailo Technologies Ltd. Hailo-8 AI Processor (rev 01)
0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 30)
0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
== device nodes
crw-rw-rw- 1 root root 509, 0 Oct 25 11:59 /dev/hailo0
== kernel
6.18.50+rpt-rpi-2712
== hailo packages
hailo-all 5.1.1
hailo-models 1.0.0-2
hailo-tappas-core 5.1.0
hailort 4.23.0
hailort-pcie-driver 4.23.0
python3-hailo-tappas 5.1.0
python3-hailort 4.23.0-1
rpicam-apps-hailo-postprocess 1.14.0-1
== hailortcli
/usr/bin/hailortcli
Executing on device: 0001:01:00.0
Identifying board
Control Protocol Version: 2
Firmware Version: 4.23.0 (release,app,extended context switch buffer)
Logger Version: 0
Board Name: Hailo-8                         
Device Architecture: HAILO8
Serial Number: HLLWM2A233900170
Part Number: HM218B1C2FAE
Product Name: HAILO-8 AI ACC M.2 M KEY MODULE EXT TEMP

== python hailo
hailo_platform 4.23.0
== models and examples on disk
resnet_v1_50_h10.hef
resnet_v1_50_h8l.hef
scrfd_2.5g_h8l.hef
yolov11m_h10.hef
yolov5n_seg_h10.hef
yolov5n_seg_h8.hef
yolov5n_seg_h8l_mz.hef
yolov5_personface.json
yolov5seg.json
yolov5s_personface_h8l.hef
yolov6n_h8.hef
yolov6n_h8l.hef
== processes touching hailo
== services that might use it
  hailort.service                                                                                                       
  hub-satellite.service                                                                                                 
== docker
openwakeword rhasspy/wyoming-openwakeword
whisper rhasspy/wyoming-whisper
piper rhasspy/wyoming-piper
pihole pihole/pihole:latest
homeassistant ghcr.io/home-assistant/home-assistant:stable
== cpu/temp now
 01:22:02 up 11 days, 14:22,  4 users,  load average: 3.64, 2.37, 2.08
temp=45.0'C
(exit 0)
```

## 2026-11-06 01:25:02 tasks/queue/069-camera-check.sh
```
== cameras (Pi camera)
No cameras available!
== video devices
/dev/video19
/dev/video20
/dev/video21
/dev/video22
/dev/video23
/dev/video24
== usb devices
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 041e:3272 Creative Technology, Ltd Pebble V3
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 002 Device 002: ID 0bda:9210 Realtek Semiconductor Corp. RTL9210 M.2 NVME Adapter
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 010: ID 214b:7250 Huasheng Electronics USB2.0 HUB
Bus 003 Device 011: ID 214b:7250 Huasheng Electronics USB2.0 HUB
Bus 003 Device 013: ID 15dd:000b MXL  MXL AC-44  
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
== hailo quick benchmark (resnet, 5 s)
hef: File does not exist: /usr/share/hailo-models/resnet_v1_50_h8.hef
Run with --help for more information.
12
(exit 0)
```

## 2026-11-06 01:28:01 tasks/queue/070-hailo-bench.sh
```

=======
Summary
=======
FPS     (hw_only)                 = 283.044
        (streaming)               = 282.696
Latency (hw)                      = 5.04367 ms
Device 0001:01:00.0:
  Power in streaming mode (average) = 1.78362 W
                          (max)     = 1.79414 W
== temp
A subcommand is required
Run with --help for more information.
(exit 0)
```

## 2026-11-06 02:55:01 tasks/queue/071-oracle-study.sh
```

## 2026-11-06 02:58:02 tasks/queue/071-oracle-study.sh
```

## 2026-11-06 03:01:01 tasks/queue/071-oracle-study.sh
```

## 2026-11-06 03:04:02 tasks/queue/071-oracle-study.sh
```

## 2026-11-06 03:07:01 tasks/queue/071-oracle-study.sh
```

## 2026-11-06 03:10:02 tasks/queue/071-oracle-study.sh
```

## 2026-11-06 03:13:01 tasks/queue/071-oracle-study.sh
```

## 2026-11-06 03:16:02 tasks/queue/071-oracle-study.sh
```
# Hindsight / oracle study (last 7 days)

Rounds with a full recording, a strike and a real Kalshi result: **307** (149 UP, 158 DOWN).

## A. The perfect-hindsight buy (cheapest ask of the side that won, with 3+ s left)

| statistic | value |
|---|---|
| rounds with a usable book | 307 |
| median cheapest winning ask | 39c |
| average perfect-hindsight profit per contract | 61.1c (157% on cost) |
| share of rounds where the perfect buy was 30c or less | 33% |
| share where it was 50c or less | 78% |
| WHEN in the round the cheapest winning ask was (seconds left) | 0-60 s: 2%, 60-180 s: 5%, 180-420 s: 15%, >420 s: 76% |

Reading: the perfect buy is nearly always a *cheap* winner early in the round that you could not have known about. The rest of this report asks which signals could have pointed to it in advance.

## B. Which signals predict UP/DOWN? (AUC: 0.50 = coin flip, 1.00 = perfect, below 0.50 = points the other way)

Each cell: AUC all rounds (older half / newer half). **Bold** = 0.60 or more (or 0.40 or less) AND the same side of 0.50 in both halves. 'vs market' = rank correlation of the signal with (result minus Kalshi mid), i.e. does it know something the price does not. Roughly +-0.13 is noise at this sample size.

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | **0.77 (0.73 / 0.82)** | **0.85 (0.80 / 0.89)** | **0.89 (0.85 / 0.91)** | **0.93 (0.91 / 0.94)** | **0.98 (0.99 / 0.98)** | **1.00 (1.00 / 0.99)** |
| dist $ (btc - strike) | **0.78 (0.74 / 0.82)** | **0.86 (0.81 / 0.91)** | **0.90 (0.87 / 0.91)** | **0.93 (0.92 / 0.93)** | **0.98 (0.99 / 0.97)** | **0.99 (1.00 / 0.99)** |
| mom 10s $ | 0.57 (0.55 / 0.58) | 0.51 (0.52 / 0.50) | 0.49 (0.50 / 0.48) | 0.52 (0.54 / 0.49) | 0.52 (0.49 / 0.54) | 0.53 (0.55 / 0.52) |
| mom 30s $ | **0.61 (0.62 / 0.61)** | 0.58 (0.61 / 0.56) | 0.54 (0.53 / 0.55) | 0.57 (0.66 / 0.46) | 0.58 (0.57 / 0.60) | 0.56 (0.54 / 0.58) |
| mom 60s $ | 0.58 (0.55 / 0.60) | **0.65 (0.65 / 0.65)** | 0.56 (0.58 / 0.55) | 0.56 (0.65 / 0.47) | **0.62 (0.62 / 0.60)** | **0.63 (0.61 / 0.65)** |
| kraken - coinbase $ | 0.48 (0.52 / 0.44) | 0.49 (0.48 / 0.52) | 0.52 (0.53 / 0.51) | 0.43 (0.32 / 0.55) | 0.42 (0.44 / 0.40) | 0.51 (0.48 / 0.55) |
| trade flow imbalance | 0.50 (0.49 / 0.51) | 0.48 (0.43 / 0.53) | 0.50 (0.51 / 0.51) | 0.53 (0.52 / 0.55) | 0.57 (0.58 / 0.56) | 0.55 (0.59 / 0.52) |
| coinbase book imbalance | 0.51 (0.69 / 0.41) | 0.47 (0.61 / 0.42) | 0.45 (0.55 / 0.39) | 0.50 (0.54 / 0.51) | 0.53 (0.64 / 0.48) | 0.49 (0.47 / 0.49) |
| kalshi book imbalance | 0.48 (0.48 / 0.47) | 0.59 (0.57 / 0.61) | 0.45 (0.51 / 0.41) | **0.33 (0.29 / 0.37)** | **0.33 (0.35 / 0.30)** | **0.24 (0.31 / 0.19)** |
| kalshi mid (crowd) | **0.78 (0.72 / 0.83)** | **0.86 (0.80 / 0.91)** | **0.90 (0.87 / 0.92)** | **0.93 (0.91 / 0.94)** | **0.97 (0.98 / 0.96)** | **0.97 (1.00 / 0.93)** |
| funding rate | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) |

### Does it beat the market price? (rank correlation with result minus Kalshi mid)

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | -0.00 | +0.16 | +0.24 | +0.32 | +0.45 | +0.45 |
| dist $ (btc - strike) | +0.01 | +0.18 | +0.26 | +0.31 | +0.44 | +0.43 |
| mom 10s $ | +0.08 | -0.05 | -0.08 | -0.01 | +0.03 | +0.09 |
| mom 30s $ | +0.02 | +0.04 | +0.03 | +0.03 | +0.09 | +0.07 |
| mom 60s $ | -0.06 | +0.15 | +0.01 | -0.06 | +0.09 | +0.13 |
| kraken - coinbase $ | +0.02 | +0.05 | +0.05 | -0.09 | -0.18 | +0.10 |
| trade flow imbalance | +0.03 | -0.04 | -0.01 | +0.08 | +0.15 | +0.21 |
| coinbase book imbalance | -0.00 | -0.01 | -0.05 | -0.00 | +0.06 | -0.07 |
| kalshi book imbalance | +0.04 | +0.14 | -0.00 | -0.04 | -0.06 | -0.14 |
| kalshi mid (crowd) | -0.01 | +0.15 | +0.24 | +0.31 | +0.42 | +0.42 |
| funding rate | -0.02 | -0.01 | -0.03 | -0.02 | -0.01 | +0.11 |

## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result

| left | min gap | bets | win rate | profit per $ staked | avg cost |
|---|---|---|---|---|---|
| 600s | 0.05 | 69 | 41% | +1.5% | 0.40 |
| 600s | 0.10 | 31 | 42% | +25.6% | 0.33 |
| 600s | 0.20 | 4 | 50% | +27.0% | 0.39 |
| 420s | 0.05 | 89 | 29% | +5.1% | 0.28 |
| 420s | 0.10 | 44 | 23% | +26.3% | 0.18 |
| 420s | 0.20 | 3 | 0% | -100.0% | 0.09 |
| 300s | 0.05 | 77 | 25% | -4.3% | 0.26 |
| 300s | 0.10 | 36 | 19% | -4.6% | 0.20 |
| 300s | 0.20 | 2 | 50% | +411.5% | 0.10 |
| 180s | 0.05 | 63 | 29% | +1.9% | 0.28 |
| 180s | 0.10 | 32 | 31% | +30.1% | 0.24 |
| 180s | 0.20 | 1 | 100% | +490.3% | 0.17 |
| 90s | 0.05 | 66 | 17% | -11.6% | 0.19 |
| 90s | 0.10 | 35 | 11% | -23.3% | 0.15 |
| 90s | 0.20 | 6 | 0% | -100.0% | 0.09 |
| 45s | 0.05 | 35 | 23% | +42.0% | 0.16 |
| 45s | 0.10 | 33 | 24% | +52.9% | 0.16 |
| 45s | 0.20 | 21 | 14% | +4.1% | 0.14 |

## How much to trust this

- 307 rounds, many signals x checkpoints: a few will look good by luck. Only a signal that stays on the same side in both halves, at several checkpoints, deserves a real test.
- Hindsight always finds a great trade. The test that matters is walk-forward: pick the rule on older rounds, test it on newer ones, after fees.
- Practice only. Nothing here changes any setting.
(exit 0)
```

## 2026-11-06 03:17:44 tasks/queue/072-oracle-check.sh
```
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5459 Nov  6 03:16 /home/kylarlovelady/starship/memory/inbox/oracle-study.md
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5459 Nov  6 03:16 /tmp/oracle-study.out
366M	/home/kylarlovelady/market-data
agent_trades.json
alerts.log
archive
calendar.json
calls.jsonl
coach_rules.json
config.json
entry_stats.json
env
exit_rules.json
exits.jsonl
hindsight.jsonl
history
innovations.jsonl
island.json
kalshi_key.pem
kalshi_raw.json
kalshi_sync.log
lab.log
lab_log.jsonl
# Hindsight / oracle study (last 7 days)

Rounds with a full recording, a strike and a real Kalshi result: **307** (149 UP, 158 DOWN).

## A. The perfect-hindsight buy (cheapest ask of the side that won, with 3+ s left)

| statistic | value |
|---|---|
| rounds with a usable book | 307 |
| median cheapest winning ask | 39c |
| average perfect-hindsight profit per contract | 61.1c (157% on cost) |
| share of rounds where the perfect buy was 30c or less | 33% |
| share where it was 50c or less | 78% |
| WHEN in the round the cheapest winning ask was (seconds left) | 0-60 s: 2%, 60-180 s: 5%, 180-420 s: 15%, >420 s: 76% |

Reading: the perfect buy is nearly always a *cheap* winner early in the round that you could not have known about. The rest of this report asks which signals could have pointed to it in advance.

## B. Which signals predict UP/DOWN? (AUC: 0.50 = coin flip, 1.00 = perfect, below 0.50 = points the other way)

Each cell: AUC all rounds (older half / newer half). **Bold** = 0.60 or more (or 0.40 or less) AND the same side of 0.50 in both halves. 'vs market' = rank correlation of the signal with (result minus Kalshi mid), i.e. does it know something the price does not. Roughly +-0.13 is noise at this sample size.

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | **0.77 (0.73 / 0.82)** | **0.85 (0.80 / 0.89)** | **0.89 (0.85 / 0.91)** | **0.93 (0.91 / 0.94)** | **0.98 (0.99 / 0.98)** | **1.00 (1.00 / 0.99)** |
| dist $ (btc - strike) | **0.78 (0.74 / 0.82)** | **0.86 (0.81 / 0.91)** | **0.90 (0.87 / 0.91)** | **0.93 (0.92 / 0.93)** | **0.98 (0.99 / 0.97)** | **0.99 (1.00 / 0.99)** |
| mom 10s $ | 0.57 (0.55 / 0.58) | 0.51 (0.52 / 0.50) | 0.49 (0.50 / 0.48) | 0.52 (0.54 / 0.49) | 0.52 (0.49 / 0.54) | 0.53 (0.55 / 0.52) |
| mom 30s $ | **0.61 (0.62 / 0.61)** | 0.58 (0.61 / 0.56) | 0.54 (0.53 / 0.55) | 0.57 (0.66 / 0.46) | 0.58 (0.57 / 0.60) | 0.56 (0.54 / 0.58) |
| mom 60s $ | 0.58 (0.55 / 0.60) | **0.65 (0.65 / 0.65)** | 0.56 (0.58 / 0.55) | 0.56 (0.65 / 0.47) | **0.62 (0.62 / 0.60)** | **0.63 (0.61 / 0.65)** |
| kraken - coinbase $ | 0.48 (0.52 / 0.44) | 0.49 (0.48 / 0.52) | 0.52 (0.53 / 0.51) | 0.43 (0.32 / 0.55) | 0.42 (0.44 / 0.40) | 0.51 (0.48 / 0.55) |
| trade flow imbalance | 0.50 (0.49 / 0.51) | 0.48 (0.43 / 0.53) | 0.50 (0.51 / 0.51) | 0.53 (0.52 / 0.55) | 0.57 (0.58 / 0.56) | 0.55 (0.59 / 0.52) |
| coinbase book imbalance | 0.51 (0.69 / 0.41) | 0.47 (0.61 / 0.42) | 0.45 (0.55 / 0.39) | 0.50 (0.54 / 0.51) | 0.53 (0.64 / 0.48) | 0.49 (0.47 / 0.49) |
| kalshi book imbalance | 0.48 (0.48 / 0.47) | 0.59 (0.57 / 0.61) | 0.45 (0.51 / 0.41) | **0.33 (0.29 / 0.37)** | **0.33 (0.35 / 0.30)** | **0.24 (0.31 / 0.19)** |
| kalshi mid (crowd) | **0.78 (0.72 / 0.83)** | **0.86 (0.80 / 0.91)** | **0.90 (0.87 / 0.92)** | **0.93 (0.91 / 0.94)** | **0.97 (0.98 / 0.96)** | **0.97 (1.00 / 0.93)** |
| funding rate | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) |

### Does it beat the market price? (rank correlation with result minus Kalshi mid)

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | -0.00 | +0.16 | +0.24 | +0.32 | +0.45 | +0.45 |
| dist $ (btc - strike) | +0.01 | +0.18 | +0.26 | +0.31 | +0.44 | +0.43 |
| mom 10s $ | +0.08 | -0.05 | -0.08 | -0.01 | +0.03 | +0.09 |
| mom 30s $ | +0.02 | +0.04 | +0.03 | +0.03 | +0.09 | +0.07 |
| mom 60s $ | -0.06 | +0.15 | +0.01 | -0.06 | +0.09 | +0.13 |
| kraken - coinbase $ | +0.02 | +0.05 | +0.05 | -0.09 | -0.18 | +0.10 |
| trade flow imbalance | +0.03 | -0.04 | -0.01 | +0.08 | +0.15 | +0.21 |
| coinbase book imbalance | -0.00 | -0.01 | -0.05 | -0.00 | +0.06 | -0.07 |
| kalshi book imbalance | +0.04 | +0.14 | -0.00 | -0.04 | -0.06 | -0.14 |
| kalshi mid (crowd) | -0.01 | +0.15 | +0.24 | +0.31 | +0.42 | +0.42 |
| funding rate | -0.02 | -0.01 | -0.03 | -0.02 | -0.01 | +0.11 |

## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result

| left | min gap | bets | win rate | profit per $ staked | avg cost |
|---|---|---|---|---|---|
| 600s | 0.05 | 69 | 41% | +1.5% | 0.40 |
| 600s | 0.10 | 31 | 42% | +25.6% | 0.33 |
| 600s | 0.20 | 4 | 50% | +27.0% | 0.39 |
| 420s | 0.05 | 89 | 29% | +5.1% | 0.28 |
| 420s | 0.10 | 44 | 23% | +26.3(exit 0)
```

## 2026-11-06 03:17:44 tasks/queue/073-oracle-light.sh
```
               total        used        free      shared  buff/cache   available
Mem:            8058        2589        2228          64        3391        5469
Mem:            8058        2489        2327          63        3392        5569
# Hindsight / oracle study (last 3 days)

Rounds with a full recording, a strike and a real Kalshi result: **300** (147 UP, 153 DOWN).

## A. The perfect-hindsight buy (cheapest ask of the side that won, with 3+ s left)

| statistic | value |
|---|---|
| rounds with a usable book | 300 |
| median cheapest winning ask | 39c |
| average perfect-hindsight profit per contract | 61.0c (157% on cost) |
| share of rounds where the perfect buy was 30c or less | 32% |
| share where it was 50c or less | 78% |
| WHEN in the round the cheapest winning ask was (seconds left) | 0-60 s: 2%, 60-180 s: 5%, 180-420 s: 15%, >420 s: 77% |

Reading: the perfect buy is nearly always a *cheap* winner early in the round that you could not have known about. The rest of this report asks which signals could have pointed to it in advance.

## B. Which signals predict UP/DOWN? (AUC: 0.50 = coin flip, 1.00 = perfect, below 0.50 = points the other way)

Each cell: AUC all rounds (older half / newer half). **Bold** = 0.60 or more (or 0.40 or less) AND the same side of 0.50 in both halves. 'vs market' = rank correlation of the signal with (result minus Kalshi mid), i.e. does it know something the price does not. Roughly +-0.13 is noise at this sample size.

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | **0.78 (0.74 / 0.83)** | **0.85 (0.80 / 0.89)** | **0.90 (0.87 / 0.91)** | **0.93 (0.92 / 0.93)** | **0.98 (0.99 / 0.98)** | **0.99 (1.00 / 0.99)** |
| dist $ (btc - strike) | **0.78 (0.75 / 0.82)** | **0.86 (0.81 / 0.91)** | **0.90 (0.89 / 0.91)** | **0.93 (0.93 / 0.93)** | **0.98 (0.99 / 0.97)** | **0.99 (1.00 / 0.99)** |
| mom 10s $ | 0.57 (0.55 / 0.59) | 0.50 (0.50 / 0.50) | 0.49 (0.51 / 0.48) | 0.52 (0.53 / 0.50) | 0.52 (0.49 / 0.55) | 0.52 (0.51 / 0.53) |
| mom 30s $ | **0.62 (0.63 / 0.61)** | 0.58 (0.60 / 0.57) | 0.54 (0.55 / 0.54) | 0.56 (0.64 / 0.47) | 0.59 (0.57 / 0.61) | 0.56 (0.52 / 0.59) |
| mom 60s $ | 0.58 (0.56 / 0.60) | **0.66 (0.66 / 0.66)** | 0.57 (0.59 / 0.55) | 0.55 (0.63 / 0.47) | **0.62 (0.60 / 0.62)** | **0.62 (0.59 / 0.66)** |
| kraken - coinbase $ | 0.48 (0.53 / 0.44) | 0.50 (0.50 / 0.51) | 0.53 (0.54 / 0.52) | 0.44 (0.36 / 0.53) | 0.42 (0.44 / 0.38) | 0.52 (0.52 / 0.52) |
| trade flow imbalance | 0.50 (0.48 / 0.52) | 0.48 (0.41 / 0.54) | 0.51 (0.52 / 0.51) | 0.54 (0.55 / 0.54) | 0.58 (0.60 / 0.57) | 0.54 (0.56 / 0.53) |
| coinbase book imbalance | 0.51 (0.65 / 0.43) | 0.47 (0.60 / 0.42) | 0.45 (0.51 / 0.40) | 0.50 (0.52 / 0.51) | 0.53 (0.60 / 0.49) | 0.49 (0.47 / 0.49) |
| kalshi book imbalance | 0.47 (0.46 / 0.48) | 0.59 (0.58 / 0.61) | 0.46 (0.51 / 0.42) | **0.33 (0.27 / 0.38)** | **0.32 (0.34 / 0.30)** | **0.24 (0.29 / 0.20)** |
| kalshi mid (crowd) | **0.79 (0.73 / 0.84)** | **0.86 (0.80 / 0.91)** | **0.90 (0.88 / 0.92)** | **0.93 (0.92 / 0.93)** | **0.97 (0.98 / 0.96)** | **0.97 (1.00 / 0.93)** |
| funding rate | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) | 0.50 (0.50 / 0.50) |

### Does it beat the market price? (rank correlation with result minus Kalshi mid)

| signal | 600s left | 420s left | 300s left | 180s left | 90s left | 45s left |
|---|---|---|---|---|---|---|
| z (btc vs strike, in sigmas) | +0.01 | +0.16 | +0.26 | +0.33 | +0.44 | +0.45 |
| dist $ (btc - strike) | +0.01 | +0.18 | +0.27 | +0.32 | +0.44 | +0.43 |
| mom 10s $ | +0.08 | -0.07 | -0.08 | +0.01 | +0.04 | +0.09 |
| mom 30s $ | +0.03 | +0.04 | +0.03 | +0.01 | +0.10 | +0.07 |
| mom 60s $ | -0.06 | +0.15 | +0.03 | -0.07 | +0.10 | +0.14 |
| kraken - coinbase $ | +0.01 | +0.06 | +0.06 | -0.08 | -0.19 | +0.09 |
| trade flow imbalance | +0.03 | -0.05 | +0.01 | +0.09 | +0.17 | +0.20 |
| coinbase book imbalance | -0.00 | -0.01 | -0.05 | -0.00 | +0.06 | -0.07 |
| kalshi book imbalance | +0.03 | +0.14 | +0.01 | -0.04 | -0.06 | -0.13 |
| kalshi mid (crowd) | +0.00 | +0.15 | +0.26 | +0.32 | +0.41 | +0.42 |
| funding rate | -0.02 | -0.01 | -0.03 | -0.02 | -0.01 | +0.11 |

## C. Simple edge rule: model chance Phi(z) vs the Kalshi ask, buy the side with the bigger gap if gap > threshold (after fee), hold to the result

| left | min gap | bets | win rate | profit per $ staked | avg cost |
|---|---|---|---|---|---|
| 600s | 0.05 | 68 | 40% | +0.8% | 0.39 |
| 600s | 0.10 | 31 | 42% | +25.6% | 0.33 |
| 600s | 0.20 | 4 | 50% | +27.0% | 0.39 |
| 420s | 0.05 | 89 | 29% | +5.1% | 0.28 |
| 420s | 0.10 | 44 | 23% | +26.3% | 0.18 |
| 420s | 0.20 | 3 | 0% | -100.0% | 0.09 |
| 300s | 0.05 | 75 | 24% | -1.4% | 0.24 |
| 300s | 0.10 | 35 | 17% | -9.7% | 0.19 |
| 300s | 0.20 | 2 | 50% | +411.5% | 0.10 |
| 180s | 0.05 | 61 | 28% | +2.4% | 0.27 |
| 180s | 0.10 | 31 | 32% | +32.3% | 0.24 |
| 180s | 0.20 | 1 | 100% | +490.3% (exit 0)
```

## 2026-11-06 13:01:02 tasks/queue/074-send-cover-a.sh
```
(exit 0)
```

## 2026-11-06 13:52:02 tasks/queue/075-pihole-check.sh
```
== container
pihole Up 11 hours (healthy) 
== pi address
192.168.1.107 100.105.140.126 172.17.0.1 fd7a:115c:a1e0::2f4c:8c7f 
== normal lookup via pihole
tasks/queue/075-pihole-check.sh: line 6: dig: command not found
== ad domain via pihole (blocked answers 0.0.0.0 or ::)
tasks/queue/075-pihole-check.sh: line 7: dig: command not found
== same ad domain via 1.1.1.1 (real address)
tasks/queue/075-pihole-check.sh: line 8: dig: command not found
== pihole version
Core version is v6.5 (Latest: v6.5)
Web version is v6.6.1 (Latest: v6.6.1)
FTL version is v6.8 (Latest: v6.8)
== pihole status
  [✓] FTL is listening on port 53
     [✓] UDP (IPv4)
     [✓] TCP (IPv4)
     [✓] UDP (IPv6)
     [✓] TCP (IPv6)
== what the Pi itself uses for DNS

nameserver 100.100.100.100
nameserver fd7a:115c:a1e0::53
(exit 0)
```
