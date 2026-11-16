#!/usr/bin/env python3
"""NEWS LOG (Kylar's first request for the Kalshi agent, built 2026-11-16). Saves every headline from free feeds with timestamps, a category, a simple
Bitcoin good/bad score and topic tags, so we can later test "does bad tech/financial news move Bitcoin?" on stored history.
Read-only on the web, writes only ~/market-data/news.jsonl. No keys needed.
  python3 news_log.py once      fetch all feeds, append new headlines (cron runs this every few minutes)
  python3 news_log.py probe     show which feeds work from this machine and how fresh they are
  python3 news_log.py report    counts by day and category, the worst/best news days"""
import json, os, re, sys, time, hashlib, urllib.request, xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
OUT = os.path.join(D, "news.jsonl")
GN = "https://news.google.com/rss/search?hl=en-US&gl=US&ceid=US:en&q="
SOURCES = [  # (name, category, url)
    ("coindesk", "crypto", "https://www.coindesk.com/arc/outboundfeeds/rss/"), ("cointelegraph", "crypto", "https://cointelegraph.com/rss"),
    ("decrypt", "crypto", "https://decrypt.co/feed"), ("bitcoinmagazine", "crypto", "https://bitcoinmagazine.com/.rss/full/"),
    ("cryptoslate", "crypto", "https://cryptoslate.com/feed/"), ("bitcoinist", "crypto", "https://bitcoinist.com/feed/"),
    ("gnews-bitcoin", "crypto", GN + "bitcoin+when:1d"),
    ("cnbc-top", "finance", "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114"),
    ("cnbc-markets", "finance", "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839069"),
    ("marketwatch", "finance", "https://feeds.content.dowjones.io/public/rss/mw_topstories"), ("yahoo-finance", "finance", "https://finance.yahoo.com/rss/topstories"),
    ("fed", "finance", "https://www.federalreserve.gov/feeds/press_all.xml"), ("gnews-fed-rates", "finance", GN + "federal+reserve+OR+inflation+OR+tariffs+when:1d"),
    ("theverge", "tech", "https://www.theverge.com/rss/index.xml"), ("techcrunch", "tech", "https://techcrunch.com/feed/"),
    ("arstechnica", "tech", "https://feeds.arstechnica.com/arstechnica/index"), ("hackernews", "tech", "https://hnrss.org/frontpage"),
    ("bleepingcomputer", "tech", "https://www.bleepingcomputer.com/feed/"),
    ("gnews-outage", "tech", GN + "(outage+OR+cyberattack+OR+hack+OR+breach)+(Microsoft+OR+Google+OR+Amazon+OR+airlines+OR+bank)+when:1d"),
    ("bbc-world", "general", "https://feeds.bbci.co.uk/news/world/rss.xml"), ("bbc-business", "general", "https://feeds.bbci.co.uk/news/business/rss.xml"),
    ("npr", "general", "https://feeds.npr.org/1001/rss.xml"), ("gnews-breaking", "general", GN + "breaking+news+when:1d")]
BULL = ["surge", "rally", "soar", "jump", "record high", "all-time high", "approv", "inflow", "adoption", "accumulat", "bullish", "breakout", "gains", "rises", "climb", "upgrade", "partnership", "rebound", "recover", "rate cut", "cuts rates", "etf", "stimulus", "ceasefire", "deal reached"]
BEAR = ["crash", "plunge", "drop", "falls", "slump", "hack", "exploit", "ban", "lawsuit", "sues", "outflow", "sell-off", "selloff", "liquidat", "bearish", "fear", "dump", "warning", "probe", "fraud", "arrest", "bankrupt", "tumble", "sinks", "rejects", "delay",
        "outage", "cyberattack", "cyber attack", "breach", "ransomware", "grounded", "ground stop", "layoff", "recession", "tariff", "default", "shutdown", "war ", "attack", "rate hike", "downturn", "meltdown", "panic"]
TAGS = {"outage": r"outage|went down|ground stop|grounded|service disruption", "cyber": r"cyberattack|cyber attack|hack|breach|ransomware|exploit", "bigtech": r"microsoft|google|alphabet|amazon|apple|nvidia|meta |tesla|crowdstrike",
        "airlines": r"airline|airport|flights", "fed": r"federal reserve|\bfed\b|powell|fomc|rate cut|rate hike|interest rate", "inflation": r"inflation|cpi|jobs report|payrolls|unemployment", "tariff": r"tariff|trade war|sanction",
        "etf": r"\betf\b", "regulation": r"sec |cftc|regulat|lawsuit|ban ", "bitcoin": r"bitcoin|\bbtc\b", "war": r"\bwar\b|missile|invasion|strike on", "bank": r"\bbank\b|banking|bank run", "stocks": r"stocks|s&p|nasdaq|dow "}

