rice 14c at 14:05
  Thu 00:00  -21  bet DOWN at 0:15 @48c ($26) (WRONG SIDE); result UP. best swing UP bought at 6:20 sold at 13:50, +62c/contract;  cheapest winning-side price 36c at 6:20
  Wed 23:30  -19  bet DOWN at 3:20 @47c ($47) (WRONG SIDE); result UP. best swing DOWN bought at 10:28 sold at 14:00, +72c/contract;  cheapest winning-side price 23c at 14:00
  Wed 22:15  -19  bet UP at 1:32 @48c ($46); result UP. best swing UP bought at 4:40 sold at 14:21, +78c/contract;  cheapest winning-side price 21c at 4:40

BEST 3 ROUNDS:
  Thu 01:15  +50  bet DOWN at 2:01 @49c ($47); result DOWN
  Thu 01:00  +30  bet UP at 0:57 @44c ($96); result UP
  Thu 00:30  +26  bet DOWN at 0:26 @48c ($48); result DOWN
(exit 0)
```

## 2026-11-05 02:31:17 tasks/queue/009-review-24.sh
```
TRADE REVIEW, last 24 hours: 1282 (strategy, round) results from 71 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_x8220761      15    +253.71   67%  +21.3%
  v_x44219232     14    +239.11   64%  +25.9%
  v_x219212       18    +176.34   56%  +14.0%
  v_x44219231     14    +174.29   57%  +18.9%
  v_x72222452     15    +156.13   53%  +15.3%
  v_x88221262      5    +117.66  100%  +63.8%
  v_x28219981     23     +88.49   52%   +5.5%
  v_x80218932     11     +82.77   73%  +44.0%
  v_cut_loose     53     +81.47   51%   +4.4%
  v_hold          53     +66.51   55%   +4.4%
  v_x16217722     10     +63.24   60%  +17.9%
  v_x24220782      2     +55.99  100%  +82.5%
  v_x64216771     21     +55.33   52%   +3.8%
  v_x28219982     23     +32.07   48%   +3.5%
  v_x24220781      2     +26.35  100%  +66.6%
  v_x36215122      7      +4.71   43%   +2.0%
  v_x88221261      2      +3.16  100%  +29.9%
  v_x64216772     21      -5.01   52%   -1.7%
  distance        53     -18.88   43%   -1.6%
  v_no_cut        53     -19.13   55%   -1.2%
  v_x8220762      15     -37.95   47%   -6.7%
  v_x52220782      2     -42.40    0%  -42.4%
  v_x52220781      3     -48.97   33%  -48.5%
  v_x16217721     10     -71.41   40%  -10.7%
  v_trail         53     -98.51   38%   -3.8%
  v_trail_wide    53     -98.51   38%   -3.8%
  v_x219211       18    -126.84   28%  -15.5%
  v_one_shot      52    -135.62   54%  -19.8%
  v_x72222451     15    -135.88   27%  -20.8%
  flow            56    -155.11   36%  -11.5%
  v_x36215121     16    -155.78   25%  -22.2%
  v_x80218931     11    -164.82   18%  -35.8%
  v_late          30    -165.74   47%  -10.8%
  signals         57    -194.59   33%   -9.4%
  v_cut_tight     53    -261.88   28%  -13.2%
  v_adds          53    -326.58   38%  -11.9%
  trend           60    -362.62   28%  -16.3%
  v_mood_flip     30    -365.94   40%  -15.5%
  run             54    -392.53   43%  -34.2%
  v_flow_flip     30    -394.45   30%  -15.5%
  hold            70    -536.47   37%  -47.9%
  swing           71    -584.03   31%  -16.3%
  mood            55    -599.92   35%  -17.7%

=== 'run': 54 rounds. Total profit -392.53 ===
1) SIDE: first bet on the winning side in 24 of 54 rounds (44%). Money-weighted: 38% of dollars staked were on the winning side (coin flip = 50%).
2) TIMING: it makes its first bet a median 2:08 into the round. The cheapest price on the winning side came a median 4:44 in. Median paid 15 cents above that cheapest point when it was on the right side.
   first bet time -> rounds, profit, side right:  0-1 min: 14, -48, 8 right  |  1-3 min: 18, -44, 8 right  |  10+ min: 4, -127, 1 right  |  3-6 min: 12, -120, 5 right  |  6-10 min: 6, -54, 2 right
3) SELLING (money made or lost by selling versus just holding those contracts to the end):
   its own odds said sell       3 sells     -52.59  selling HURT (holding would have been better)
   cut a loss                   5 sells     -12.97  selling HURT (holding would have been better)
   other                        1 sells      +6.75  selling HELPED
4) BET SIZE -> rounds, profit, wins:  $25-100: 19, -389, 5  |  under $25: 35, -4, 18
5) HOUR OF DAY -> rounds, profit:  00h: 3, +11  |  01h: 3, +95  |  03h: 2, -11  |  04h: 4, -29  |  05h: 4, -64  |  06h: 2, -58  |  07h: 2, -41  |  08h: 3, -182  |  09h: 3, -5  |  10h: 3, +5  |  11h: 3, +12  |  12h: 2, -10  |  13h: 3, +19  |  14h: 2, -23  |  15h: 3, -3  |  16h: 2, +1  |  17h: 1, -6  |  20h: 3, +5  |  21h: 2, -32  |  22h: 1, -19  |  23h: 3, -59
6) HINDSIGHT: buying the winning side at its cheapest moment and holding earns an average 69 cents per contract after fees; the best swing (buy low, sell high, any side) averages 68 cents per contract. It is not achievable (nobody knows the cheapest moment); it shows how much room there is.

