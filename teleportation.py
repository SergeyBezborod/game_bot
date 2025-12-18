from validation import *
from controller import *


def s_reg_tp(city_x, city_y, s_reg_x, s_reg_y, city_name, s_reg_name, pic_path):
    """Телепортация в безопасный регион и проверка её успешности (возвращает bool)"""
    mouse_click(1370, 540)
    press_keyboard_button('x')
    
    if city_x != 0 and city_y != 0:
        mouse_click(1185, 425)
        mouse_click(city_x, city_y)

    mouse_click(s_reg_x, s_reg_y)
    mouse_click(800, 640)
    sleeper(1, "Подготовка")

    for time_index in range(10):
        if validate_teleportation(pic_path, city_name, s_reg_name):
            return True
        else:
            sleeper(1, "Ожидание")
    return False


def f_reg_tp(f_reg_x, f_reg_y, city_name, f_reg_name, pic_path):
    """Телепортация в регион фарма и проверка её успешности (возвращает bool)"""
    mouse_click(1370, 540)
    press_keyboard_button('x')
    
    mouse_click(f_reg_x, f_reg_y)
    mouse_click(850, 640)
    sleeper(1, "Подготовка")
    
    for time_index in range(10):
        if validate_teleportation(pic_path, city_name, f_reg_name):
            return True
        else:
            sleeper(1, "Ожидание")
    return False


def k_city_tp():
    """Телепортация в Конхобар и проверка её успешности (возвращает bool)"""
    mouse_click(1370, 540)
    press_keyboard_button('x')

    mouse_click(1185, 425)
    mouse_doubleclick(1185, 465)
    mouse_click(1085, 525)
    mouse_click(800, 415)
    mouse_click(800, 640)
    sleeper(1, "Подготовка")

    for time_index in range(10):
        if validate_teleportation("run_data/konhobar_gorod.png", "Конхобар", "город Конхобар"):
            return True
        else:
            sleeper(1, "Ожидание")
    return False
