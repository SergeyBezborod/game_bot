from validation import *
from utils import *
from controller import *


def detect_current_region():
    for i in range(0, len(current_region_markers)):
        if validate_image(current_region_markers[i], 460, 25, 1000, 940, 0.98):
            print(f"{time.ctime()}: Найден '{current_region_markers[i]}'")
            break
        else:
            print(f"{time.ctime()}: Ничего не найдено")


def move_map(map_x, map_y):
    sleeper(1, "Подготовка")
    mouse_click(map_x, map_y)
    print(f"{time.ctime()}: Карта перемещена, координаты: х={map_x}, y={map_y}")
    logging(f"Карта перемещена, координаты: х={map_x}, y={map_y}")


def move_to_loc(loc_x, loc_y, loc_name, delay, picture_to_validate):
    mouse_position(loc_x, loc_y)
    time.sleep(0.5)
    mouse_doubleclick(loc_x, loc_y)
    for time_index in range(delay):
        if validate_image(picture_to_validate, 460, 25, 1000, 940, 0.965):
            print(f"{time.ctime()}: Персонаж у '{loc_name}'. Обнаружена '{picture_to_validate}'")
            time.sleep(0.5)
            logging(f"Персонаж у '{loc_name}'. Обнаружена '{picture_to_validate}'")
            return True
        else:
            sleeper(1, "Ожидание")
    return False


def open_loc(loc_x, loc_y, loc_name):
    mouse_click(loc_x, loc_y)
    sleeper(1, "Подготовка")
    entry = locate_image("run_data/open_location_marker.png", 460, 25, 1000, 940, 0.965)
    if len(entry) > 0:
        print(f"{time.ctime()}: Выбор сложности для локации '{loc_name}'")
        logging(f"Выбор сложности для локации '{loc_name}'")
        mouse_click(entry[0][0] + 462, entry[0][1] + 27)

        for time_index in range(5):
            if validate_image("run_data/health_bar.png", 460, 25, 1000, 940, 0.965):
                print(f"{time.ctime()}: Персонаж в '{loc_name}. Обнаружена 'run_data/health_bar.png'")
                logging(f"Персонаж в '{loc_name}. Обнаружена 'run_data/health_bar.png'")
                return True
            else:
                sleeper(1, "Ожидание")
    else:
        screenshot = pyautogui.screenshot(region=(460, 25, 1000, 940))
        screenshot.save(rf"logs/debug_screenshots/open_loc_debug.png")
        print(f"{time.ctime()}: Не открыт выбор сложности для '{loc_name}'. "
              f"Скрин 'logs/debug_screenshots/open_loc_debug.png'")
        logging(f"Не открыт выбор сложности для '{loc_name}'. "
                f"Скрин 'logs/debug_screenshots/open_loc_debug.png'")
    return False


def use_exit_stone(loc_name):
    for times in range(15):
        mouse_click(1150, 375)
        sleeper(1, "Перемещение до камня")
        if find_stone() and validate_fight():
            break

    for stone in enter_exit_stones:
        entry3 = locate_image(stone, 460, 25, 1000, 940, 0.9)
        if len(entry3) > 0:
            print(f"{time.ctime()}: Пройден этап '{loc_name}', найден '{stone}'. Переход")
            logging(f"Пройден этап '{loc_name}', найден '{stone}'. Переход")
            mouse_click(entry3[0][0] + 462, entry3[0][1] + 27)
            sleeper(4, "Перемещение")
            return True
    return False


def find_stone():
    for stone in range(0, len(enter_exit_stones)-8):
        if validate_image(enter_exit_stones[stone], 460, 25, 1000, 940, 0.9):
            print(f"{time.ctime()}: Переход к бою, '{enter_exit_stones[stone]}' обнаружен")
            logging(f"Переход к бою. Обнаружен '{enter_exit_stones[stone]}'")
            return True

    print(f"{time.ctime()}: Ни один камень не обнаружен")
    logging(f"Ни один камень не обнаружен")
    return False


def bank_enter(bank_x, bank_y, bank_name, run_time, btn_x, btn_y):
    mouse_doubleclick(bank_x, bank_y)
    sleeper(run_time, f"Перемещение до '{bank_name}'")
    mouse_doubleclick(bank_x, bank_y)
    sleeper(1, "Ожидание")
    mouse_click(btn_x, btn_y)

    for time_index in range(10):
        if validate_image('run_data/is_enter_bank.png', 460, 25, 1000, 940, 0.9):
            print(f"{time.ctime()}: '{bank_name}' загружен")
            logging(f"'{bank_name}' загружен")
            return True
        else:
            sleeper(1, f"Загрузка в '{bank_name}'")
    print(f"{time.ctime()}: Не удалось загрузить '{bank_name}' за 10 секунд")
    logging(f"Не удалось загрузить '{bank_name}' за 10 секунд")
    return False


def store_enter(store_x, store_y, store_name, run_time, btn_x, btn_y, map_x, map_y):
    if map_x != 0 and map_y != 0:
        move_map(map_x, map_y)

    mouse_doubleclick(store_x, store_y)
    sleeper(run_time, f"Перемещение в '{store_name}'")
    mouse_doubleclick(store_x, store_y)
    if btn_x != 0 and btn_y != 0:
        mouse_click(btn_x, btn_y)

    for time_index in range(10):
        if validate_image('run_data/is_enter_store.png', 460, 25, 1000, 940, 0.9):
            print(f"{time.ctime()}: '{store_name}' загружен")
            return True
        else:
            sleeper(1, f"Загрузка в '{store_name}'")

    print(f"{time.ctime()}: Не удалось загрузить '{store_name}' за 10 секунд")
    logging(f"Не удалось загрузить '{store_name}' за 10 секунд")
    return False


def k_bank_enter():
    move_map(1375, 135)
    mouse_doubleclick(930, 240)
    sleeper(4, "Персонаж идет до банка")
    mouse_doubleclick(930, 240)

    for time_index in range(10):
        if validate_image('run_data/is_enter_bank.png', 460, 25, 1000, 940, 0.9):
            print(f"{time.ctime()}: 'Банкъ Гроггенброггъ' загружен")
            return True
        else:
            sleeper(1, f"Загрузка в 'Банкъ Гроггенброггъ'")

    print(f"{time.ctime()}: Не удалось загрузить 'Банкъ Гроггенброггъ' за 10 секунд")
    logging(f"Не удалось загрузить 'Банкъ Гроггенброггъ' за 10 секунд")
    return False


def k_store_enter():
    move_map(1382, 133)
    mouse_doubleclick(965, 264)
    sleeper(4, "Персонаж идет до магазина")
    mouse_doubleclick(965, 264)

    for time_index in range(10):
        if validate_image('run_data/is_enter_store.png', 460, 25, 1000, 940, 0.9):
            print(f"{time.ctime()}: 'Лавка Легкость бытия' загружен")
            return True
        else:
            sleeper(1, f"Загрузка в 'Лавка Легкость бытия'")

    print(f"{time.ctime()}: Не удалось загрузить 'Лавка Легкость бытия' за 10 секунд")
    logging(f"Не удалось загрузить 'Лавка Легкость бытия' за 10 секунд")
    return False
