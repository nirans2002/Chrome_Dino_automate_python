# https://pyautogui.readthedocs.io/en/latest/

import time
import pyautogui
import numpy as np
import random
from PIL import ImageGrab, ImageOps

# click function
def press(key):
    pyautogui.keyDown(key)
    time.sleep(0.01)
    pyautogui.keyUp(key)
    return



# variables

# delay for 5 seconds to navigate to game
time.sleep(2)

area = (10,350,600,200)
# is night or day
night = 0


def is_night(data):
    pxTime1 =(10,170)
    pxTime2 =(20,170)
    pxTime3 =(30,170)

    # print(data[60,100])
    if (data[10,170] == 33 and data[20,170] == 33 and data[30,170] == 33 ):
        isNightMode = 1
        return isNightMode
pxDark = 33
ground_sur_y = 100
air_sur_y = 60
start_sur_x = 160
sur_x = start_sur_x
# run
while True:

    try:
        image = pyautogui.screenshot(region=area)
        image = ImageOps.grayscale(image)
        data = image.load()

        isNightMode = is_night(data)
        
        # print(isNightMode)

        #catus and bird on ground
        if (data[sur_x,ground_sur_y] == 171 ):
            press('up')  
            print("jump")

    except Exception as e:
        print(e)



