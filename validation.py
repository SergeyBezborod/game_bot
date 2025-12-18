import numpy
from utils import *
import pyautogui


def validate_image(pic_path, x, y, w, h, threshold):
    """Поиск изображения на указанной области экрана с указанной точностью (возвращает bool)"""
    try:
        if pic_path in template_cache:
            template = template_cache[pic_path]
        else:
            template = cv2.imread(pic_path, cv2.IMREAD_COLOR)
            template_cache[pic_path] = template

        if template is None:
            print(f"Ошибка: не удалось загрузить '{pic_path}'")
            logging(f"Ошибка: не удалось загрузить '{pic_path}'")
            return False

        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)

        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)

        if max_val >= threshold:
            # print(str(max_val) + "/" + str(threshold))
            # logging(f"{pic_path} найден с трешхолдом {max_val}/{threshold}")
            return True
        else:
            # print(str(max_val) + "/" + str(threshold))
            # logging(f"{pic_path} найден с трешхолдом {max_val}/{threshold}")
            return False

    except Exception as e:
        print(f"{time.ctime()}: Ошибка обработки '{pic_path}' - {str(e)}")
        logging(f"Ошибка обработки '{pic_path}' - {str(e)}")
        return False


def locate_image(pic_path, x, y, w, h, threshold):
    """Поиск изображения на указанной области экрана с указанной точностью (возвращает координаты)"""
    try:
        if pic_path in template_cache:
            image_to_find = template_cache[pic_path]
        else:
            image_to_find = cv2.imread(pic_path, cv2.IMREAD_COLOR)
            template_cache[pic_path] = image_to_find

        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(screenshot, image_to_find, cv2.TM_CCOEFF_NORMED)

        locations = []

        for y, x in zip(*numpy.where(result >= threshold)):
            locations.append((int(x), int(y)))
        return locations

    except Exception as e:
        print(f"{time.ctime()}: Ошибка обработки '{pic_path}' - {str(e)}")
        logging(f"Ошибка обработки '{pic_path}' - {str(e)}")
        return []


def locate_item(pic_path, item_name, bag, x, y, w, h):
    """Поиск изображений предметов на указанной области экрана с указанной точностью (возвращает координаты)"""
    time.sleep(0.5)
    locations = locate_image(pic_path, x, y, w, h, 0.9)
    if len(locations) > 0:
        print(f"{time.ctime()}: Предмет '{item_name}' обнаружен в '{bag}'")
        logging(f"Предмет '{item_name}' обнаружен в '{bag}'")
    else:
        print(f"{time.ctime()}: Предмет '{item_name}' НЕ обнаружен в '{bag}'")
        logging(f"Предмет '{item_name}' НЕ обнаружен в '{bag}'")
    return locations


def validate_teleportation(pic_path, city_name, reg_name):
    """Проверка телепортации в целевой регион с указанной точностью (возвращает bool)"""
    time.sleep(0.5)
    if validate_image(pic_path, 460, 25, 1000, 940, 0.9):
        print(f"{time.ctime()}: Персонаж перемещён в '{city_name}, '{reg_name}'")
        logging(f"Персонаж перемещён в '{city_name}, '{reg_name}'")
        return True
    else:
        print(f"{time.ctime()}: Персонаж НЕ перемещён в '{city_name}, '{reg_name}'")
        logging(f"Персонаж НЕ перемещён в '{city_name}, '{reg_name}'")
        screenshot = pyautogui.screenshot(region=(460, 25, 1000, 940))
        screenshot.save(rf"logs/debug_screenshots/teleport_debug.png")
        return False


def validate_fight():
    """Проверка состояния боя с указанной точностью (возвращает bool)"""
    if validate_image("run_data/out_fight_marker_1.png", 460, 25, 1000, 940, 0.99):
        print(f"{time.ctime()}: Бой закончен")
        return True
    else:
        print(f"{time.ctime()}: Бой НЕ закончен")
        return False
