#!/usr/bin/env python3
"""Build Miro table_sync_rows payload from pilot_table_rows.json."""
import json

GROUP_MAP = {
    "BI + Сквозная аналитика": "Group 1",
    "АБ-тесты + Чистый ручеёк": "Group 2",
    "Смарт-движок и модели": "Group 3",
}

STUB_ROW_IDS = ["0", "ebf68c41-5930-4138-b3ac-293cae063fd5", "1", "2"]

rows_in = json.load(open("/workspace/miro_updates/roadmap/pilot_table_rows.json", encoding="utf-8"))
out = []
for i, row in enumerate(rows_in):
    cells = []
    for cell in row["cells"]:
        c = dict(cell)
        if c["columnTitle"] == "Group":
            c["value"] = GROUP_MAP.get(c["value"], c["value"])
        cells.append(c)
    item = {"cells": cells}
    if i < len(STUB_ROW_IDS):
        item["rowId"] = STUB_ROW_IDS[i]
    out.append(item)

json.dump(out, open("/workspace/miro_updates/roadmap/sync_payload.json", "w"), ensure_ascii=False, indent=2)
print(f"Payload rows: {len(out)}")
print("Batch 1:", len(out[:10]), "Batch 2:", len(out[10:]))
