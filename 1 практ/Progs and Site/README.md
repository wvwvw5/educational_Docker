# Docker Практическая Работа

Этот проект содержит различные приложения, упакованные в Docker контейнеры.

## Содержимое проекта

### Приложения
1. **Java калькулятор** (`calc-java/`) - Простой калькулятор на Java
2. **Python калькулятор** (`calc-py/`) - Калькулятор на Python с меню
3. **Dart калькулятор** (`dart-calc/`) - Калькулятор на Dart
4. **Java игра** (`game-java/`) - Игра "Угадай число" на Java
5. **Python игра** (`rpsgame-py/`) - Игра "Камень-ножницы-бумага" на Python
6. **Веб-сайт** (`site/`) - Простой веб-сайт на HTML

## Требования

- Docker
- Docker Compose

## Инструкции по запуску

### Запуск всех сервисов
```bash
docker-compose up --build
```

### Запуск отдельных сервисов

#### Java калькулятор
```bash
cd calc-java
docker build -t java-calc .
docker run -it java-calc
```

#### Python калькулятор
```bash
cd calc-py
docker build -t python-calc .
docker run -it python-calc
```

#### Dart калькулятор
```bash
cd dart-calc
docker build -t dart-calc .
docker run -it dart-calc
```

#### Java игра
```bash
cd game-java
docker build -t java-game .
docker run -it java-game
```

#### Python игра
```bash
cd rpsgame-py
docker build -t python-rps .
docker run -it python-rps
```

#### Веб-сайт
```bash
cd site
docker build -t nginx-site .
docker run -p 8080:80 nginx-site
```
Затем откройте браузер и перейдите по адресу: http://localhost:8080

## Остановка сервисов

```bash
docker-compose down
```

## Полезные команды

### Просмотр запущенных контейнеров
```bash
docker ps
```

### Просмотр всех контейнеров
```bash
docker ps -a
```

### Просмотр образов
```bash
docker images
```

### Удаление контейнеров
```bash
docker rm <container_id>
```

### Удаление образов
```bash
docker rmi <image_id>
```

### Очистка системы Docker
```bash
docker system prune -a
```
