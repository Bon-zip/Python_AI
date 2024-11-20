from pyautogui import*
import pyautogui
import time
import keyboard
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) 
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    
def piano_auto():
    while not keyboard.is_pressed('q'):
        if pyautogui.pixel(373, 512)[0] == 0:
            click(373, 512)
        if pyautogui.pixel(458, 512)[0] == 0:
            click(458, 512)
        if pyautogui.pixel(551, 512)[0] == 0:
            click(551, 512)
        if pyautogui.pixel(625, 512)[0] == 0:
            click(625, 512)


time.sleep(2)
piano_auto()
