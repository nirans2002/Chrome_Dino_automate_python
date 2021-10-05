from PIL import ImageGrab, ImageOps
import time
import pyautogui

# take screenscrots
time.sleep(1)
for i in range(250):
    im = pyautogui.screenshot(region=(10,350,600,200))
    # im = pyautogui.screenshot(region=(120,390,100,100))
    # im =  ImageGrab.grab(bbox=(190,350,100,100))
    im =  ImageOps.grayscale(im)
    data = im.load()
    # for a in range(120,350):
    for a in range(600):
        for b in range(200):
            for q in range(100,600,10):
        # for b in range(50,110):
                data[a,100] = 171
                data[q,b] = 150
    
            # print(data[a,b])

    filepath ="img/t1/img{}.png".format(i)
    im.save(filepath)
    print("saving image {}".format(i))
    time.sleep(0.1)


# for i in range(500):
#     im = pyautogui.screenshot(region=(140,430,10,10))
#     filepath ="img/img{}.png".format(i)
#     im.save(filepath)
#     print("saving image {}".format(i))
#     time.sleep(0.5)










# https://github.com/ClarityCoders/ChromeDino/blob/master/CreateData.py