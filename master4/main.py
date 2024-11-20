import pyautogui
import time
import keyboard
import win32api
import win32con

# #AIMBOOTER

# img = pyautogui.screenshot(region=(160, 300, 640, 500))
# img = img.save('image aimbootter')


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) 
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    
def main():
    while not keyboard.is_pressed('q'):
        pic = pyautogui.screenshot(region=(160, 300, 640, 500))
        width, height = pic.size
        
        for x in range(0, width , 5):
            for y in range(0, height, 5):
                r, g, b = pic.getpixel((x, y))
                if b == 195:
                    click(x + 160, y + 300)
                    time.sleep(0.05)
                    break


time.sleep(2)
main()
