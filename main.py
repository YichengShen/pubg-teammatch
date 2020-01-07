#把模拟器放在左上角
import pyautogui
import random
import time

screen_size = pyautogui.size()
width, height = screen_size


def click_start():
    x = random.randint(50,200)
    y = random.randint(65,120)
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click(x, y)
    print("已点击开始")
    return

def click_ok():
    pyautogui.moveTo(620, 750, duration=1)
    for _ in range(5):
        pyautogui.click(620, 750)
        print("已点击Ok")
        time.sleep(1)
    return

def click_continue():
    pyautogui.moveTo(1100, 830, duration=1)
    for _ in range(2):
        pyautogui.click(1100, 830)
        print("已点击Continue")
        time.sleep(3)
    return


def loop():
    while True:
        click_ok()
        time.sleep(2)
        click_start()
        time.sleep(560)
        click_continue()
        time.sleep(10)
    return


loop()
