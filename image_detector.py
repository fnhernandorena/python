from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:

    try:
     if pyautogui.locateOnScreen('searched_image/search.png', confidence=0.8) != None:
        print("La imagen fue encontrada en la pantalla.")
     else:
        print("La imagen no fue encontrada en la pantalla.")
    except pyautogui.ImageNotFoundException:
        print("La imagen no fue encontrada en la pantallafverfer.")
