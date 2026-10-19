# Kling 4.0 + Higgsfield: handoff для GrokBot (анимация)

Дата сборки: **2026-10-19**  
Назначение: передать GrokBot контекст по **Kling 4.0** (официальная платформа) и по тому, что **реально доступно через Higgsfield MCP** на момент проверки.

> **Важно:** полные официальные мануалы **не вложены** в этот файл — только ссылки. Скачивайте/читайте их на стороне Kling при необходимости.

---

## 1. Краткий вывод (TL;DR)

| Платформа | Kling 4.0 | Kling 3.x (близкий аналог) |
|-----------|-----------|----------------------------|
| **kling.ai** | ✅ Полный функционал (30s, 21:9, 10 keyframes, 15 refs, Omni Edit) | ✅ Тоже есть |
| **Higgsfield MCP** | ❌ **Не найдено** в каталоге моделей (`kling4` / `Kling 4.0` отсутствует) | ✅ `kling3_0`, Omni 3.0, Turbo, Motion Control, Omni Edit |

**Для GrokBot:** если пайплайн завязан на Higgsfield API/MCP — используйте **Kling 3.x** и таблицу маппинга ниже. Если нужны фичи **только Kling 4** (30 секунд, 21:9, 10 keyframes, 15 референсов) — генерируйте на **kling.ai** или ждите появления Kling 4 в каталоге Higgsfield.

---

## 2. Официальные инструкции Kling 4.0 (только ссылки)

| Документ | URL | Зачем |
|----------|-----|--------|
| **Kling 4.0 User Guide** (полный мануал, ~77 min read) | https://kling.ai/quickstart/kling-4-model-user-guide | Режимы Omni Reference / Keyframes, лимиты, промпты, editing |
| **Introducing Kling 4.0** (анонс возможностей) | https://kling.ai/blog/kling40-kling-visual-realism-creative-control-introducing-storytelling | Обзор апгрейдов: motion, audio, Omni, narrative |
| **Kling 4.0 feature page** | https://kling.ai/feature/kling-4-ai-video-generation | Маркетинг + спецификации 3–30s |
| **Пресс-релиз Kuaishou** | https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-officially-launches-next-generation-kling-40-raising/ | Официальный launch narrative |

**Сравнение Higgsfield vs Kling (сторонний обзор, окт 2026):**  
https://anglr.co/blog/higgsfield-vs-kling — полезно для понимания, что Kling 4.0 может быть **не в прайсе Higgsfield**.

---

## 3. Kling 4.0 — ключевой функционал (для GrokBot)

Источник: официальные страницы Kling (см. ссылки выше). Параметры могут меняться в UI.

### 3.1 Спецификации (сводка)

| Параметр | Kling 4.0 |
|----------|-----------|
| Text-to-Video | ✓ |
| Image-to-Video | ✓ |
| First / Last frame | ✓ |
| **Multiple Keyframes** | ✓, до **10** keyframe images |
| **Omni Reference** | ✓ |
| **Длительность** | **3–30 s** (шаг 1 s, default часто 10 s) |
| Разрешение | 720p / 1080p / **4K** |
| HDR | 10-bit HDR (1080p/4K) — в гайде помечено как coming soon |
| Aspect ratio | **21:9** (new), 16:9, 1:1, 9:16, Auto |
| Аудио | **Stereo, 2-channel**, улучшенный lip-sync |
| Длина промпта | до **~8000 tokens** |
| Ref images | до **10** |
| Ref videos | до **5**, суммарно **≤ 30 s** |
| Elements | до **7** (в т.ч. до 3 video elements) |
| Voice profiles | до **3** на задачу |
| **Всего ref-ассетов** | **≤ 15** (images + videos + voice + elements) |
| Video editing | до 5 клипов (1 primary), каждый 3–30 s, total ≤ 30 s |
| Extension | extend до ~**2 min** (в гайде: coming soon) |
| Flash-режим | **Kling 4.0 Flash** — быстрее/дешевле |

### 3.2 Два режима входа (не комбинируются в одной задаче)