def fetch(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; starship-news-log/1.0)"})
    with urllib.request.urlopen(req, timeout=timeout) as r: return r.read()

def parse_ts(s):
    if not s: return None
    try: return parsedate_to_datetime(s).timestamp()
    except Exception: pass
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if dt.tzinfo is None: dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except Exception: return None

def read(url):
    root = ET.fromstring(fetch(url)); out = []
    for it in list(root.iter("item")) + [e for e in root.iter() if e.tag.endswith("}entry")]:
        def g(*names):
            for ch in it:
                if ch.tag.split("}")[-1] in names and (ch.text or "").strip(): return ch.text.strip()
        title = re.sub(r"\s+", " ", g("title") or ""); ts = parse_ts(g("pubDate", "published", "updated", "date"))
        if title: out.append((title, ts))
    return out

def score(title):
    t = title.lower(); s = sum(1 for w in BULL if w in t) - sum(1 for w in BEAR if w in t)
    return max(-3, min(3, s)), [k for k, rx in TAGS.items() if re.search(rx, t)]

def one(src):
    name, cat, url = src
    try: return src, read(url), None
    except Exception as e: return src, [], "%s: %s" % (type(e).__name__, str(e)[:60])

def cmd_once():
    os.makedirs(D, exist_ok=True); seen = set()
    try:
        for ln in open(OUT).readlines()[-6000:]:
            try: seen.add(json.loads(ln)["id"])
            except Exception: pass
    except OSError: pass
    now = time.time(); new = []; fails = 0
    with ThreadPoolExecutor(8) as ex:
        for (name, cat, url), items, err in ex.map(one, SOURCES):
            if err: fails += 1
            for title, ts in items:
                i = hashlib.md5((name + "|" + title).encode()).hexdigest()[:12]
                if i in seen: continue
                seen.add(i); sc, tags = score(title)
                new.append({"id": i, "seen": int(now), "pub": int(ts) if ts else None, "src": name, "cat": cat, "title": title[:240], "score": sc, "tags": tags})
    with open(OUT, "a") as f:
        for r in new: f.write(json.dumps(r) + "\n")
    print("news_log: %d new headlines, %d feeds failed, file now %d lines" % (len(new), fails, sum(1 for _ in open(OUT))))

def cmd_probe():
    now = time.time(); print("%-18s %-8s %s" % ("feed", "cat", "result"))
    with ThreadPoolExecutor(8) as ex:
        for (name, cat, url), items, err in ex.map(one, SOURCES):
            if err: print("%-18s %-8s FAIL %s" % (name, cat, err)); continue
            ages = sorted((now - ts) / 60 for _, ts in items if ts)
            print("%-18s %-8s ok %3d items, newest %s min old" % (name, cat, len(items), ("%.0f" % ages[0]) if ages else "?"))

def cmd_report():
    rows = []
    try:
        for ln in open(OUT):
            try: rows.append(json.loads(ln))
            except Exception: pass
    except OSError: print("no news.jsonl yet"); return
    print("%d headlines stored, %s to %s" % (len(rows), time.strftime("%a %d %H:%M", time.localtime(min(r["seen"] for r in rows))), time.strftime("%a %d %H:%M", time.localtime(max(r["seen"] for r in rows)))))
    days = {}
    for r in rows:
        d = time.strftime("%a %d", time.localtime(r.get("pub") or r["seen"])); x = days.setdefault(d, {"n": 0, "bad": 0, "good": 0, "shock": 0})
        x["n"] += 1; x["bad"] += r["score"] < 0; x["good"] += r["score"] > 0; x["shock"] += bool({"outage", "cyber", "bank", "war"} & set(r["tags"]))
    for d, x in days.items(): print("  %s: %4d headlines, %3d bad, %3d good, %3d shock-tagged (outage/cyber/bank/war)" % (d, x["n"], x["bad"], x["good"], x["shock"]))

if __name__ == "__main__":
    {"once": cmd_once, "probe": cmd_probe, "report": cmd_report}.get(sys.argv[1] if len(sys.argv) > 1 else "once", cmd_once)()
