"se": 0.0138, "rounds": 368, "rule": -0.0349, "hold": -0.0203}, {"peak": 20, "drop": 4, "gain": -0.0146, "se": 0.0124, "rounds": 368, "rule": -0.0349, "hold": -0.0203}, {"peak": 20, "drop": 2, "gain": -0.0148, "se": 0.0123, "rounds": 368, "rule": -0.0351, "hold": -0.0203}, {"peak": 20, "drop": 3, "gain": -0.0153, "se": 0.0124, "rounds": 368, "rule": -0.0357, "hold": -0.0203}], "note": "no take-profit rule beat holding by a clear margin yet; keeping the starting guess", "exits_checked": 30, "exit_vs_hold": 0.034}
== entry_stats.json
{"updated": 1793867284, "rounds": 238, "price": {"1-20": {"n": 742, "rounds": 166, "win": 0.09, "avg": -0.0068}, "20-35": {"n": 625, "rounds": 188, "win": 0.269, "avg": -0.0179}, "35-50": {"n": 747, "rounds": 171, "win": 0.431, "avg": -0.0109}, "50-60": {"n": 538, "rounds": 154, "win": 0.53, "avg": -0.0294}, "60-70": {"n": 469, "rounds": 170, "win": 0.635, "avg": -0.0254}, "70-80": {"n": 395, "rounds": 169, "win": 0.742, "avg": -0.0153}, "80-90": {"n": 353, "rounds": 158, "win": 0.822, "avg": -0.0292}, "90-100": {"n": 465, "rounds": 138, "win": 0.946, "avg": -0.0039}}, "hours": {"0": {"n": 106, "rounds": 12, "avg": 0.0233}, "1": {"n": 105, "rounds": 11, "avg": -0.1425}, "2": {"n": 70, "rounds": 8, "avg": 0.0457}, "3": {"n": 87, "rounds": 8, "avg": -0.0401}, "4": {"n": 119, "rounds": 8, "avg": -0.0665}, "5": {"n": 113, "rounds": 8, "avg": -0.0513}, "6": {"n": 94, "rounds": 8, "avg": -0.0212}, "7": {"n": 94, "rounds": 8, "avg": 0.0209}, "8": {"n": 87, "rounds": 7, "avg": -0.0399}, "9": {"n": 111, "rounds": 8, "avg": -0.0462}, "10": {"n": 95, "rounds": 8, "avg": 0.0081}, "11": {"n": 116, "rounds": 8, "avg": -0.0162}, "12": {"n": 67, "rounds": 7, "avg": 0.0019}, "13": {"n": 88, "rounds": 8, "avg": -0.0311}, "14": {"n": 77, "rounds": 8, "avg": 0.0149}, "15": {"n": 90, "rounds": 8, "av
== patterns.json
{"updated": 1793867373, "rounds": 196, "bad": [], "good": [], "note": null, "baseline": {"train": -0.0491, "test": -0.0439}}
== config (keys with plain values only)
{'threshold': 12.0, 'min_bet': 5.0, 'cap': 0, 'edge_min': 0.03, 'max_trades': 6.0, 'slice': 0.1, 'min_price': 0.08, 'max_price': 0.92, 'aggression': 50.0, 'floor': 0, 'entry_max': 0.8, 'entry_min': 0.15}
== real (live) order slippage notes, last 8
{"t": 1793679463, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV022330-30", "action": "buy", "side": "UP"}
{"t": 1793681642, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "buy", "side": "DOWN"}
{"t": 1793681702, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "sell", "side": "DOWN"}
{"t": 1793681918, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "buy", "side": "UP"}
{"t": 1793681966, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "buy", "side": "UP"}
{"t": 1793682188, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030015-15", "action": "buy", "side": "DOWN"}
{"t": 1793683870, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030045-45", "action": "buy", "side": "DOWN"}
{"t": 1793683924, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030045-45", "action": "sell", "side": "DOWN"}
(exit 0)
```

## 2026-11-05 02:34:01 tasks/queue/011-signals-and-stakes.sh
```
signals (n, right%, 95% range, verdict, weight):
  momentum       n=193  right= 57.0%  range 46.9-65.6  no clear edge      x1.16
  levels         n=159  right= 52.2%  range 42.4-63.0  no clear edge      x1.07
  trend_1h       n=108  right= 51.9%  range 40.3-62.0  no clear edge      x1.03
  funding        n=238  right= 51.3%  range 42.7-59.9  no clear edge      x1.03
  fng            n=215  right= 51.2%  range 41.7-60.5  no clear edge      x1.03
  trend_h        n=196  right= 51.0%  range 40.9-59.0  no clear edge      x1.00
  book           n=161  right= 50.3%  range 39.7-60.6  no clear edge      x1.00
  bigtrades      n=156  right= 48.1%  range 41.3-61.1  no clear edge      x1.03
  trend_w        n=189  right= 48.1%  range 38.5-57.2  no clear edge      x0.94
  news           n=202  right= 48.0%  range 38.0-56.7  no clear edge      x0.93
  trend_4h       n=98   right= 48.0%  range 35.1-58.0  no clear edge      x0.92
  trend_7d       n=94   right= 47.9%  range 36.3-59.0  no clear edge      x0.94
  trend_24h      n=110  right= 47.3%  range 37.0-58.2  no clear edge      x0.94
  whales         n=94   right= 41.5%  range 27.8-54.4  no clear edge      x0.80
other keys: ['time', 'scored', 'adopted', 'notes', 'weights']

'run' stakes by round, last 14 h (from sim_windows / trades):
no buy rows found with a cost field; first row keys:
['t', 'pnl', 'outcome', 'bal', 'src', 'hold', 'trades', 'moves', 'first', 'end', 'mix', 'sigs', 'p_open', 'staked', 'ticker', 'why', 'run', 'strat', 'hour']
(exit 0)
```

## 2026-11-05 02:37:01 tasks/queue/012-stakes.sh
```
rows: 137
Wed 20:00 staked $5.59 pnl -5.59 UP strat auto trades 1
Wed 20:15 staked $5.48 pnl 5.52 DOWN strat auto trades 1
Wed 20:30 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Wed 20:45 staked $5.48 pnl 5.52 DOWN strat auto trades 1
Wed 21:00 staked $5.59 pnl -5.59 UP strat auto trades 1
Wed 21:15 staked $0.0 pnl 0.0 UP strat auto trades 0
Wed 21:30 staked $49.68 pnl -26.39 UP strat auto trades 3
Wed 21:45 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Wed 22:00 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Wed 22:15 staked $48.22 pnl -18.9 UP strat auto trades 4
Wed 22:30 staked $0.0 pnl 0.0 UP strat auto trades 0
Wed 22:45 staked $49.75 pnl -28.52 DOWN strat auto trades 4
Wed 23:00 staked $36.63 pnl -15.53 DOWN strat auto trades 3
Wed 23:15 staked $48.26 pnl -24.68 DOWN strat auto trades 5
Wed 23:30 staked $49.83 pnl -19.09 UP strat auto trades 5
Wed 23:45 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Thu 00:00 staked $20.3 pnl -20.3 UP strat auto trades 1
Thu 00:15 staked $0.0 pnl 0.0 UP strat auto trades 0
Thu 00:30 staked $49.71 pnl 25.65 DOWN strat auto trades 3
Thu 00:45 staked $19.85 pnl 6.15 UP strat auto trades 1
Thu 01:00 staked $49.71 pnl 30.02 UP strat auto trades 5
Thu 01:15 staked $49.55 pnl 50.45 DOWN strat auto trades 2
Thu 01:30 staked $49.66 pnl 14.34 DOWN strat auto trades 2
Thu 01:45 staked $49.6 pnl -10.09 DOWN strat auto trades 6
max staked, last 14h: $49.83
(exit 0)
```

## 2026-11-05 02:40:01 tasks/queue/013-starship-url.sh
```
== routes/mounts in server.py
47:@app.get("/", response_class=HTMLResponse)
65:@app.post("/event/{name}")
75:@app.get("/mute")
79:@app.post("/mute/toggle")
89:app.include_router(router)
91:app.include_router(settings_router)
93:app.include_router(crop_router)
95:app.include_router(preview_router)
97:app.include_router(memory_router)
99:app.include_router(hub_router)
101:app.include_router(janitor_router)
103:app.include_router(mute_router)
105:app.include_router(network_router)
107:app.include_router(health_router)
109:app.include_router(layout_router)
== listeners
0.0.0.0:22
0.0.0.0:53
0.0.0.0:8089
0.0.0.0:8123
100.105.140.126:8090
100.105.140.126:8095
100.105.140.126:8097
100.105.140.126%tailscale0:41665
100.105.140.126%tailscale0:443
100.105.140.126%tailscale0:8081
127.0.0.1:10200
127.0.0.1:10300
127.0.0.1:10400
127.0.0.1:10700
127.0.0.1:18554
127.0.0.1:8080
127.0.0.1:8099
*:18555
[::]:22
[::]:53
[::]:8123
[fd7a:115c:a1e0::2f4c:8c7f]%tailscale0:38492
[fd7a:115c:a1e0::2f4c:8c7f]%tailscale0:443
[fd7a:115c:a1e0::2f4c:8c7f]%tailscale0:8081
== other http servers
kylarlo+ 1413028  0.1  1.1 207648 98240 ?        Ssl  Oct26  16:36 /home/kylarlovelady/kdp-studio/.venv/bin/python3 /home/kylarlovelady/kdp-studio/.venv/bin/uvicorn app:app --host 100.105.140.126 --po
kylarlo+ 2711573  0.0  0.2 328576 21488 ?        Ss   Oct30   0:36 /usr/bin/python3 -m http.server 8095 --bind 100.105.140.126 --directory /home/kylarlovelady/crew-web
== tailscale serve
https://loveladymainaihub.taild703ca.ts.net (tailnet only)
|-- / proxy http://127.0.0.1:8099

http://loveladymainaihub:8081 (tailnet only)
http://loveladymainaihub.taild703ca.ts.net:8081 (tailnet only)
|-- / proxy http://127.0.0.1:8080

(exit 0)
```

## 2026-11-05 02:49:01 tasks/queue/014-maker-study.sh
```
rounds used: 0 (from /home/kylarlovelady/market-data, last 3 days)

Reading it: the maker only helps if per-$ profit beats the taker's AFTER filling only on dips (adverse selection shows up as a lower win rate when filled). Fee for maker is assumed; confirm on a first real fill.
(exit 0)
```

## 2026-11-05 02:58:01 tasks/queue/015-hub-source.sh
```
== hub_api.py
import asyncio, json, os, subprocess, time, urllib.request
from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from settings_api import auth

router = APIRouter()
PAGE = Path(__file__).parent / "hub.html"
OUT = Path(os.environ.get("HUB_OUTAGE_DIR", "/var/lib/hub-outage"))
DEV = Path(os.environ.get("HUB_DEV_FILE", "/var/lib/hub-devices/known.json"))
MEM = Path(os.environ.get("HUB_MEM_FILE", "/home/kylarlovelady/homeassistant/memory/facts.md"))
SVC = [("hub-satellite", "Voice satellite"), ("hub-oled", "Small screen"), ("hub-lights", "Lights"),
       ("hub-dashboard", "Dashboard"), ("hub-watchdog", "Watchdog"), ("hub-devices", "Device alerts"),
       ("hub-outage", "Outage logger"), ("hub-memlog", "Conversation log")]

def jread(p, default):
    try:
        return json.loads(Path(p).read_text())
    except Exception:
        return default

def state(unit):
    try:
        return subprocess.run(["systemctl", "is-active", unit], capture_output=True, text=True, timeout=5).stdout.strip() or "unknown"
    except Exception:
        return "unknown"

def ha_up():
    try:
        urllib.request.urlopen("http://127.0.0.1:8123", timeout=3)
        return True
    except urllib.error.HTTPError:
        return True
    except Exception:
        return False

def collect():
    now = time.time()
    svcs = [{"name": n, "state": state(u)} for u, n in SVC]
    svcs.append({"name": "Home Assistant", "state": "active" if ha_up() else "down"})
    recs = []
    try:
        for line in (OUT / "outages.jsonl").read_text().splitlines():
            r = json.loads(line)
            if r["end"] >= now - 30 * 86400:
                recs.append(r)
    except Exception:
        pass
    st = jread(OUT / "state.json", {})
    outages = {"count": len(recs), "total": sum(r["secs"] for r in recs), "last": recs[-1] if recs else None,
               "since": st.get("since"), "watching": bool(st.get("beat")) and now - st["beat"] < 180}
    known = jread(DEV, {}); names = jread(PAGE.parent / "device-names.json", {})
    devs = sorted(({"ip": v.get("ip", ""), "name": names.get(mac) or v.get("name") or "", "vendor": v.get("vendor", ""),
                    "new": v.get("first_seen", 0) > now - 86400 and v.get("notified", False)} for mac, v in known.items()),
                  key=lambda d: [int(x) if x.isdigit() else 0 for x in d["ip"].split(".")])
    try:
        facts = sum(1 for l in MEM.read_text(encoding="utf-8").splitlines() if l.startswith("- "))
    except Exception:
        facts = None
    try:
        up = float(Path("/proc/uptime").read_text().split()[0])
    except Exception:
        up = None
    return {"services": svcs, "outages": outages, "devices": devs, "facts": facts, "uptime": up, "now": int(now)}

@router.get("/hub")
async def hub_page():
    return HTMLResponse(PAGE.read_text(encoding="utf-8"))

@router.get("/api/status")
async def status(request: Request):
    await auth(request)
    return await asyncio.to_thread(collect)
== hub.html (tabs and script, trimmed)
<!doctype html><html><head><meta charset="utf-8"><title>Hub</title>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Hub"><meta name="theme-color" content="#0b1220">
<style>
:root{color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:#0b1220;color:#e8f4ff;font:16px system-ui,sans-serif;display:flex;flex-direction:column;height:100vh;height:100dvh}
header{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 14px 6px}
header b{font-size:19px}
#pin{width:120px;background:#16233a;color:#fff;border:1px solid #2a3b57;border-radius:10px;padding:8px 10px;font-size:16px}
nav{display:flex;gap:6px;padding:4px 14px 10px;overflow-x:auto}
nav button,nav a{flex:none;background:#26354f;color:#e8f4ff;border:0;border-radius:12px;padding:9px 14px;font-size:15px;font-weight:600;text-decoration:none}
nav button.on{background:#1c6bff}
.pane{display:none;flex:1;min-height:0;width:100%;border:0;overflow:auto}
.pane.on{display:block}
#status{padding:0 14px 20px}
.card{background:#101b2e;border:1px solid #1d2a3d;border-radius:14px;padding:12px 14px;margin-bottom:12px}
.card h3{margin:0 0 8px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#7f93a8}
.row{display:flex;align-items:center;gap:8px;padding:4px 0;font-size:15px}
.dot{width:10px;height:10px;border-radius:50%;flex:none;background:#ff4d5e}
.dot.ok{background:#3dffa0}
.sub{color:#9fb0c3;font-size:14px}
.nw{background:#ffb02e;color:#201400;border-radius:6px;font-size:11px;font-weight:700;padding:1px 6px}
button.act{background:#1c6bff;color:#fff;border:0;border-radius:12px;padding:10px 14px;font-size:15px;font-weight:600;margin:4px 6px 0 0}
</style></head><body>
<header><b>Lovelady Hub</b><input id="pin" type="password" inputmode="numeric" placeholder="PIN"></header>
<nav><button data-t="status" class="on">Status</button><button data-t="look">Look</button><button data-t="memory">Memory</button><button data-t="janitor">Janitor</button><button data-t="network">Network</button><button data-t="layout">Layout</button><button data-t="crew">Control Room</button><button data-t="markets">Markets</button></nav>
<main id="status" class="pane on"><div class="card"><div class="sub" id="msg">Enter your PIN above.</div></div></main>
<iframe id="look" class="pane" data-src="/settings"></iframe>
<iframe id="memory" class="pane" data-src="/memory"></iframe>
<iframe id="janitor" class="pane" data-src="/janitor"></iframe><iframe id="network" class="pane" data-src="/network"></iframe><iframe id="layout" class="pane" data-src="/layout"></iframe><iframe id="crew" class="pane" data-src="http://loveladymainaihub.taild703ca.ts.net:8095/"></iframe><iframe id="markets" class="pane" data-src="http://loveladymainaihub.taild703ca.ts.net:8095/live.html"></iframe>
<scrip(exit 0)
```

## 2026-11-05 03:01:01 tasks/queue/016-merge-hub.sh
REFUSED: sudo is not allowed in queue scripts

## 2026-11-05 03:04:01 tasks/queue/017-merge-hub.sh
```
merged: True
data-t="overview" class="on">
(hub.html is read fresh on every request, no restart needed)
(exit 0)
```

## 2026-11-05 05:01:02 tasks/queue/018-starship-check.sh
```
== listener
LISTEN 0      5                             100.105.140.126:8095       0.0.0.0:*   
== server process
kylarlo+ 2711573  0.0  0.2 328576 21536 ?        Ss   Oct30   0:37 /usr/bin/python3 -m http.server 8095 --bind 100.105.140.126 --directory /home/kylarlovelady/crew-web
== files in crew-web
total 800
drwxr-xr-x  2 kylarlovelady kylarlovelady   4096 Nov  5 05:00 .
drwx------ 36 kylarlovelady kylarlovelady   4096 Nov  5 04:28 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady   3280 Nov  5 05:00 crew.json
-rw-rw-r--  1 kylarlovelady kylarlovelady     42 Nov  5 05:00 hub-alerts.json
-rw-rw-r--  1 kylarlovelady kylarlovelady   1022 Nov  5 05:00 hub-extra.json
-rw-r--r--  1 kylarlovelady kylarlovelady 147057 Nov  5 03:27 index.html
-rw-r--r--  1 kylarlovelady kylarlovelady 142042 Nov  4 15:13 index.html.bak
-rw-rw-r--  1 kylarlovelady kylarlovelady  49563 Nov  5 05:00 live.html
-rw-r--r--  1 kylarlovelady kylarlovelady 189303 Nov  5 05:00 market.json
-rw-rw-r--  1 kylarlovelady kylarlovelady  14611 Nov  5 05:00 markets.html
-rw-rw-r--  1 kylarlovelady kylarlovelady  11664 Nov  5 05:00 report.html
-rw-r--r--  1 kylarlovelady kylarlovelady  38121 Nov  5 04:59 report.json
lrwxrwxrwx  1 kylarlovelady kylarlovelady     43 Oct 30 14:17 status.json -> /home/kylarlovelady/crew-status/status.json
-rw-r--r--  1 kylarlovelady kylarlovelady 188749 Nov  5 03:27 support.js
== fetch
index 200 147057b
crew.json 200
== index.html matches repo?
same
== crew-update log
(exit 0)
```

## 2026-11-05 12:40:02 tasks/queue/019-kalshi-full.sh
```
=== maker study (3 days)
rounds used: 69 (from /home/kylarlovelady/market-data, last 3 days)

entry at about 1 min in: 138 orders per method
  TAKER  profit per contract -0.022  per $ staked -4.1%   (win rate 50%)
  MAKER  filled 128 of 138 (93%); avg price 1.0 cents better than the ask; win rate when filled 52% (taker on the same orders 52%)
         profit per FILLED contract +0.017 (assumed 1.75% fee) / +0.021 (0 fee);  taker on those same orders -0.006
         per $ staked: maker +3.4% vs taker -4.1%;  per ATTEMPT (unfilled = 0): maker +0.016 vs taker -0.022

entry at about 2 min in: 138 orders per method
  TAKER  profit per contract -0.021  per $ staked -4.0%   (win rate 50%)
  MAKER  filled 128 of 138 (93%); avg price 1.0 cents better than the ask; win rate when filled 49% (taker on the same orders 49%)
         profit per FILLED contract -0.001 (assumed 1.75% fee) / +0.003 (0 fee);  taker on those same orders -0.023
         per $ staked: maker -0.3% vs taker -4.0%;  per ATTEMPT (unfilled = 0): maker -0.001 vs taker -0.021

entry at about 3 min in: 138 orders per method
  TAKER  profit per contract -0.020  per $ staked -3.9%   (win rate 50%)
  MAKER  filled 125 of 138 (91%); avg price 1.0 cents better than the ask; win rate when filled 50% (taker on the same orders 50%)
         profit per FILLED contract -0.004 (assumed 1.75% fee) / -0.000 (0 fee);  taker on those same orders -0.026
         per $ staked: maker -0.8% vs taker -3.9%;  per ATTEMPT (unfilled = 0): maker -0.004 vs taker -0.020

Reading it: the maker only helps if per-$ profit beats the taker's AFTER filling only on dips (adverse selection shows up as a lower win rate when filled). Fee for maker is assumed; confirm on a first real fill.

=== review 24h (tail)
TRADE REVIEW, last 24 hours: 2363 (strategy, round) results from 65 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_hold          54    +990.35   70%  +63.3%
  v_cut_loose     54    +577.86   61%  +26.9%
  v_late          35    +571.24   60%  +33.6%
  v_x96220861     28    +561.71   68%  +31.3%
  v_x88221261     25    +508.59   60%  +41.9%
  v_flow_flip     60    +458.14   48%   +9.6%
  v_no_cut        54    +399.06   67%  +25.4%
  v_x60222031     27    +397.62   67%  +31.2%
  v_x64216771     50    +388.75   56%   +9.8%
  v_x16217721     38    +361.06   42%  +11.2%
  v_x32221881     28    +357.28   57%  +12.7%
  mood            58    +354.37   50%  +14.5%
  v_x52220781     25    +266.30   52%  +21.8%
  v_x219211       47    +233.55   45%   +9.2%
  v_x72222451     44    +224.51   45%   +9.5%
  v_one_shot      54    +203.17   70%  +46.6%
  v_x28219981     52    +201.35   52%   +4.9%
  v_x80218931     40    +195.57   45%   +9.0%
  swing           65    +176.90   43%   +5.2%
  v_x80218932     40    +158.30   62%  +21.7%
  flow            57    +148.58   49%  +10.0%
  v_x28219982     52    +144.01   52%   +7.5%
  v_x219212       47    +141.38   47%   +3.8%
  v_x96220872     28    +128.96   39%   +8.9%
  v_x36215122     26    +125.39   50%  +12.0%
  v_x32221882     28    +122.96   54%   +5.1%
  v_x52220782     24    +110.21   42%   +9.5%
  v_x64216772     50    +108.55   64%  +17.3%
  v_x36215121     45    +106.19   42%   +4.6%
  signals         55    +102.32   51%   +5.6%
  v_x24220781     31    +101.88   61%  +17.5%
  v_x60222032     28     +92.04   71%  +29.8%
  hold            65     +83.95   57%  +11.5%
  v_x68220542     25     +81.14   48%   +8.3%
  v_x76218991     15     +74.22   60%  +26.3%
  v_x76218992     15     +74.22   60%  +26.3%
  v_x40223631     19     +55.28   58%  +22.5%
  v_x68220541     25     +54.52   48%   +2.6%
  v_x44219232     43     +47.69   44%   +1.4%
  trend           57     +35.07   44%   +2.8%
  v_adds          54     +29.39   50%   +1.9%
  distance        54     +10.12   54%   +1.1%
  v_x8220762      43      -6.37   47%   -0.3%
  v_x12229262     12     -15.60   42%   -3.6%
  v_x40223632     20     -22.69   35%   -6.2%
  v_x44219231     43     -38.94   40%   -1.2%
  v_x8220761      44     -47.37   43%   -1.3%
  v_mood_flip     60     -54.37   52%   -1.4%
  v_x72222452     44     -57.10   39%   -1.7%
  v_x12229261     12     -70.61   33%  -16.3%
  v_x88221262     34     -95.57   41%   -3.7%
  v_cut_tight     54     -95.89   41%   -8.1%
  v_x16217722     39    -103.03   38%   -6.7%
  v_x24220782     31    -142.99   35%   -6.0%
  v_trail         54    -148.31   48%  -10.6%
  v_trail_wide    54    -148.31   48%  -10.6%
  v_x4227191      22    -202.60   32%  -11.5%
  v_x4227192      22    -204.69   32%  -10.5%
  run             54    -291.88   46%  -12.8%

=== 'run': 54 rounds. Total profit -291.88 ===
1) SIDE: first bet on the winning side in 33 of 54 rounds (61%). Money-weighted: 52% of dollars staked were on the winning side (coin flip = 50%).
2) TIMING: it makes its first bet a median 1:32 into the round. The cheapest price on the winning side came a median 3:58 in. Median paid 21 cents above that cheapest point when it was on the right side.
   first bet time -> rounds, profit, side right:  0-1 min: 24, -214, 14 right  |  1-3 min: 17, -14, 13 right  |  10+ min: 2, -17, 1 right  |  3-6 min: 6, -32, 2 right  |  6-10 min: 5, -16, 3 right
3) SELLING (money made or lost by selling versus just holding those contracts to the end):
   cut a loss                  15 sells    -325.01  selling HURT (holding would have been better)
   other                        1 sells      +6.75  selling HELPED
   its own odds said sell      28 sells     +33.85  selling HELPED
4) BET SIZE -> rounds, profit, wins:  $100-250: 6, -167, 1  |  $25-100: 23, -161, 8  |  under $25: 25, +36, 16
5) HOUR OF DAY -> rounds, profit:  00h: 3, +11  |  01h: 4, +85  |  04h: 2, -1  |  05h: 4, +17  |  06h: 2, -10  |  07h: 4, -68  |  08h: 2, -8  |  09h: 4, -77  |  10h: 4, -26  |  11h: 2, -73  |  12h: 3, -28  |  13h: 3, +19  |  14h: 2, -23  |  15h: 3, -3  |  16h: 2, +1  |  17h: 1, -6  |  20h: 3, +5  |  21h: 2, -32  |  22h(exit 0)
```

## 2026-11-05 12:43:01 tasks/queue/020-kalshi-more.sh
```
=== key strategies, last 72 h
  v_hold          95    +296.88   60%   +8.5%
  v_late          60    +125.62   48%   +2.9%
  v_one_shot      95     -58.77   60%   -5.7%
  v_cut_loose     95     -83.26   52%   -1.8%
  v_no_cut        95    -269.14   57%   -6.5%
  hold           188    -274.35   51%   -5.3%
  v_adds          95    -483.14   43%   -9.1%
  v_trail         95    -535.18   42%  -11.5%
  v_cut_tight     95    -562.70   35%  -14.3%
  swing          186    -767.42   34%   -7.5%
  signals        162    -798.12   44%   -7.3%
  distance       148   -1125.74   45%   -9.6%
  flow           156   -1151.33   39%   -8.0%
  trend          169   -1250.37   34%   -8.1%
  run            158   -1748.43   39%  -15.6%
  mood           159   -1825.53   42%  -18.1%
=== key strategies, last 12 h
  v_hold          32    +738.53   78%  +82.7%
  v_late          25    +505.31   56%  +42.0%
  mood            33    +419.86   58%  +31.5%
  v_cut_loose     32    +399.14   62%  +27.8%
  v_no_cut        32    +274.79   69%  +27.1%
  swing           34    +248.03   47%  +13.8%
  trend           33    +146.83   58%  +22.6%
  v_adds          32    +143.80   56%  +15.9%
  flow            33    +139.75   55%  +16.6%
  v_one_shot      32    +124.47   78%  +51.1%
  distance        32     +79.12   62%  +15.7%
  hold            34     +77.25   68%  +18.7%
  signals         32     +48.60   59%   +4.7%
  v_cut_tight     32      +5.29   50%   +0.8%
  v_trail         32     -30.53   56%   -4.4%
  run             31    -186.85   52%  -10.0%

=== run, recent rounds (is the cap working?)
{'strategy': 'auto', 'bal': 827.72, 'pnl': -172.28, 'windows': 42, 'active': None, 'live': False}
Thu 09:00 {'staked': 49.24, 'pnl': 15.76}
Thu 09:15 {'staked': 49.8, 'pnl': -29.65}
Thu 09:30 {'staked': 50.0, 'pnl': -27.79}
Thu 09:45 {'staked': 49.96, 'pnl': -34.89}
Thu 10:00 {'staked': 49.95, 'pnl': -37.19}
Thu 10:15 {'staked': 20.48, 'pnl': 21.52}
Thu 10:30 {'staked': 49.93, 'pnl': -32.33}
Thu 10:45 {'staked': 49.64, 'pnl': 22.02}
Thu 11:00 {'staked': 0.0, 'pnl': 0.0}
Thu 11:15 {'staked': 49.96, 'pnl': -41.19}
Thu 11:30 {'staked': 49.9, 'pnl': -31.85}
Thu 11:45 {'staked': 0.0, 'pnl': 0.0}
Thu 12:00 {'staked': 49.77, 'pnl': -22.12}
Thu 12:15 {'staked': 20.73, 'pnl': -11.13}

=== collector restart / version
ActiveEnterTimestamp=Mon 2026-11-02 22:27:17 CST
# v8.2 restart: cap 25, Auto wallet needs 40+ rounds and a positive record (else holds to the end); nothing is retired (

=== real live orders
61 rows; keys: ['action', 'book_side', 'count', 'price', 'reply', 'side', 'status', 't', 'ticker']
{('buy', 'UP'): 22, ('sell', 'UP'): 27, ('buy', 'DOWN'): 7, ('sell', 'DOWN'): 5}
{"t": 1793652359, "action": "buy", "side": "UP", "ticker": "KXBTC15M-26NOV021600-00", "book_side": "bid", "count": 1, "price": 0.55, "status": 201, "reply": {"average_fee_paid": "0.0174", "average_fill_price": "0.5400", "client_order_id": "1ab386c5-dfb6-42c2-a759-a0b764994f79", "fill_count": "1.00", "order_id": "01a19e02-ff58-7c
{"t": 1793652361, "action": "sell", "side": "UP", "ticker": "KXBTC15M-26NOV021600-00", "book_side": "ask", "count": 1, "price": 0.54, "status": 201, "reply": {"average_fee_paid": "0.0174", "average_fill_price": "0.5500", "client_order_id": "d174effe-9f14-4d4e-87ef-78e666d416c1", "fill_count": "1.00", "order_id": "01a19e03-0728-7
{"t": 1793683924, "kind": "order", "action": "sell", "side": "DOWN", "ticker": "KXBTC15M-26NOV030045-45", "book_side": "bid", "count": 18, "price": 0.38, "quote_ask": 0.35, "quote_bid": 0.34, "status": 201, "reply": {"average_fee_paid": "0.0159", "average_fill_price": "0.3500", "client_order_id": "3036302b-8f89-4e26-b607-b0c9294
{"t": 1793683924, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030045-45", "action": "sell", "side": "DOWN"}

=== my real trades
fills downloaded: 439
fills that were YOUR own: 429, fills from the agent's live sessions: 10
rounds traded: 107   won: 49 (46%)   total after fees: -2201.25   fees: 423.82
avg stake per round: $106.34   avg win: +93.25   avg loss: -116.73
first buy in the first 2 minutes: 70 of 107 rounds   avg first buy 145s into the round
avg buy price: 47 cents
took profit early (sold before close): 38 rounds, avg -47.90, won 61%
held to the end: 69 rounds, avg -5.52, won 38%
avg time of first sale: 387s into the round
date range: 10-31 00:30 to 11-05 01:00
sold early at a profit: 23 rounds, avg +100.21   sold early at a loss (cut loser): 15 rounds, avg -275.00
stake under $10  14 rounds  won  50%  total    +26.00
stake $10-50     53 rounds  won  42%  total   -343.91
stake $50-150    21 rounds  won  52%  total   -179.99
stake over $150  19 rounds  won  47%  total  -1703.35
first buy first minute   55 rounds  won  51%  total  -1736.64
first buy minutes 2-3    21 rounds  won  29%  total   -687.50
first buy after minute 3 29 rounds  won  45%  total   +213.53
last 5 rounds:
  11-04 23:45  yes  staked 48.4    pnl  -50.00 (held)
  11-05 00:00  yes  staked 96.29   pnl +131.41 (sold early)
  11-05 00:15  no   staked 47.47   pnl  -50.00 (held)
  11-05 00:30  no   staked 19.4    pnl  +25.20 (sold early)
  11-05 01:00  no   staked 18.95   pnl  -20.00 (held)
THE AGENT'S live rounds (not yours): 4 rounds, -2.58 after fees
saved to ~/market-data/my_trades.json
(exit 0)
```

## 2026-11-05 12:49:01 tasks/queue/021-kalshi-state.sh
```
== collector process
 710034 Mon Nov  2 22:27:17 2026 /usr/bin/python3 /home/kylarlovelady/starship/markets/collector.py
== repo head on Pi
367c7df 3 minutes ago queue 021: is the new Kalshi code running
== config files (numbers only)
-- config.json
{'weights': {'book': 0.25, 'momentum': 0.2, 'whales': 0.2, 'bigtrades': 0.15, 'news': 0.1, 'fng': 0.05, 'funding': 0.05}, 'threshold': 12.0, 'min_bet': 5.0, 'cap': 0, 'edge_min': 0.03, 'max_trades': 6.0, 'slice': 0.1, 'min_price': 0.08, 'max_price': 0.92, 'aggression': 50.0, 'floor': 0, 'entry_max': 0.8, 'entry_min': 0.15}
== auto log and pick
auto_pick: None
cap shown: None None None
run keys: ['added', 'autolog', 'bal', 'curve', 'equity', 'events', 'halt', 'id', 'in_round', 'inflight', 'k_age', 'label', 'live', 'now', 'pnl', 'pos', 'refills', 'round_cash', 'rounds', 'slip_avg', 'start', 'started', 'status', 'stopped', 'strategy', 'trades', 'using', 'warn', 'windows', 'wins']
(exit 0)
```

## 2026-11-05 12:52:01 tasks/queue/022-run-state.sh
```
strategy: auto | using: v_x88221261 | status: running | halt: None
autolog {'t': 1793892614, 'from': 'v_x8220761', 'to': 'v_x44219232', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793893513, 'from': 'v_x44219232', 'to': 'v_x72222451', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793894413, 'from': 'v_x72222451', 'to': 'v_x44219232', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793895312, 'from': 'v_x44219232', 'to': 'v_x64216771', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793899823, 'from': 'v_x64216771', 'to': 'v_x52220781', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793902514, 'from': 'v_x52220781', 'to': 'v_x88221261', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
cap in config shown: None
11:15 49.96 -41.19
11:30 49.9 -31.85
11:45 0.0 0.0
12:00 49.77 -22.12
12:15 20.73 -11.13
12:30 49.83 -14.72
Mon Nov  2 22:27:17 2026 /usr/bin/python3 /home/kylarlovelady/starship/markets/collector.py
(exit 0)
```
