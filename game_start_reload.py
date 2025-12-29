from validation import *
from main_data import *
from controller import *
import sys


def start_game(personage):
    os.startfile(r'C:/Program Files (x86)/Overkings/Overkings/Overkings.exe')
    print(time.ctime() + ": Overkings запущен")
    logging(time.ctime() + ": Overkings запущен")
    sleeper(6, 'Ждем запуска игры')
    if validate_image("run_data/start_game.png", 460, 25, 1000, 940, 0.9):
        mouse_click(960, 550)
        sleeper(6, "Переход к выбору героев")
        mouse_click(personages[personage][0], personages[personage][1])
        mouse_click(1030, 624)
        logging(f"Произведён вход в учетную запись, выбран '{personages[personage][2]}'")
        sleeper(8, "Ждем прогруза в игру")
        entry = locate_image("run_data/game_events_log.png", 460, 25, 1000, 940, 0.95)
        if len(entry) > 0:
            mouse_click(entry[0][0] + 462, entry[0][1] + 27)

    else:
        logging("Оверкингс не запущен")
        screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        screenshot.save(r"logs/debug_screenshots/start_game_debug.png")
        mouse_click(1895, 10)
        sys.exit()


def reload_game(personage):
    sleeper(1, "Перезапуск игры")
    mouse_click(1895, 10)
    logging("Overkings закрыт")
    sleeper(2, 'Подготовка к запуску игры')
    start_game(personage)
