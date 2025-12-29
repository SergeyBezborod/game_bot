from navigation import *


def farm_sub_loc(location_name, delay, personage, event):
    if personage == 1:
        event.wait()
        mouse_click(1370, 540)
        mouse_click(1425, 485)
        alt_click(1150, 375)
        mouse_click(1315, 540)
        press_keyboard_button('1')
        sleeper(2, "Набор очков")
        mouse_click(1370, 540)
        mouse_click(1425, 365)
        event.wait()

        index = 0
        while index < 30:
            alt_click(1150, 375)
            time.sleep(0.20)
            shift_click(1150, 525)
            time.sleep(0.20)
            if index > 15:
                if find_stone():
                    break
            index = index + 1
            event.wait()

        event.wait()
        mouse_click(1315, 540)
        press_keyboard_button('1')
        mouse_position(1240, 540)
        event.wait()

        index1 = 0
        while index1 < 20:
            press_keyboard_button('q')
            time.sleep(0.25)
            if validate_fight():
                break
            else:
                index1 = index1 + 1
        event.wait()

        sleeper(2, "Резервное время")
        if not validate_fight():
            if delay >= 20:
                mouse_click(1255, 40)
                sleeper(1, "Выбор врага")
                press_keyboard_button('w')
                sleeper(4, "Пробная комбинация")
                press_keyboard_button('a')
                sleeper(2, "Прыжковый манёвр")
                press_keyboard_button('s')
                sleeper(2, 'Метка теней')
                press_keyboard_button('d')
                sleeper(2, 'Коварный укол')
                press_keyboard_button('3')
                sleeper(2, "Быстрее ветра")

            for delay_i in range(0, delay):
                if validate_fight():
                    break
                else:
                    sleeper(1, f"Авто-атаки добивают остатки в '{location_name}'")
        event.wait()
    use_exit_stone(location_name)


def farm_loc(loc_name, n_lvl, delay, personage, event):
    loc_t_start = time.time()
    if n_lvl == "1_lvl":
        event.wait()
        farm_sub_loc(loc_name, delay, personage, event)
        event.wait()
    elif n_lvl == "2_lvl":
        farm_sub_loc(loc_name, delay, personage, event)
        event.wait()
        farm_sub_loc(loc_name, delay, personage, event)
        event.wait()
    elif n_lvl == "3_lvl":
        event.wait()
        farm_sub_loc(loc_name, delay, personage, event)
        event.wait()
        farm_sub_loc(loc_name, delay, personage, event)
        event.wait()
        farm_sub_loc(loc_name, delay, personage, event)
        event.wait()
    loc_t_finish = time.time()
    loc_t = loc_t_finish - loc_t_start
    logging(f"Время локации: {int(loc_t // 3600)}ч {int((loc_t // 60) % 60)}м {int(loc_t % 60)}c")
