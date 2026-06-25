#!/usr/bin/env python3
"""Build first 20 roadmap rows from backlog DSL for Miro table sync."""
import json
import re
from datetime import datetime, timedelta, timezone

DIRECTIONS = [
    ("bi", "BI + Сквозная аналитика"),
    ("ab", "АБ-тесты + Чистый ручеёк"),
    ("smart", "Смарт-движок и модели"),
    ("mech", "Механики on-site"),
    ("stavki", "Ставки и контрагенты"),
    ("crm", "CRM и коммуникации"),
    ("retarget", "Ретаргетинг и медиа"),
    ("mobile", "Мобилка"),
    ("mgmt", "Менеджмент и рутина"),
    ("tech", "Тех.долг и инфра"),
    ("raznoe", "Разное"),
    ("competitors", "Конкуренты и ресёрч"),
]

DIRECTION_TO_NAPRAVLENIE = {
    "bi": "BI отчётность",
    "ab": "Чистый ручеёк и АБ тесты",
    "smart": "Смарт Движок (автоматизация) (умнота)",
    "mech": "Подбор правильных офферов в моменте",
    "stavki": "Выбивание ставок",
    "crm": "Пуши",
    "retarget": "Аналитика",
    "mobile": "Мобилка",
    "mgmt": "BI отчётность",
    "tech": "Аналитика",
    "raznoe": "Аналитика",
    "competitors": "Аналитика",
}

CLASSIFICATION = {
    "3458764676440309011": "bi",
    "3458764676440309012": "ab",
    "3458764676440309013": "ab",
    "3458764676440309014": "smart",
    "3458764676440309015": "raznoe",
    "3458764676440309016": "stavki",
    "3458764676440309017": "retarget",
    "3458764676440309018": "crm",
    "3458764676440309019": "crm",
    "3458764676440309020": "bi",
    "3458764676440309021": "raznoe",
    "3458764676440309022": "smart",
    "3458764676440309023": "stavki",
    "3458764676440309024": "mech",
    "3458764676440309025": "mech",
    "3458764676440309026": "mech",
    "3458764676440309027": "mech",
    "3458764676440309030": "crm",
    "3458764676440309031": "raznoe",
    "3458764676440309032": "raznoe",
    "3458764676440309033": "tech",
    "3458764676440309034": "crm",
    "3458764676440309035": "retarget",
    "3458764676440309036": "mech",
    "3458764676440309037": "bi",
    "3458764676440309038": "stavki",
    "3458764676440309039": "competitors",
    "3458764676440309040": "crm",
    "3458764676440309041": "raznoe",
    "3458764676440309042": "bi",
    "3458764676440309043": "crm",
    "3458764676440309046": "raznoe",
    "3458764676440309047": "mech",
    "3458764676440309048": "mech",
    "3458764676440309049": "smart",
    "3458764676440309050": "smart",
    "3458764676440309053": "mech",
    "3458764676440309054": "mech",
    "3458764676440309055": "mech",
    "3458764676440309056": "crm",
    "3458764676440309057": "mobile",
    "3458764676440309058": "mech",
    "3458764676440309059": "mech",
    "3458764676440309060": "mech",
    "3458764676440309061": "mech",
    "3458764676440309062": "mech",
    "3458764676440309063": "mech",
    "3458764676440309064": "mech",
    "3458764676440309065": "mech",
    "3458764676440309066": "crm",
    "3458764676440309067": "smart",
    "3458764676440309068": "smart",
    "3458764676440309070": "smart",
    "3458764676440309071": "smart",
    "3458764676440309072": "smart",
    "3458764676440309073": "smart",
    "3458764676440309074": "smart",
    "3458764676440309075": "ab",
    "3458764676440309076": "smart",
    "3458764676440309078": "mgmt",
    "3458764676440309079": "mgmt",
    "3458764676440309080": "mgmt",
    "3458764676440309081": "mgmt",
    "3458764676440309082": "mgmt",
    "3458764676440309083": "smart",
    "3458764676440309084": "smart",
    "3458764676440309085": "mgmt",
    "3458764676440309086": "mgmt",
    "3458764676440309087": "smart",
    "3458764676440309089": "mech",
    "3458764676440309090": "mech",
    "3458764676440309091": "mech",
    "3458764676440309092": "mech",
    "3458764676440309093": "stavki",
    "3458764676440309095": "retarget",
    "3458764676440309096": "retarget",
    "3458764676440309097": "crm",
    "3458764676440309099": "mech",
    "3458764676440309100": "mech",
    "3458764676440309101": "mech",
    "3458764676440309102": "mech",
    "3458764676440309103": "competitors",
    "3458764676440309104": "competitors",
    "3458764676440309105": "raznoe",
    "3458764676440309106": "smart",
    "3458764676440309107": "smart",
    "3458764676440309108": "bi",
    "3458764676440309109": "raznoe",
    "3458764676440309110": "competitors",
    "3458764676440309111": "mech",
    "3458764676440309112": "ab",
    "3458764676440309113": "mech",
    "3458764676440309114": "mech",
    "3458764676440309115": "mech",
    "3458764676440309120": "ab",
    "3458764676440309121": "mgmt",
    "3458764676440309122": "mobile",
    "3458764676440309123": "crm",
    "3458764676440309124": "mech",
    "3458764676440309125": "mech",
    "3458764676440309126": "mech",
    "3458764676440309127": "mech",
    "3458764676440309128": "mech",
    "3458764676440309130": "mech",
    "3458764676440309131": "mech",
    "3458764676440309132": "mech",
    "3458764676440309133": "mech",
    "3458764676440309134": "mech",
    "3458764676440309135": "mobile",
    "3458764676440309136": "mech",
    "3458764676440309137": "mech",
    "3458764676440309138": "mech",
    "3458764676440309139": "mech",
    "3458764676440309140": "mech",
    "3458764676440309141": "mech",
    "3458764676440309142": "mech",
}

