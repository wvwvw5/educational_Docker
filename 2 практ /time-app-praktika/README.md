# Time App - Docker практическая работа

Веб-приложение для сохранения и отображения времени, развернутое в Docker контейнерах.

## Архитектура приложения

- **Frontend**: Vue.js 3 + Vite (порт 80)
- **Backend API**: Node.js + Express (порт 5000)
- **База данных**: MySQL 8.0 (порт 3306)
- **Админка БД**: Adminer (порт 8080)

## Структура проекта

```
time-app-praktika/
├── api/                    # Backend API
│   ├── src/
│   │   └── utils/
│   │       ├── mysqlPool.mjs
│   │       └── records.mjs
│   ├── Dockerfile
│   ├── package.json
│   └── index.mjs
├── frontend/               # Frontend приложение
│   ├── src/
│   │   ├── components/
│   │   ├── utils/
│   │   └── assets/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml      # Конфигурация всех сервисов
└── README.md
```

## Запуск приложения

### Требования
- Docker
- Docker Compose

### Команды для запуска

```bash
# Клонирование репозитория
git clone <repository-url>
cd time-app-praktika

# Запуск всех сервисов
docker-compose up --build

# Запуск в фоновом режиме
docker-compose up -d --build
```

### Доступ к приложению

- **Веб-приложение**: http://localhost
- **API**: http://localhost:5000
- **Adminer (управление БД)**: http://localhost:8080
  - Сервер: `mysql`
  - Пользователь: `root`
  - Пароль: `password`
  - База данных: `time_db`

## API Endpoints

- `GET /` - Проверка работы API
- `GET /times` - Получить все сохраненные времена
- `POST /times` - Сохранить новое время
- `DELETE /time/:id` - Удалить время по ID

## Полезные команды

```bash
# Просмотр логов
docker-compose logs

# Остановка сервисов
docker-compose down

# Пересборка образов
docker-compose build

# Просмотр запущенных контейнеров
docker ps

# Подключение к контейнеру
docker exec -it time-api bash
docker exec -it time-mysql mysql -u root -p
```

## Разработка

### Локальная разработка

```bash
# Backend
cd api
npm install
npm run dev

# Frontend
cd frontend
npm install
npm run dev
```

### Переменные окружения

API поддерживает следующие переменные окружения:
- `MYSQL_HOST` - хост MySQL (по умолчанию: mysql)
- `MYSQL_PORT` - порт MySQL (по умолчанию: 3306)
- `MYSQL_USER` - пользователь MySQL (по умолчанию: root)
- `MYSQL_PASSWORD` - пароль MySQL (по умолчанию: password)
- `MYSQL_DATABASE` - имя базы данных (по умолчанию: time_db)

## Технологии

- **Frontend**: Vue.js 3, Vite, Moment.js
- **Backend**: Node.js, Express, MySQL2
- **База данных**: MySQL 8.0
- **Контейнеризация**: Docker, Docker Compose
- **Веб-сервер**: Nginx (для фронтенда)
