import pyautogui
import time
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    
operation_string = input('\x1b[1;33m'+'Using numbers and , - + x % \nWrite the math operation you want the robot do: \n \n')

time.sleep(4)

operation_array = list(operation_string)

for e in operation_array:
    btn = pyautogui.locateOnScreen(f'searched_image/{e}.png')
    x2,y2 = pyautogui.center(btn)
    click(x2,y2)
    time.sleep(0.5)
    
btne = pyautogui.locateOnScreen('searched_image/=.png')
x2,y2 = pyautogui.center(btne)
click(x2,y2)