DIR_ORDER = {k: i for i, (k, _) in enumerate(DIRECTIONS)}
DIR_LABEL = {k: label for k, label in DIRECTIONS}

CARD_RE = re.compile(
    r"moveToWidget=(\d+) CARD .*? x=([\d.]+) y=([\d.]+) .*? theme=(#[0-9a-fA-F]+)"
    r'(?: desc="((?:[^"\\]|\\.)*)")? "((?:[^"\\]|\\.)*)"',
    re.DOTALL,
)


def strip_html(text: str) -> str:
    text = text.replace("\\\"", '"')
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:5000]


def theme_to_status(theme: str) -> str:
    if theme.lower() in ("#067429", "#2dc75c"):
        return "Done"
    if theme.lower() == "#6631d7":
        return "To do"
    return "To do"


def theme_to_priority(theme: str) -> str:
    if theme.lower() == "#6631d7":
        return "High"
    if theme.lower() in ("#067429", "#2dc75c"):
        return "Low"
    return "Medium"


def parse_cards(dsl: str) -> list[dict]:
    cards = []
    for m in CARD_RE.finditer(dsl):
        wid, x, y, theme, desc, title = m.groups()
        if wid not in CLASSIFICATION:
            continue
        dkey = CLASSIFICATION[wid]
        cards.append(
            {
                "id": wid,
                "x": float(x),
                "y": float(y),
                "theme": theme,
                "title": strip_html(title),
                "description": strip_html(desc or ""),
                "direction_key": dkey,
                "direction_label": DIR_LABEL[dkey],
                "napravlenie": DIRECTION_TO_NAPRAVLENIE[dkey],
            }
        )
    return cards


def sort_cards(cards: list[dict]) -> list[dict]:
    return sorted(
        cards,
        key=lambda c: (DIR_ORDER[c["direction_key"]], c["y"], c["x"]),
    )


def build_timeline(rows: list[dict], start: datetime) -> list[dict]:
    """Sequential 2-week slots per task, grouped by direction on same timeline track."""
    out = []
    cursor = start
    for row in rows:
        end = cursor + timedelta(days=14)
        row = dict(row)
        row["start_date"] = cursor.strftime("%Y-%m-%dT09:00:00Z")
        row["end_date"] = end.strftime("%Y-%m-%dT18:00:00Z")
        out.append(row)
        cursor = end + timedelta(days=1)
    return out


def to_table_rows(items: list[dict]) -> list[dict]:
    table_rows = []
    for item in items:
        cells = [
            {"columnTitle": "Title", "value": item["title"]},
            {"columnTitle": "Status", "value": theme_to_status(item["theme"])},
            {"columnTitle": "Priority", "value": theme_to_priority(item["theme"])},
            {"columnTitle": "Description", "value": item["description"]},
            {"columnTitle": "Group", "value": item["direction_label"]},
            {"columnTitle": "Направление", "value": item["napravlenie"]},
            {"columnTitle": "Start Date", "value": item["start_date"]},
            {"columnTitle": "End Date", "value": item["end_date"]},
        ]
        table_rows.append({"cells": cells})
    return table_rows


def main():
    dsl_path = "/workspace/miro_updates/roadmap/backlog_full.dsl"
    dsl = open(dsl_path, encoding="utf-8").read()
    cards = sort_cards(parse_cards(dsl))
    pilot = build_timeline(cards[:20], datetime(2026, 6, 24, 9, 0, tzinfo=timezone.utc))

    out_dir = "/workspace/miro_updates/roadmap"
    json.dump(pilot, open(f"{out_dir}/pilot_cards.json", "w"), ensure_ascii=False, indent=2)
    json.dump(
        to_table_rows(pilot),
        open(f"{out_dir}/pilot_table_rows.json", "w"),
        ensure_ascii=False,
        indent=2,
    )
    groups = sorted({c["direction_label"] for c in pilot})
    json.dump(groups, open(f"{out_dir}/pilot_groups.json", "w"), ensure_ascii=False, indent=2)
    print(f"Parsed {len(cards)} cards, pilot {len(pilot)}")
    for i, c in enumerate(pilot, 1):
        print(f"{i:2}. [{c['direction_label']}] {c['title'][:60]}")


if __name__ == "__main__":
    main()
