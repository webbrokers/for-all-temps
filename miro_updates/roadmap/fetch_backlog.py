#!/usr/bin/env python3
"""Fetch all backlog cards from Miro API and save to backlog_cards.json."""
import json
import subprocess
import sys

# Cards are fetched via MCP in agent; this script merges saved pages.
# Run: python fetch_backlog.py page1.json page2.json page3.json

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fetch_backlog.py <page*.json>...")
        sys.exit(1)
    items = []
    for path in sys.argv[1:]:
        data = json.load(open(path, encoding="utf-8"))
        items.extend(data.get("data", data))
    out = "/workspace/miro_updates/roadmap/backlog_cards.json"
    json.dump(items, open(out, "w"), ensure_ascii=False, indent=2)
    print(f"Saved {len(items)} cards to {out}")
