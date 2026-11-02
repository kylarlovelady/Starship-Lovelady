#!/bin/bash
# Read-only probe: checks which FREE sources show big Bitcoin transfers WITH direction (to/from exchanges).
python3 - <<'PY'
import re, urllib.request, json
H = {"User-Agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 Chrome/120 Safari/537.36", "Accept": "*/*"}
def get(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=20)
        return r.status, r.read().decode("utf-8", "replace")
    except Exception as e:
        return getattr(e, "code", 0), str(e)[:120]
srcs = [
 ("Telegram public page of Whale Alert", "https://t.me/s/whale_alert_io"),
 ("Swiss Whale dashboard (BTC netflow)", "https://swisswhaleintelligence.com/dashboard/btc"),
 ("Coinlobster free whale trades", "https://coinlobster.com/api/public/crypto-whales"),
 ("Coinlobster free whale radar", "https://coinlobster.com/api/public/whale-radar"),
 ("mempool.space newest pending", "https://mempool.space/api/mempool/recent"),
 ("blockchain.info pending list", "https://blockchain.info/unconfirmed-transactions?format=json"),
]
for name, u in srcs:
    code, body = get(u)
    print("\n==", name, "->", code, "| %d chars" % len(body))
    if code == 200:
        if "t.me" in u:
            msgs = re.findall(r'tgme_widget_message_text[^>]*>(.*?)</div>', body, re.S)
            for m in msgs[-4:]:
                print("  *", re.sub(r"<[^>]+>", "", m).strip()[:160])
        elif "swiss" in u:
            for m in re.findall(r"[^.]{0,60}(?:inflow|outflow|netflow)[^.]{0,80}", body, re.I)[:5]:
                print("  *", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m)).strip()[:150])
            print("  api paths found:", sorted(set(re.findall(r'["\'](/api/[A-Za-z0-9_/\-]+)', body)))[:12])
        else:
            print(" ", body[:500].replace("\n", " "))
    else:
        print(" ", body[:150])
PY
