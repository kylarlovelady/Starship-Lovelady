#!/usr/bin/env python3
"""Print the ready-to-paste KDP listing (title, description, 7 keywords, price, settings) for a title slug from tasks/kdp_series.json.
Usage: python3 kdp_listing.py [process-operator|lab-operator|...]   (no argument = all titles)"""
import json, os, sys
S = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kdp_series.json")))
for slug, t in S["titles"].items():
    if len(sys.argv) > 1 and sys.argv[1] != slug: continue
    title = " ".join(w.capitalize() for w in t["lines"])
    print("== %s" % title); print("Title: %s | Author: %s | no subtitle | price $%s" % (title, S["settings"]["author"], S["price_usd"]))
    print("Description: " + S["description_template"].format(role=t["role"], log_words=t["log_words"]))
    print("Keywords: " + "; ".join(k.format(keyword_job=t["keyword_job"]) for k in S["keywords"]))
    print("Colours: " + ", ".join("%s (%s)" % (v["name"], k.upper()) for k, v in S["schemes"].items())); print()
