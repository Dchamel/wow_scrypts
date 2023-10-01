import time

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

# float = cv2.imread('float_day.png')
float = cv2.imread('float_night.png')
bw, bh = float.shape[1::-1]
float_gray = cv2.cvtColor(float, cv2.COLOR_BGR2GRAY)

average = [0, ]
pyautogui.moveTo(1465, 976)
pyautogui.mouseDown()
time.sleep(0.1)
pyautogui.mouseUp()
for q in range(1000):
    try:
        time.sleep(1)
        pyautogui.moveTo(1465, 976)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(2)
        print(f'Step: {q}')
        main_scrshot = ImageGrab.grab(bbox=(260, 0, 1530, 420))
        main_scrshot.save('main_scrshot.png')

        main_rgb = cv2.imread('main_scrshot.png')
        main_gray = cv2.cvtColor(main_rgb, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(main_gray, float_gray, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.7)
        for i in range(70):
            try:
                float_scrshot = ImageGrab.grab(bbox=(x + 260, y, x + 260 + bw, y + bh))
                time.sleep(0.1)
                float_scrshot.save('float_scrshot.png')
                float_move = np.mean(float_scrshot)
                fish_biting = average[-1] - float_move
                print(fish_biting)
                if fish_biting >= 2:
                    pyautogui.moveTo(x + 260 + 15, y + 17)
                    pyautogui.mouseDown()
                    time.sleep(0.2)
                    pyautogui.mouseUp()
                    pyautogui.mouseDown(button='right')
                    time.sleep(0.2)
                    pyautogui.mouseUp(button='right')
                    break
                average.append(float_move)
            except:
                for coord in zip(*loc[::-1]):
                    x = int(coord[0])
                    y = int(coord[1])
                print(x, y)
                time.sleep(0.2)
        pyautogui.moveTo(100, 100)
        try:
            del x
            del y
        except:
            pass
        average = [0, ]
        time.sleep(1)
    except:
        continue
