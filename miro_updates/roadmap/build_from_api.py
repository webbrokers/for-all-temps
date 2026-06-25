#!/usr/bin/env python3
"""Build pilot roadmap rows from backlog cards API export."""
import json
import re
from datetime import datetime, timedelta, timezone

from build_transfer import (
    CLASSIFICATION,
    DIR_LABEL,
    DIR_ORDER,
    DIRECTION_TO_NAPRAVLENIE,
    build_timeline,
    strip_html,
    theme_to_priority,
    theme_to_status,
    to_table_rows,
)


def parse_api_cards(items: list[dict]) -> list[dict]:
    cards = []
    for item in items:
        wid = item["id"]
        if wid not in CLASSIFICATION:
            continue
        dkey = CLASSIFICATION[wid]
        title = strip_html(item.get("data", {}).get("title", ""))
        if not title:
            continue
        desc = strip_html(item.get("data", {}).get("description", ""))
        theme = item.get("style", {}).get("cardTheme", "#ffdc4a")
        pos = item.get("position", {})
        cards.append(
            {
                "id": wid,
                "x": float(pos.get("x", 0)),
                "y": float(pos.get("y", 0)),
                "theme": theme,
                "title": title,
                "description": desc,
                "direction_key": dkey,
                "direction_label": DIR_LABEL[dkey],
                "napravlenie": DIRECTION_TO_NAPRAVLENIE[dkey],
            }
        )
    return sorted(cards, key=lambda c: (DIR_ORDER[c["direction_key"]], c["y"], c["x"]))


def main():
    src = "/workspace/miro_updates/roadmap/backlog_cards.json"
    items = json.load(open(src, encoding="utf-8"))
    cards = parse_api_cards(items)
    pilot = build_timeline(cards[:20], datetime(2026, 6, 24, 9, 0, tzinfo=timezone.utc))
    out = "/workspace/miro_updates/roadmap"
    json.dump(pilot, open(f"{out}/pilot_cards.json", "w"), ensure_ascii=False, indent=2)
    json.dump(to_table_rows(pilot), open(f"{out}/pilot_table_rows.json", "w"), ensure_ascii=False, indent=2)
    groups = sorted({c["direction_label"] for c in pilot})
    json.dump(groups, open(f"{out}/pilot_groups.json", "w"), ensure_ascii=False, indent=2)
    print(f"Total classified cards: {len(cards)}")
    print(f"Pilot rows: {len(pilot)}")
    for i, c in enumerate(pilot, 1):
        print(f"{i:2}. [{c['direction_label']}] {c['title'][:70]}")
