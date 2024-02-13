from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Game link: https://www.juegos.com/juego/teclas-de-piano-magicas

x = [350, 450, 550, 650]
y = 700
y2 = 550

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    
  if pyautogui.pixel(x[0], y)[0] == 0:
     click(x[0], y)
  
  if pyautogui.pixel(x[1], y)[0] == 0:
     click(x[1], y)
    
  if pyautogui.pixel(x[2], y)[0] == 0:
     click(x[2], y)
    
  if pyautogui.pixel(x[3], y)[0] == 0:
     click(x[3], y)
    
  if pyautogui.pixel(x[0], y2)[0] == 0:
     click(x[0], y2)
  
  if pyautogui.pixel(x[1], y2)[0] == 0:
     click(x[1], y2)
    
  if pyautogui.pixel(x[2], y2)[0] == 0:
     click(x[2], y2)
    
  if pyautogui.pixel(x[3], y2)[0] == 0:
     click(x[3], y2)
     
#this function is slower than the upper
#while not keyboard.is_pressed('q'):
#    for x in x_list:
 #           click(x, y)