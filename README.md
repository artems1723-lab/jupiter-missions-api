# Jupiter Missions API

API для управления миссиями к спутникам Юпитера.

## Предметная область

Система учёта космических миссий к спутникам Юпитера. Позволяет:
- Отслеживать космические аппараты (Spacecraft)
- Управлять целями — спутниками Юпитера (Target)
- Планировать миссии (Mission)
- Регистрировать научные приборы (Instrument)
- Назначать приборы на миссии (MissionInstrument)

## Эндпоинты API

Базовый URL: `http://127.0.0.1:17450/api/v1/`

### 1. Космические аппараты (`/spacecraft/`)

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/spacecraft/` | Список всех аппаратов |
| GET | `/spacecraft/?country=США` | Фильтрация по стране |
| GET | `/spacecraft/?status=в пути` | Фильтрация по статусу |
| GET | `/spacecraft/{id}/` | Получить один аппарат |
| POST | `/spacecraft/` | Создать один аппарат |
| POST | `/spacecraft/` | Создать несколько аппаратов (массив) |
| PUT | `/spacecraft/{id}/` | Полное обновление |
| PATCH | `/spacecraft/{id}/` | Частичное обновление одного |
| PATCH | `/spacecraft/` | Массовое обновление (массив с id) |
| DELETE | `/spacecraft/{id}/` | Удалить один |
| DELETE | `/spacecraft/batch/?ids=1,2,3` | Массовое удаление |

### 2. Спутники Юпитера (`/targets/`)

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/targets/` | Список всех спутников |
| GET | `/targets/?has_ocean=true` | Фильтрация по океану |
| GET | `/targets/?type=галилеевы` | Фильтрация по типу |
| GET | `/targets/{id}/` | Получить один спутник |
| POST | `/targets/` | Создать один спутник |
| POST | `/targets/` | Создать несколько (массив) |
| PUT | `/targets/{id}/` | Полное обновление |
| PATCH | `/targets/{id}/` | Частичное обновление одного |
| PATCH | `/targets/` | Массовое обновление |
| DELETE | `/targets/{id}/` | Удалить один |
| DELETE | `/targets/batch/?ids=1,2,3` | Массовое удаление |

### 3. Миссии (`/missions/`)

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/missions/` | Список всех миссий |
| GET | `/missions/?spacecraft_id=1` | Фильтрация по аппарату |
| GET | `/missions/?target_id=1` | Фильтрация по спутнику |
| GET | `/missions/?status=активна` | Фильтрация по статусу |
| GET | `/missions/{id}/` | Получить одну миссию |
| POST | `/missions/` | Создать одну миссию |
| POST | `/missions/` | Создать несколько (массив) |
| PUT | `/missions/{id}/` | Полное обновление |
| PATCH | `/missions/{id}/` | Частичное обновление одной |
| PATCH | `/missions/` | Массовое обновление |
| DELETE | `/missions/{id}/` | Удалить одну |
| DELETE | `/missions/batch/?ids=1,2,3` | Массовое удаление |

### 4. Научные приборы (`/instruments/`)

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/instruments/` | Список всех приборов |
| GET | `/instruments/?type=камера` | Фильтрация по типу |
| GET | `/instruments/{id}/` | Получить один прибор |
| POST | `/instruments/` | Создать один прибор |
| POST | `/instruments/` | Создать несколько (массив) |
| PUT | `/instruments/{id}/` | Полное обновление |
| PATCH | `/instruments/{id}/` | Частичное обновление одного |
| PATCH | `/instruments/` | Массовое обновление |
| DELETE | `/instruments/{id}/` | Удалить один |
| DELETE | `/instruments/batch/?ids=1,2,3` | Массовое удаление |

### 5. Связи миссий и приборов (`/mission-instruments/`)

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/mission-instruments/` | Список всех связей |
| GET | `/mission-instruments/?mission_id=1` | Фильтрация по миссии |
| GET | `/mission-instruments/?instrument_id=1` | Фильтрация по прибору |
| GET | `/mission-instruments/{id}/` | Получить одну связь |
| POST | `/mission-instruments/` | Создать одну связь |
| POST | `/mission-instruments/` | Создать несколько (массив) |
| PUT | `/mission-instruments/{id}/` | Полное обновление |
| PATCH | `/mission-instruments/{id}/` | Частичное обновление одной |
| PATCH | `/mission-instruments/` | Массовое обновление |
| DELETE | `/mission-instruments/{id}/` | Удалить одну |
| DELETE | `/mission-instruments/batch/?ids=1,2,3` | Массовое удаление |

## Документация

- Swagger UI: `http://127.0.0.1:17450/api/schema/swagger-ui/`

## Установка

```bash
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver