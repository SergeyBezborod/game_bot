import numpy
from utils import *
import pyautogui
from typing import Optional, Tuple


def load_and_process_image(pic_path: str, x: int, y: int, w: int, h: int) -> Tuple[Optional[numpy.ndarray], Optional[numpy.ndarray]]:
    """
    Вспомогательная функция для загрузки и обработки

    Args:
        pic_path: Путь к искомому изображению
        x: Координата x для начала построения области
        y: Координата y для начала построения области
        w: Ширина для построения области
        h: Высота для построения области
    
    Returns:
        Tuple: 2 объекта или None, None
            template: шаблон изображения
            screenshot: скриншот экрана
    """
    if pic_path in template_cache:
        template = template_cache[pic_path]
    else:
        template = cv2.imread(pic_path, cv2.IMREAD_COLOR)
        if template is not None:
            template_cache[pic_path] = template

    if template is None:
        return None, None

    try:
        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)
        return template, screenshot
    except Exception as e:
        logging(f"Ошибка при захвате экрана - {str(e)}")
        return None, None


def validate_image(pic_path: str, x: int, y: int, w: int, h: int, threshold: float) -> bool:
    """
    Поиск изображения на указанной области экрана с указанной точностью (возвращает bool)

    Args:
        pic_path: Путь к искомому изображению
        x: Координата x для начала построения области
        y: Координата y для начала построения области
        w: Ширина для построения области
        h: Высота для построения области
        threshold: Пороговое значение совпадения (0.0-1.0)

    Returns:
        bool: True если изображение найдено
    """
    try:
        template, screenshot = load_and_process_image(pic_path, x, y, w, h)

        if template is None or screenshot is None:
            logging(f"Ошибка: не удалось загрузить '{pic_path}'")
            return False

        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)

        return max_val >= threshold

    except Exception as e:
        logging(f"Ошибка обработки '{pic_path}' - {str(e)}")
        return False


def locate_image(pic_path: str, x: int, y: int, w: int, h: int, threshold: float) -> list:
    """
    Поиск изображения на указанной области экрана с указанной точностью (возвращает координаты)

    Args:
        pic_path: Путь к искомому изображению
        x: Координата x для начала построения области
        y: Координата y для начала построения области
        w: Ширина для построения области
        h: Высота для построения области
        threshold: Пороговое значение совпадения (0.0-1.0)

    Returns:
        list: координаты найденного изображения на экране
    """
    locations = []
    try:
        template, screenshot = load_and_process_image(pic_path, x, y, w, h)

        if template is None or screenshot is None:
            logging(f"Ошибка: не удалось загрузить '{pic_path}'")
            return locations

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        for loc_y, loc_x in zip(*numpy.where(result >= threshold)):
            locations.append((int(loc_x), int(loc_y)))
        return locations

    except Exception as e:
        logging(f"Ошибка обработки '{pic_path}' - {str(e)}")
        return locations


def locate_item(pic_path: str, item_name: str, bag: str, x: int, y: int, w: int, h: int) -> list:
    """
    Поиск изображений предметов на указанной области экрана (возвращает координаты)

    Args:
        pic_path: Путь к искомому изображению
        item_name: Название предмета для поиска
        bag: Название сумки
        x: Координата x для начала построения области
        y: Координата y для начала построения области
        w: Ширина для построения области
        h: Высота для построения области

    Returns:
        list: координаты найденного изображения на экране
    """
    time.sleep(0.5)
    locations = locate_image(pic_path, x, y, w, h, 0.9)
    if len(locations) > 0:
        logging(f"Предмет '{item_name}' обнаружен в '{bag}'")
    else:
        logging(f"Предмет '{item_name}' НЕ обнаружен в '{bag}'")
    return locations


def validate_teleportation(pic_path: str, city_name: str, reg_name: str) -> bool:
    """
    Проверка телепортации в целевой регион с указанной точностью (возвращает bool)

    Args:
        pic_path: Путь к исходному изображению
        city_name: Название города
        reg_name: Название региона

    Returns:
         bool: True, если телепортация в нужный регион успешна
    """
    time.sleep(0.5)
    if validate_image(pic_path, 460, 25, 1000, 940, 0.9):
        logging(f"Персонаж перемещён в '{city_name}, '{reg_name}'")
        return True
    else:
        logging(f"Персонаж НЕ перемещён в '{city_name}, '{reg_name}'")
        screenshot = pyautogui.screenshot(region=(460, 25, 1000, 940))
        screenshot.save(rf"logs/debug_screenshots/teleport_debug.png")
        return False


def validate_fight() -> bool:
    """
    Проверка состояния боя с указанной точностью (возвращает bool)

    Returns:
         bool: True, если найден маркер окончания боя
    """
    if validate_image("run_data/out_fight_marker_1.png", 460, 25, 1000, 940, 0.99):
        print(f"{time.ctime()}: Бой закончен")
        return True
    else:
        return False
