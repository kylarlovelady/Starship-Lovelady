#!/bin/bash
# Read-only diagnosis of the two free whale feeds: shows what they contain and how old it is.
cd ~/starship/markets && python3 - <<'PY'
import time, json, re, html, collector as c
now = int(time.time())
print("== Telegram Whale Alert page")
try:
    body = c.fetch("https://t.me/s/whale_alert_io", 10, c.BROWSER_UA)
    blks = body.split("tgme_widget_message_wrap")[1:]
    print("posts on page:", len(blks))
    shown = 0
    for b in blks[::-1]:
        m = re.search(r'<time[^>]*datetime="([^"]+)"', b)
        t = re.search(r'tgme_widget_message_text[^>]*>(.*?)</div>', b, re.S)
        if not (m and t): continue
        txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t.group(1))))
        age = (now - c.parsedate_iso(m.group(1))) / 60
        if "BTC" in txt and shown < 5:
            print("  %5.0f min ago | %s" % (age, txt[:140])); shown += 1
    if not shown: print("  no BTC posts on the page at all (page only holds the newest ~20 posts)")
    if blks:
        m = re.findall(r'<time[^>]*datetime="([^"]+)"', body)
        if m: print("newest post age: %.0f min" % ((now - c.parsedate_iso(m[-1])) / 60))
except Exception as e:
    print("FAILED:", e)
print("== Coinlobster giant trades")
try:
    d = json.loads(c.fetch("https://coinlobster.com/api/public/crypto-whales", 10, c.BROWSER_UA))
    w = d.get("whales", [])
    btc = [t for t in w if str(t.get("pair", "")).upper().startswith("BTC/")]
    print("trades in feed:", len(w), "| BTC pairs:", len(btc))
    ages = sorted((now - t.get("timestamp", 0) / 1000.0) / 60 for t in btc)
    if ages: print("BTC trade ages (min): newest %.0f, oldest %.0f" % (ages[0], ages[-1]))
    if w: print("newest any-pair age (min): %.0f" % min((now - t.get("timestamp", 0) / 1000.0) / 60 for t in w))
except Exception as e:
    print("FAILED:", e)
print("== What the signals say")
for name, fn in (("Whale transfers", c.sig_whales), ("Big exchange trades", c.sig_bigtrades)):
    try:
        s, d = fn(now); print("%s: %+.2f | %s" % (name, s, d))
    except Exception as e:
        print(name, "FAILED:", e)
PY
