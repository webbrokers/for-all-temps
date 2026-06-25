#!/usr/bin/env python3
"""Generate pilot 20 rows JSON for Miro table sync."""
import json
from datetime import datetime, timedelta, timezone

from build_transfer import (
    DIRECTION_TO_NAPRAVLENIE,
    build_timeline,
    strip_html,
    theme_to_priority,
    theme_to_status,
    to_table_rows,
)

PILOT_CARDS = [
    {"id": "3458764676440309011", "direction_key": "bi", "direction_label": "BI + Сквозная аналитика",
     "title": "Движок Трекинга и Аналитики", "theme": "#6631d7", "description": "Сквозная идентификация клиентов на витринах для умной монетизации"},
    {"id": "3458764676440309020", "direction_key": "bi", "direction_label": "BI + Сквозная аналитика",
     "title": "Сквозная отчётность перформа", "theme": "#6631d7", "description": "Видеть клиента от Входа до Канала монетизации и считать перформ"},
    {"id": "3458764676440309037", "direction_key": "bi", "direction_label": "BI + Сквозная аналитика",
     "title": "Сокращатель ссылок для Трекинга", "theme": "#ffdc4a", "description": "Подойдёт для собственного трекинга, чтобы лучше атрибутировать клики с СМСок"},
    {"id": "3458764676440309042", "direction_key": "bi", "direction_label": "BI + Сквозная аналитика",
     "title": "Трекинг сквозной аналитики и атрибуция", "theme": "#ffdc4a", "description": "Модуль записи всех шагов и ивентов по клиенту в ClickHouse"},
    {"id": "3458764676440309108", "direction_key": "bi", "direction_label": "BI + Сквозная аналитика",
     "title": "Построение сквозной аналитики от Расхода до Дохода в автоматическом режиме", "theme": "#ffdc4a",
     "description": "Считать доходность от отказного трафика на каждый входящий источник"},
    {"id": "3458764676440309012", "direction_key": "ab", "direction_label": "АБ-тесты + Чистый ручеёк",
     "title": "Считать эффективность / показать дельту", "theme": "#6631d7", "description": "Чёткий контроль профита от работы команды через чистый ручеёк"},
    {"id": "3458764676440309013", "direction_key": "ab", "direction_label": "АБ-тесты + Чистый ручеёк",
     "title": "Движок АБ Тестов", "theme": "#6631d7", "description": "Проводить АБС пилоты различных решений с сохранением данных в аналитическом контуре"},
    {"id": "3458764676440309075", "direction_key": "ab", "direction_label": "АБ-тесты + Чистый ручеёк",
     "title": "Чистый Ручеек", "theme": "#ffdc4a", "description": "Сплитовка на витрины СРА сетей и тестирование разных ссылок на один оффер"},
    {"id": "3458764676440309112", "direction_key": "ab", "direction_label": "АБ-тесты + Чистый ручеёк",
     "title": "АБ тестирование дизайна витрин", "theme": "#ffdc4a", "description": "Глобальный тест разных дизайнов, размеров плашек и т.д."},
    {"id": "3458764676440309120", "direction_key": "ab", "direction_label": "АБ-тесты + Чистый ручеёк",
     "title": "АБС Эксперименты (модуль/движок)", "theme": "#6631d7", "description": "Быстро и безболезненно проводить эксперименты с контрагентами"},
    {"id": "3458764676440309014", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Смарт Движок отказных 1.0 + Умнение", "theme": "#6631d7", "description": "Подключение всех витрин на Смарт Движок и управление трафиком через платформу"},
    {"id": "3458764676440309022", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Быстрые сайты на Смарте \"в 2 клика\"", "theme": "#6631d7", "description": "Набор ПО для быстрого развёртывания на новый источник или проект"},
    {"id": "3458764676440309049", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Анифрод + анти мотив", "theme": "#ffdc4a", "description": "Модуль антифрода в трафиковом потоке"},
    {"id": "3458764676440309050", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Качество трафика", "theme": "#ffdc4a", "description": "Модель качества клиентов по вебмастерам и источникам на входе"},
    {"id": "3458764676440309068", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Фичеринг для СМАРТ", "theme": "#ffdc4a", "description": "Раз в квартал генерировать новые фичи для моделей"},
    {"id": "3458764676440309070", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Модуль автоподкидывания офферов", "theme": "#067429", "description": "Тестирование новых офферов без слива бюджета с топовых"},
    {"id": "3458764676440309071", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Обогащение внешними данными", "theme": "#ffdc4a", "description": "Обогащение данных по клиентам в БД из DMP и других источников"},
    {"id": "3458764676440309072", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Переобучение моделей без данных БКИ", "theme": "#ffdc4a", "description": "Новая регуляторка — модели без сильных переменных БКИ"},
    {"id": "3458764676440309073", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Модуль АБ пилотов смарт моделей", "theme": "#ffdc4a", "description": "АБ пилоты на каждом элементе: плейсмент, механика, витрина, ссылки"},
    {"id": "3458764676440309074", "direction_key": "smart", "direction_label": "Смарт-движок и модели",
     "title": "Построение моделей для всех типов трафика", "theme": "#ffdc4a", "description": "Модели не только для отказного 301, но и для всех механик"},
]

for c in PILOT_CARDS:
    c["napravlenie"] = DIRECTION_TO_NAPRAVLENIE[c["direction_key"]]

pilot = build_timeline(PILOT_CARDS, datetime(2026, 6, 24, 9, 0, tzinfo=timezone.utc))
out = "/workspace/miro_updates/roadmap"
json.dump(pilot, open(f"{out}/pilot_cards.json", "w"), ensure_ascii=False, indent=2)
json.dump(to_table_rows(pilot), open(f"{out}/pilot_table_rows.json", "w"), ensure_ascii=False, indent=2)
groups = sorted({c["direction_label"] for c in pilot})
json.dump(groups, open(f"{out}/pilot_groups.json", "w"), ensure_ascii=False, indent=2)
print(f"Generated {len(pilot)} pilot rows")
for i, c in enumerate(pilot, 1):
    print(f"{i:2}. [{c['direction_label']}] {c['title'][:60]}")
