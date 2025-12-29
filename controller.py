import time
import keyboard
import pyautogui
from pynput.mouse import Button, Controller

mouse = Controller()


def cursor_location():
    """Вывод позиции курсора (отладочная функция)"""
    while True:
        print(pyautogui.position())


def mouse_position(x, y):
    time.sleep(0.25)
    mouse.position = (x, y)
    time.sleep(0.25)


def mouse_click(x, y):
    time.sleep(0.25)
    mouse.position = (x, y)
    time.sleep(0.25)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)


def mouse_doubleclick(x, y):
    time.sleep(0.25)
    mouse.position = (x, y)
    time.sleep(0.25)
    mouse.press(Button.left)
    time.sleep(0.25)
    mouse.release(Button.left)
    time.sleep(0.25)
    mouse.press(Button.left)
    time.sleep(0.25)
    mouse.release(Button.left)
    time.sleep(0.25)


def press_keyboard_button(key):
    time.sleep(0.25)
    keyboard.send(key)
    time.sleep(0.25)


def shift_press_button(key):
    pyautogui.keyDown('shift')
    keyboard.send(key)
    pyautogui.keyUp('shift')


def shift_click(x, y):
    pyautogui.keyDown('shift')
    pyautogui.click(x, y)
    pyautogui.keyUp('shift')


def alt_click(x, y):
    pyautogui.keyDown('alt')
    pyautogui.click(x, y)
    pyautogui.keyUp('alt')


def mouse_click_to_item(x, y):
    time.sleep(0.05)
    mouse.position = (x, y)
    time.sleep(0.05)
    mouse.press(Button.left)
    time.sleep(0.05)
    mouse.release(Button.left)


def mouse_doubleclick_to_item(x, y):
    time.sleep(0.05)
    mouse.position = (x, y)
    time.sleep(0.05)
    mouse.press(Button.left)
    time.sleep(0.05)
    mouse.release(Button.left)
    time.sleep(0.05)
    mouse.press(Button.left)
    time.sleep(0.05)
    mouse.release(Button.left)
    time.sleep(0.05)

def mouse_click_and_doubleclick_to_item(x, y):
    mouse_click_to_item(x, y)
    mouse_doubleclick_to_item(x, y)
