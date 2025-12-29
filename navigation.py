from validation import *
from utils import *
from controller import *


def detect_current_region() -> str:
    """
    Определяет текущий регион по маркерам на экране.
    
    Returns:
        Название региона или пустая строка.
    """
    for i in range(0, len(current_region_markers)):
        if validate_image(current_region_markers[i], 460, 25, 1000, 940, 0.98):
            logging(f"Найден '{current_region_markers[i]}'")
            return current_region_markers[i]
        else:
            logging(f"Не удалось определить текущее местоположение персонажа")
            return ""


def move_map(map_x: int, map_y: int):
    """
    Перемещает карту в нужные координаты.

    Args:
        map_x, map_y: Координаты карты
    """
    sleeper(1, "Подготовка")
    mouse_click(map_x, map_y)
    logging(f"Карта перемещена, координаты: х={map_x}, y={map_y}")


def move_to_loc(loc_x: int, loc_y: int, loc_name: str, delay: int, picture_to_validate: str) -> bool:
    """
    Перемещает персонажа к локации и проверяет успешность перемещения.
    
    Args:
        loc_x, loc_y: Координаты локации
        loc_name: Название локации
        delay: Максимальное время ожидания (секунды)
        picture_to_validate: Изображение для валидации успешного перемещения
    
    Returns:
        True если перемещение успешно, иначе False
    """
    try:
        mouse_position(loc_x, loc_y)
        time.sleep(0.5)
        mouse_doubleclick(loc_x, loc_y)
        for time_index in range(delay):
            if validate_image(picture_to_validate, 460, 25, 1000, 940, 0.965):
                time.sleep(0.5)
                logging(f"Персонаж у '{loc_name}'. Обнаружена '{picture_to_validate}'")
                return True
            else:
                sleeper(1, "Ожидание")
        logging(f"Не удалось переместиться к локации '{loc_name}' за '{delay}' секунд")
        return False
    except Exception as e:
        logging(f"Ошибка при перемещении '{loc_name}' - {str(e)}")
        return False


def open_loc(loc_x: int, loc_y: int, loc_name: str) -> bool:
    """
    Открывает локацию для фарма.
    
    Args:
        loc_x, loc_y: Координаты локации
        loc_name: Название локации
    
    Returns:
        True если локация открыта успешно, иначе False
    """
    try:
        mouse_click(loc_x, loc_y)
        sleeper(1, "Подготовка")
        entry = locate_image("run_data/open_location_marker.png", 460, 25, 1000, 940, 0.965)
        if len(entry) > 0:
            logging(f"Выбор сложности для локации '{loc_name}'")
            mouse_click(entry[0][0] + 462, entry[0][1] + 27)

            for time_index in range(5):
                if validate_image("run_data/health_bar.png", 460, 25, 1000, 940, 0.965):
                    logging(f"Персонаж в '{loc_name}. Обнаружена 'run_data/health_bar.png'")
                    return True
                else:
                    sleeper(1, "Ожидание")
        else:
            screenshot = pyautogui.screenshot(region=(460, 25, 1000, 940))
            screenshot.save(rf"logs/debug_screenshots/open_loc_debug.png")
            logging(f"Не открыт выбор сложности для '{loc_name}'. "
                    f"Скрин 'logs/debug_screenshots/open_loc_debug.png'")
            return False
    except Exception as e:
        logging(f"Ошибка при открытии локации '{loc_name}' - {str(e)}")
        return False



def use_exit_stone(loc_name: str) -> bool:
    """
    Использование камня перехода.

    Args:
        loc_name: имя локации

    Returns:
        bool:
            true если камень использован
    """
    try:
        for times in range(15):
            mouse_click(1150, 375)
            sleeper(1, "Перемещение до камня")
            if find_stone() and validate_fight():
                break

        for stone in enter_exit_stones:
            entry3 = locate_image(stone, 460, 25, 1000, 940, 0.9)
            if len(entry3) > 0:
                logging(f"Пройден этап '{loc_name}', найден '{stone}'. Переход")
                mouse_click(entry3[0][0] + 462, entry3[0][1] + 27)
                sleeper(4, "Перемещение")
                return True
        logging(f"Ни один камень не найден в '{loc_name}'")
        return False
    except Exception as e:
        logging(f"Ошибка использования камня в '{loc_name}' - {str(e)}")
        return False


def find_stone() -> bool:
    try:
        for stone in range(0, len(enter_exit_stones)-8):
            if validate_image(enter_exit_stones[stone], 460, 25, 1000, 940, 0.9):
                logging(f"Переход к бою. Обнаружен '{enter_exit_stones[stone]}'")
                return True

        logging(f"Ни один камень не обнаружен")
        return False
    except Exception as e:
        logging(f"Ошибка при поиске камней {str(e)}")
        return False


def bank_enter(bank_x: int, bank_y: int, bank_name: str, run_time: int, btn_x: int, btn_y: int) -> bool:
    """
    Вход в магазин 

    Args:
        bank_x, bank_y: координаты банка
        bank_name: название банка
        run_time: время перехода в банка (sec)
        btn_x, btn_y: координаты кнопки входа (0 или координата)

    Returns:
        bool:
            true если вход в банк прошел успешно
    """
    try:
        mouse_doubleclick(bank_x, bank_y)
        sleeper(run_time, f"Перемещение до '{bank_name}'")
        mouse_doubleclick(bank_x, bank_y)
        sleeper(1, "Ожидание")
        mouse_click(btn_x, btn_y)

        for time_index in range(10):
            if validate_image('run_data/is_enter_bank.png', 460, 25, 1000, 940, 0.9):
                logging(f"'{bank_name}' загружен")
                return True
            else:
                sleeper(1, f"Загрузка в '{bank_name}'")
        logging(f"Не удалось загрузить '{bank_name}' за 10 секунд")
        return False
    except Exception as e:
        logging(f"Ошибка входа на банк '{bank_name}' - {str(e)}")
        return False


def store_enter(store_x: int, store_y: int, store_name: str, run_time: int, btn_x: int, btn_y: int, map_x: int, map_y: int) -> bool:
    """
    Вход в магазин 

    Args:
        store_x, store_y: координаты магазина
        store_name: название магазина
        run_time: время перехода в магазин (sec)
        btn_x, btn_y: координаты кнопки входа (0 или координата)
        map_x, map_y: координаты для смещения камеры (0 или координата)

    Returns:
        bool:
            true если вход в магазин прошел успешно
    """
    try:
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

        logging(f"Не удалось загрузить '{store_name}' за 10 секунд")
        return False
    except Exception as e:
        logging(f"Ошибка входа в магазин '{store_name}' - {str(e)}")
        return False


def k_bank_enter() -> bool:
    """Вход в банк 'Банкъ Гроггенброггъ'."""
    try:
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

        logging(f"Не удалось загрузить 'Банкъ Гроггенброггъ' за 10 секунд")
        return False
    except Exception as e:
        logging(f"Ошибка входа в 'Банкъ Гроггенброггъ' - {str(e)}")
        return False


def k_store_enter() -> bool:
    """Вход в магазин 'Лавка Легкость бытия'."""
    try:
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

        logging(f"Не удалось загрузить 'Лавка Легкость бытия' за 10 секунд")
        return False
    except Exception as e:
        logging(f"Ошибка входа в 'Лавка Легкость бытия' - {str(e)}")
        return False