WORST 5 ROUNDS (when, what it did, what was best):
  Wed 08:45  -84  bet UP at 0:43 @37c ($80) (WRONG SIDE); result DOWN. best swing DOWN bought at 4:50 sold at 12:27, +67c/contract;  cheapest winning-side price 31c at 4:50
  Wed 08:15  -64  bet UP at 10:14 @46c ($61) (WRONG SIDE); result DOWN. best swing DOWN bought at 11:41 sold at 14:27, +92c/contract;  cheapest winning-side price 7c at 11:41
  Wed 06:45  -63  bet DOWN at 13:05 @49c ($60) (WRONG SIDE); result UP. best swing UP bought at 9:42 sold at 14:31, +95c/contract;  cheapest winning-side price 4c at 9:42
  Wed 05:30  -56  bet UP at 3:14 @49c ($53) (WRONG SIDE); result DOWN. best swing DOWN bought at 7:58 sold at 14:54, +67c/contract;  cheapest winning-side price 31c at 7:58
  Wed 07:45  -46  bet UP at 3:02 @49c ($44) (WRONG SIDE); result DOWN. best swing DOWN bought at 11:46 sold at 14:09, +67c/contract;  cheapest winning-side price 31c at 11:46

BEST 3 ROUNDS:
  Thu 01:15  +50  bet DOWN at 2:01 @49c ($47); result DOWN
  Thu 01:00  +30  bet UP at 0:57 @44c ($96); result UP
  Wed 05:15  +27  bet UP at 6:46 @48c ($25); result UP
(exit 0)
```

## 2026-11-05 02:31:32 tasks/queue/010-learn-files.sh
```
== learn_report.json
{"time": 1793864719, "scored": 238, "adopted": false, "signals": {"book": {"n": 161, "right": 81, "pct": 50.3, "low": 39.7, "high": 60.6, "verdict": "no clear edge", "mult": 1.0, "trust": 50.1, "n_eff": 83.5}, "momentum": {"n": 193, "right": 110, "pct": 57.0, "low": 46.9, "high": 65.6, "verdict": "no clear edge", "mult": 1.16, "trust": 55.4, "n_eff": 103.7}, "whales": {"n": 94, "right": 39, "pct": 41.5, "low": 27.8, "high": 54.4, "verdict": "no clear edge", "mult": 0.8, "trust": 43.2, "n_eff": 48.6}, "bigtrades": {"n": 156, "right": 75, "pct": 48.1, "low": 41.3, "high": 61.1, "verdict": "no clear edge", "mult": 1.03, "trust": 51.0, "n_eff": 94.6}, "news": {"n": 202, "right": 97, "pct": 48.0, "low": 38.0, "high": 56.7, "verdict": "no clear edge", "mult": 0.93, "trust": 47.7, "n_eff": 105.2}, "fng": {"n": 215, "right": 110, "pct": 51.2, "low": 41.7, "high": 60.5, "verdict": "no clear edge", "mult": 1.03, "trust": 51.0, "n_eff": 104.4}, "funding": {"n": 238, "right": 122, "pct": 51.3, "low": 42.7, "high": 59.9, "verdict": "no clear edge", "mult": 1.03, "trust": 51.2, "n_eff": 126.0}, "trend_h": {"n": 196, "right": 100, "pct": 51.0, "low": 40.9, "high": 59.0, "verdict": "no clear edge", "mult": 1.0, "trust": 50.0, "n_eff": 114.2}, "trend_w": {"n": 189, "right": 91, "pct": 48.1, "low"
== exit_rules.json
{"updated": 1793867339, "rounds": 190, "source": "default", "peak": 8, "drop": 4, "enabled": false, "audit": "switched off: over 190 rounds every tested take-profit rule did worse than holding", "table": [{"peak": 20, "drop": 8, "gain": -0.0087, "se": 0.0119, "rounds": 368, "rule": -0.0291, "hold": -0.0203}, {"peak": 20, "drop": 6, "gain": -0.011, "se": 0.012, "rounds": 368, "rule": -0.0314, "hold": -0.0203}, {"peak": 15, "drop": 8, "gain": -0.0146, "se": 0.0138, "rounds": 368, "rule": -0.0349, "hold": -0.0203}, {"peak": 20, "drop": 4, "gain": -0.0146, "se": 0.0124, "rounds": 368, "rule": -0.0349, "hold": -0.0203}, {"peak": 20, "drop": 2, "gain": -0.0148, "se": 0.0123, "rounds": 368, "rule": -0.0351, "hold": -0.0203}, {"peak": 20, "drop": 3, "gain": -0.0153, "se": 0.0124, "rounds": 368, "rule": -0.0357, "hold": -0.0203}], "note": "no take-profit rule beat holding by a clear margin yet; keeping the starting guess", "exits_checked": 30, "exit_vs_hold": 0.034}
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
