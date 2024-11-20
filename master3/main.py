import pyautogui as pg
import time
import io
import pyperclip
time.sleep(10)
txt = io.open('animals.txt', mode='r', encoding='UTF-8');
text = " "

for i in txt:
    str = text + i
    pyperclip.copy(str)
    pg.hotkey("ctrl", "v")
    pg.press('Enter')
