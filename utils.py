import os
import time
import cv2
from main_data import *

# Кеш изображений
template_cache = {}


def logging(text):
    """Логирование в файл"""
    file = open('logs/bot_log.txt', 'a')
    file.writelines(time.ctime() + ": " + text + "\n")


def sleeper(seconds, text):
    """Ожидание выполнения какого-то действия с таймером"""
    for second in range(seconds):
        time.sleep(1)
        print(f"{time.ctime()}: {text}... {second + 1}/{seconds}")


def preload_images():
    """Загрузка всех изображений из указанных папок в кеш"""
    for folder in folders_to_cache:
        if not os.path.exists(folder):
            print(f"{time.ctime()}: Папка '{folder}' не найдена")
            continue

        print(f"{time.ctime()}: Загрузка изображений из папки: {folder}")

        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith('.png'):
                    full_path = str(os.path.join(root, file))
                    try:
                        img = cv2.imread(full_path, cv2.IMREAD_COLOR)
                        if img is not None:
                            template_cache[full_path] = img
                            print(f"{time.ctime()}: '{file}' загружена в кеш")
                        else:
                            print(f"{time.ctime()}: Ошибка загрузки '{file}'")
                    except Exception as e:
                        print(f"{time.ctime()}: Ошибка при обработке '{file}' - {str(e)}")