| | **Omni Reference** | **Keyframes** |
|---|-------------------|---------------|
| Когда | Есть ref images/videos/elements/voice или только текст | Ключевые кадры уже заданы, нужна точная привязка к timeline |
| Контролирует | Внешность, стиль, действия, камера | Распределение ключевых моментов по времени |
| Загрузки | Images, videos, voice, elements | **Только images** (до 10 keyframes) |

### 3.3 Omni Reference — практика промптов

- Ассеты нумеруются: `@Image1`, `@Video1`, …
- **Явно указывайте роль** каждого ref: «@Image1: сохранить внешность персонажа», «@Video1: темп монтажа».
- Без ролей модель **угадывает** — результат менее предсказуем.
- Пишите **описательно**, что видно в кадре; избегайте абстракций («premium look»).
- Негативы по гайду обычно нужны только для: **no subtitles**, **no background music** (если не нужны).

### 3.4 Precise Video Editing (Kling 4)

Точечные правки без полной перегенерации: выражение лица, поза, камера, фон, общий стиль — остальная сцена стабильна.

### 3.5 Creative Recreation

Референс ** pacing / composition / visual language** существующего видео + замена продукта/персонажей/ассетов.

---

## 4. Higgsfield MCP — что доступно сейчас (проверка каталога)

Поиск `kling 4` / `kling 4.0` в `models_explore` → **только Kling 3.0 Turbo**, **Kling 4.0 не listed**.

### 4.1 Видео-модели Kling в Higgsfield

| `model` id | Имя | Назначение | Длительность | Medias (roles) | Ключевые params |
|------------|-----|------------|--------------|----------------|-----------------|
| `kling3_0` | Kling v3.0 | Multi-shot, audio, motion transfer | 3–15 s | `start_image`, `end_image` | `mode`: std / pro / **4k**; `sound`: on / off |
| `kling3_0_turbo` | Kling 3.0 Turbo | Быстрый T2V / I2V | 3–15 s | `start_image` | `resolution`: 720p / 1080p |
| `kling_o3_image_reference` | Kling 3.0 Omni | T2V + до **7 ref images** | 3–15 s | `image_references` | `multi_shots`, `multi_prompt[]`, `mode`, `sound` |
| `kling_o3_flf` | Kling 3.0 Omni (Frames) | First/last frame + multi-shot | 3–15 s | `start_image`, `end_image` | как Omni |
| `kling_video_edit` | Kling 3.0 Omni Edit | Edit video по тексту + ref images | — | `video_references`, `image_references` | `mode`: std / pro / 4k |
| `kling3_0_motion_control` | Kling 3.0 Motion Control | Motion с ref video на ref image | — | `image_references`, `video_references` | `mode`, `background_source` |
| `kling2_6` | Kling 2.6 | Cinematic motion, physics | 5 / 10 s | `start_image` | `sound`: bool |

**Aspect ratios (большинство Kling 3.x):** `16:9`, `9:16`, `1:1` — **без 21:9**.

### 4.2 Смежные инструменты Higgsfield (не Kling, но для анимации)

| Инструмент | Когда |
|------------|--------|
| `hf_mult_motion_control` (Genjutsu) | Перенос движения с driving video на персонажа на ref images |
| `hf_mult_replace_object` (Genjutsu) | Замена объекта в source video по ref images |
| `motion_control` | Kling 3.0 Motion Control (legacy alias в экосистеме) |
| `seedance_2_5` / `cinematic_studio_4_0` | Альтернативы, если Kling недостаточно (omni ref, extension, edit modes) |

---

## 5. Маппинг: задача GrokBot → где делать

