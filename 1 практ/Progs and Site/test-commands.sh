#!/bin/bash

# Скрипт для тестирования всех Docker контейнеров

echo "=== ТЕСТИРОВАНИЕ DOCKER КОНТЕЙНЕРОВ ==="
echo

# Функция для тестирования сборки
test_build() {
    local service_name=$1
    local dockerfile_path=$2
    
    echo "Сборка $service_name..."
    if docker build -t $service_name $dockerfile_path; then
        echo "✅ $service_name успешно собран"
    else
        echo "❌ Ошибка сборки $service_name"
    fi
    echo
}

# Функция для тестирования запуска
test_run() {
    local service_name=$1
    local run_command=$2
    
    echo "Тестирование запуска $service_name..."
    echo "Команда: $run_command"
    echo "Примечание: Для интерактивных приложений используйте -it флаг"
    echo
}

echo "1. СБОРКА ВСЕХ ОБРАЗОВ"
echo "======================"

test_build "java-calculator" "./calc-java"
test_build "python-calculator" "./calc-py"
test_build "dart-calculator" "./dart-calc"
test_build "java-game" "./game-java"
test_build "python-rps-game" "./rpsgame-py"
test_build "nginx-website" "./site"

echo "2. КОМАНДЫ ДЛЯ ЗАПУСКА"
echo "====================="

test_run "Java калькулятор" "docker run -it java-calculator"
test_run "Python калькулятор" "docker run -it python-calculator"
test_run "Dart калькулятор" "docker run -it dart-calculator"
test_run "Java игра" "docker run -it java-game"
test_run "Python игра" "docker run -it python-rps-game"
test_run "Веб-сайт" "docker run -p 8080:80 nginx-website"

echo "3. DOCKER COMPOSE"
echo "================="
echo "Для запуска всех сервисов:"
echo "docker-compose up --build"
echo
echo "Для запуска в фоновом режиме:"
echo "docker-compose up -d --build"
echo
echo "Для остановки:"
echo "docker-compose down"
echo

echo "4. ПОЛЕЗНЫЕ КОМАНДЫ"
echo "==================="
echo "Просмотр образов:"
echo "docker images"
echo
echo "Просмотр контейнеров:"
echo "docker ps -a"
echo
echo "Удаление всех остановленных контейнеров:"
echo "docker container prune"
echo
echo "Удаление неиспользуемых образов:"
echo "docker image prune -a"
echo
echo "Очистка всей системы Docker:"
echo "docker system prune -a"
echo

echo "=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ==="
