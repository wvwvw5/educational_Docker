# ИНСТРУКЦИИ ДЛЯ ЗАГРУЗКИ НА GITLAB/GITHUB

## Подготовка к загрузке

### 1. Инициализация Git репозитория
```bash
cd "Progs and Site"
git init
```

### 2. Создание .gitignore файла
```bash
cat > .gitignore << EOF
# Системные файлы
.DS_Store
Thumbs.db

# Docker файлы (опционально, если хотите включить их в репозиторий)
# Dockerfile
# docker-compose.yml

# Временные файлы
*.tmp
*.log
*.swp
*.swo

# IDE файлы
.vscode/
.idea/
*.iml

# Python кэш
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Java классы
*.class
EOF
```

### 3. Добавление файлов в репозиторий
```bash
git add .
git commit -m "Initial commit: Docker практическая работа

- Добавлены Dockerfile для всех приложений
- Создан docker-compose.yml
- Добавлены инструкции и документация
- Включены тестовые скрипты"
```

## Загрузка на GitLab

### 1. Создание репозитория на GitLab
1. Войдите в GitLab
2. Нажмите "New Project"
3. Выберите "Create blank project"
4. Введите название: `docker-practical-work`
5. Установите видимость (Private/Public)
6. Нажмите "Create project"

### 2. Подключение локального репозитория
```bash
git remote add origin https://gitlab.com/YOUR_USERNAME/docker-practical-work.git
git branch -M main
git push -u origin main
```

## Загрузка на GitHub

### 1. Создание репозитория на GitHub
1. Войдите в GitHub
2. Нажмите "New repository"
3. Введите название: `docker-practical-work`
4. Добавьте описание: "Практическая работа по Docker с различными приложениями"
5. Выберите видимость (Private/Public)
6. НЕ инициализируйте с README (у нас уже есть файлы)
7. Нажмите "Create repository"

### 2. Подключение локального репозитория
```bash
git remote add origin https://github.com/YOUR_USERNAME/docker-practical-work.git
git branch -M main
git push -u origin main
```

## Структура репозитория

После загрузки структура будет выглядеть так:

```
docker-practical-work/
├── calc-java/
│   ├── calc.java
│   └── Dockerfile
├── calc-py/
│   ├── calc.py
│   └── Dockerfile
├── dart-calc/
│   ├── calc.dart
│   └── Dockerfile
├── game-java/
│   ├── game.java
│   └── Dockerfile
├── rpsgame-py/
│   ├── RockPaperScissorsGame.py
│   └── Dockerfile
├── site/
│   ├── *.html
│   └── Dockerfile
├── docker-compose.yml
├── README.md
├── test-commands.sh
├── .dockerignore
└── .gitignore
```

## Дополнительные команды

### Обновление репозитория
```bash
git add .
git commit -m "Описание изменений"
git push
```

### Клонирование репозитория
```bash
git clone https://gitlab.com/YOUR_USERNAME/docker-practical-work.git
# или
git clone https://github.com/YOUR_USERNAME/docker-practical-work.git
```

### Просмотр статуса
```bash
git status
git log --oneline
```

## Ссылка для отчета

После загрузки скопируйте ссылку на репозиторий:
- GitLab: `https://gitlab.com/YOUR_USERNAME/docker-practical-work`
- GitHub: `https://github.com/YOUR_USERNAME/docker-practical-work`

Эта ссылка будет использоваться в отчете по практической работе.