| Задача | Kling 4.0 (kling.ai) | Higgsfield MCP (сейчас) |
|--------|----------------------|---------------------------|
| Клип **до 30 s** одним прогоном | ✅ | ❌ (max ~15 s на Kling 3.x) |
| **21:9** ultrawide | ✅ | ❌ |
| **10 keyframes** | ✅ Keyframes mode | ⚠️ `start_image` + `end_image` (+ multi_prompt shots) |
| **15 ref assets** (img+video+voice+elements) | ✅ Omni | ⚠️ до 7 `image_references` (Omni) |
| Multi-shot сценарий | ✅ + длиннее | ✅ `multi_shots` + `multi_prompt` |
| Точечный video edit | ✅ Precise Editing | ⚠️ `kling_video_edit` |
| Ремейк ролика с заменой героя/продукта | ✅ Creative Recreation | ⚠️ частично Omni Edit / Genjutsu replace |
| Перенос motion с reference video | ✅ (в экосистеме 4) | ✅ `kling3_0_motion_control` / Genjutsu |
| Стерео + lip-sync pro | ✅ | ⚠️ `sound: on` на 3.x (не заявлено как stereo 4.0) |
| Быстрые итерации | ✅ 4.0 Flash | ✅ `kling3_0_turbo` |

---

## 6. Примеры payload для Higgsfield `generate_video`

Инструмент MCP: **`generate_video`**.  
Перед генерацией: `media_import_url` или `media_upload` → `media_confirm` для картинок/видео.

### 6.1 Image-to-video (простой клип с концепта)

```json
{
  "params": {
    "model": "kling3_0",
    "prompt": "Arcane-style painterly fight scene, hero charges forward in rainy neon alley, dramatic camera push-in, stable motion, no subtitles, no background music",
    "duration": 10,
    "mode": "pro",
    "sound": "on",
    "aspect_ratio": "16:9",
    "medias": [
      { "value": "<MEDIA_ID_OR_JOB_ID>", "role": "start_image" }
    ]
  }
}
```

### 6.2 First + last frame (микро-story между двумя ключами)

```json
{
  "params": {
    "model": "kling_o3_flf",
    "prompt": "Same character, continuous action from ready stance to strike impact, Arcane painterly lighting",
    "duration": 8,
    "mode": "pro",
    "sound": "off",
    "aspect_ratio": "16:9",
    "medias": [
      { "value": "<START_IMAGE_ID>", "role": "start_image" },
      { "value": "<END_IMAGE_ID>", "role": "end_image" }
    ]
  }
}
```

### 6.3 Multi-shot (аналог режиссёрских «шотов», но ≤15s total)

```json
{
  "params": {
    "model": "kling_o3_image_reference",
    "prompt": "Arcane undercity fighter, consistent character design from references",
    "duration": 12,
    "mode": "pro",
    "sound": "on",
    "multi_shots": true,
    "multi_prompt": [
      { "prompt": "Wide: hero in alley, green haze, industrial pipes", "duration": 4 },
      { "prompt": "Medium: glowing runes on arms activate, rain", "duration": 4 },
      { "prompt": "Close: aggressive lunge toward camera", "duration": 4 }
    ],
    "medias": [
      { "value": "<CONCEPT_IMAGE_ID>", "role": "image_references" }
    ],
    "aspect_ratio": "16:9"
  }
}
```

### 6.4 Video edit (правка без полного ремажа)

```json
{
  "params": {
    "model": "kling_video_edit",
    "prompt": "Change background to deeper Zaun green smog, keep character motion and framing identical, Arcane painterly grade",
    "mode": "pro",
    "medias": [
      { "value": "<SOURCE_VIDEO_ID>", "role": "video_references" },
      { "value": "<STYLE_REF_IMAGE_ID>", "role": "image_references" }
    ]
  }
}
```

### 6.5 Motion control (анимация персонажа по driving clip)

```json
{
  "params": {
    "model": "kling3_0_motion_control",
    "medias": [
      { "value": "<CHARACTER_STILL_ID>", "role": "image_references" },
      { "value": "<MOTION_VIDEO_ID>", "role": "video_references" }
    ],
    "mode": "pro",
    "background_source": "input_image"
  }
}
```

### 6.6 Preflight стоимости (без списания)

```json
{
  "params": {
    "model": "kling3_0",
    "prompt": "...",
    "duration": 10,
    "get_cost": true
  }
}
```

---

## 7. MCP workflow (polling)

1. `generate_video` → job id(s)  
2. `job_status` с `sync: true` или `jobs_wait` для batch  
3. `job_display` / `show_generation_by_ids` для показа результата  
4. История: `show_generations` с `type: "video"`

