import os
import time
import cv2
from main_data import *

# Кеш изображений
template_cache = {}


def logging(text: str):
    """Логирование в файл и консоль"""
    time_now = time.ctime()
    file = open('logs/bot_log.txt', 'a')
    file.writelines(time_now + ": " + text + "\n")
    print(f"{time_now}: {text}")


def sleeper(seconds: int, text: str):
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

        logging(f"Загрузка изображений из папки: {folder}")

        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith('.png'):
                    full_path = str(os.path.join(root, file))
                    try:
                        img = cv2.imread(full_path, cv2.IMREAD_COLOR)
                        if img is not None:
                            template_cache[full_path] = img
                            logging(f"'{file}' загружена в кеш")
                        else:
                            logging(f"Ошибка загрузки '{file}'")
                    except Exception as e:
                        logging(f"Ошибка при обработке '{file}' - {str(e)}")
