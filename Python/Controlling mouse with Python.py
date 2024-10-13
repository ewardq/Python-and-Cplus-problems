"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Move cursor at random
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

import pyautogui
from pyautogui import press, typewrite, hotkey
import random
import time
import os

def autogui_demo():
    pyautogui.moveTo(100, 150)
    pyautogui.moveRel(0, 20)  # move mouse 10 pixels down
    pyautogui.dragTo(100, 150)
    pyautogui.dragRel(0, 20) # drag mouse 10 pixels down
    
def move_to_random_position():
    a = random.randrange(200, 400)
    pyautogui.dragTo(a + 200, 200)
    
def move_mouse_at_random():
    for i in range(10000):
        time.sleep(4)
        move_to_random_position()
        print(i, end="\r")
        
if __name__ == "__main__":
    move_mouse_at_random()
    

"""""
 =============================  TOP SOLUTION   =======================================

 =====================================================================================  
"""""