**Типичное время:** video ~60–180 s (из описания MCP).

---

## 8. Референс: уже сгенерированный Arcane-концепт (Higgsfield)

| Поле | Значение |
|------|----------|
| Job ID | `f1ed4a89-a48b-4027-ab22-05f5e93d72a4` |
| Модель image | `soul_cinematic`, 2K, 16:9 |
| PNG URL | https://d8j0ntlcm91z4.cloudfront.net/user_34YtvFPzgzWzaLocJ8iWkwjZpjg/hf_20260910_140619_f1ed4a89-a48b-4027-ab22-05f5e93d72a4.png |

**Рекомендуемый следующий шаг для GrokBot:** import URL → `media_id` → `kling_o3_flf` или `kling_o3_image_reference` (multi_shots).

---

## 9. Промпт-шаблоны для GrokBot (Arcane / game character)

### 9.1 Статичный стиль (image / first frame)

```
Arcane animated series visual style, painterly hand-painted illustration, thick brushstrokes,
dramatic cinematic lighting, deep shadows and glowing accent colors, semi-realistic stylized proportions,
steampunk-fantasy undercity Zaun aesthetic, visible paint texture, no text, no watermark
```

### 9.2 Motion (video)

```
Arcane-style painterly 3D animation look, stable body mechanics, controlled camera,
[wide|medium|close] shot, [action description], rain and green industrial haze,
no subtitles, no background music
```

### 9.3 Multi-shot beats (для `multi_prompt`)

```
Shot 1 — Establishing: ...
Shot 2 — Action beat: ...
Shot 3 — Payoff: ...
Character design locked to reference image, consistent face and costume
```

---

## 10. Ограничения и риски для автomation

1. **Kling 4 ≠ Higgsfield catalog** — не хардкодить `model: "kling4"` в GrokBot до появления в `models_explore`.
2. **Длина:** планируйте сценарии **≤15 s** на Higgsfield Kling 3.x; **≤30 s** только на kling.ai 4.0.
3. **21:9** — только Kling 4 native; на Higgsfield используйте 16:9 + post crop/reframe (`reframe` tool).
4. **Reference elements (Higgsfield):** для некоторых моделей placeholders `<<<element_id>>>` в prompt — см. MCP tool `show_reference_elements` (отдельно от Kling native Elements).
5. **Credits:** генерации списывают кредиты workspace; `balance` / `get_cost` перед batch.
6. **IP / reveal:** часть seedance-family jobs может требовать `reveal_generation` — для Kling смотреть status job.

---

## 11. Чеклист передачи в GrokBot

- [ ] Решить платформу: **kling.ai (4.0)** vs **Higgsfield (3.x)** по таблице маппинга §5  
- [ ] Подтянуть официальный гайд: https://kling.ai/quickstart/kling-4-model-user-guide  
- [ ] Для Higgsfield: зафиксировать `model` id из §4.1  
- [ ] Загрузить концепт → получить `media_id`  
- [ ] Выбрать режим: simple I2V / FLF / multi_shots / edit / motion_control  
- [ ] В промпте явно: **no subtitles, no background music** (если нужно)  
- [ ] Poll: `job_status` / `jobs_wait`  
- [ ] Экспорт URL → следующий этап пайплайна GrokBot  

---

## 12. Полезные MCP tools (Higgsfield)

| Tool | Назначение |
|------|------------|
| `models_explore` | list / search / get / recommend моделей |
| `generate_video` | основная генерация |
| `generate_video_batch` | до 12 параллельных jobs |
| `media_import_url` | import HTTPS asset → media_id |
| `media_upload` + `media_confirm` | upload bytes |
| `job_status`, `jobs_wait` | polling |
| `balance`, `transactions` | кредиты |
| `list_workspaces`, `select_workspace` | billing context |

---

*Файл подготовлен для handoff в GrokBot. Обновляйте §4 после появления Kling 4.0 в каталоге Higgsfield (`models_explore` search: `kling 4`).*
