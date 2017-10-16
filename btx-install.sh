#!/bin/bash
echo "Устанавливаем модуль..."
pip3 install bs4
sleep 2
echo "Создаем директорию..."
sleep 2
mkdir /usr/local/bin/btcc
echo "Копируем скрипт..."
sleep 2
cp btc-c.py /usr/local/bin/btcc 
echo "Колдуем..."
sleep 2
cp btx /usr/local/bin
chmod +x btx
echo "Готово! Введите в терминале "btx" "


