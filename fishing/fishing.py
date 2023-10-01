import time

import cv2
import numpy as np
from PIL import ImageGrab

bobber = cv2.imread('bobber1.png')
bw, bh = bobber.shape[1::-1]
print(bobber)
bobber_gray = cv2.cvtColor(bobber, cv2.COLOR_BGR2GRAY)

average = [0, ]
for q in range(20):
    print(f'Step: {q}')
    main_scrshot = ImageGrab.grab(bbox=(260, 0, 1530, 420))
    # main_scrshot.save('main_scrshot.png')

    main_rgb = cv2.imread('main_scrshot.png')
    main_gray = cv2.cvtColor(main_rgb, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(main_gray, bobber_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)
    for i in range(10):
        try:
            bobber_scrshot = ImageGrab.grab(bbox=(x, y, x - bw, y - bh))
            time.sleep(0.1)
            bobber_scrshot.save('bobber_scrshot.png')
            bobber_move = np.mean(bobber_scrshot)
            fish_biting = average[-1] - bobber_move
            # print(fish_biting)
            if fish_biting >= 1:
                print(True)
                time.sleep(0.4)
                break
            average.append(bobber_move)
        except:
            for coord in zip(*loc[::-1]):
                x = int(coord[0])
                y = int(coord[1])
                print(x, y)
            time.sleep(0.1)
