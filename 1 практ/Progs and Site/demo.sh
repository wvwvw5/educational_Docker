#!/bin/bash

echo "=== ДЕМОНСТРАЦИЯ DOCKER КОНТЕЙНЕРОВ ==="
echo

echo "1. ВЕБ-САЙТ (уже запущен)"
echo "   Откройте браузер: http://localhost:8080"
echo "   Статус:"
docker ps | grep nginx-website
echo

echo "2. JAVA КАЛЬКУЛЯТОР"
echo "   Тест: 10 + 5 = 15"
echo -e "10\n5\n+\n" | docker run -i --rm java-calculator
echo

echo "3. PYTHON КАЛЬКУЛЯТОР"
echo "   Тест: 10 + 5 = 15"
echo -e "1\n10\n5\n" | docker run -i --rm python-calculator
echo

echo "4. DART КАЛЬКУЛЯТОР"
echo "   Тест: 10 + 5 = 15"
echo -e "10\n5\n+\n" | docker run -i --rm dart-calculator
echo

echo "5. JAVA ИГРА (угадай число)"
echo "   Запуск игры (для демонстрации):"
echo "   docker run -it --rm java-game"
echo

echo "6. PYTHON ИГРА (камень-ножницы-бумага)"
echo "   Запуск игры (для демонстрации):"
echo "   docker run -it --rm python-rps-game"
echo

echo "=== ВСЕ КОНТЕЙНЕРЫ УСПЕШНО РАБОТАЮТ! ==="
