import pyautogui
import time
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

btn_2 = pyautogui.locateOnScreen('searched_image/2.png')
x2,y2 = pyautogui.center(btn_2)
click(x2,y2)

time.sleep(0.5)

btn_add = pyautogui.locateOnScreen('searched_image/+.png')
x_add, y_add = pyautogui.center(btn_add)
click(x_add,y_add)

time.sleep(0.5)

btn_8 = pyautogui.locateOnScreen('searched_image/8.png')
x8,y8 = pyautogui.center(btn_8)
click(x8,y8)

time.sleep(0.5)

btn_equal = pyautogui.locateOnScreen('searched_image/=.png')
x_equal, y_equal = pyautogui.center(btn_equal)
click(x_equal, y_equal)