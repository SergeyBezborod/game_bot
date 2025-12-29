import threading

from bot import *

# Глобальные события
pause_event = threading.Event()  # Установлен = пауза снята
pause_event.set()  # Изначально пауза снята
stop_event = threading.Event()


def monitoring():
    """Мониторинг экрана на наличие маркеров установки паузы (работает в отдельном потоке)"""
    while not stop_event.is_set():
        try:
            marker_found = False

            for marker_path, message, x, y, w, h in pause_markers:
                if validate_image(marker_path, x, y, w, h, 0.95):
                    if pause_event.is_set():
                        print(message)
                        pause_event.clear()
                    marker_found = True
                    sleeper(60, "Ожидание")
                    reload_game(1)
                    break

            if not marker_found and not pause_event.is_set():
                print("Маркеры паузы не обнаружены, пауза скоро снимется")
                sleeper(10, "Пауза снимется через")
                pause_event.set()

        except Exception as e:
            print(f"Ошибка в мониторинге: {e}")

        time.sleep(0.5)


def farming():
    """Основная логика фарма"""
    while not stop_event.is_set():
        pause_event.wait()

        if stop_event.is_set():
            break

        pers_fact = 2 - 1

        time_index = 1
        while time_index <= 100:
            logging(f"Круг №{time_index}")
            global_run_and_farm(pers_fact, pause_event)
            time_index = time_index + 1

        if stop_event.is_set():
            break
        time.sleep(1)


def main():
    preload_images()

    monitor_thread = threading.Thread(target=monitoring, daemon=True)
    farm_thread = threading.Thread(target=farming, daemon=True)

    monitor_thread.start()
    farm_thread.start()

    try:
        while monitor_thread.is_alive() and farm_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        pause_event.set()
        monitor_thread.join(2.0)
        farm_thread.join(2.0)

        logging(f"Потоки остановлены вручную")


if __name__ == "__main__":
    main()
