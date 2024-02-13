from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#starts x=575 y=444 x2= 1327 y2=970 x-dif= 752 y-dif=526
#color (255,219,195)

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(575,444,752,526))
    width, heigth = pic.size
    
    for x in range(0,width,5):
        for y in range(0,heigth,5):
            r,g,b = pic.getpixel((x,y))
            if b == 195:
                click(x+575,y+444)
                time.sleep(0.05)
                break