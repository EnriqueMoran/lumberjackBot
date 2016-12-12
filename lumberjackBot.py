import pyautogui
import time
from ctypes import windll


class lumberjackBot():

    __author__ = "EnriqueMoran"

    def __init__(self, playX, playY, treeX, treeY):
        self.playX = playX
        self.playY = playY
        self.treeX = treeX
        self.treeY = treeY      

    def move(self, direction):
        if direction == "left":
            pyautogui.typewrite(['left'])
            pyautogui.typewrite(['left'])
        elif direction == "right":
            pyautogui.typewrite(['right'])
            pyautogui.typewrite(['right'])

    def get_color(self, rgb):
        r = rgb & 0xff
        g = (rgb >> 8) & 0xff
        b = (rgb >> 16) & 0xff
        return r,g,b


    def play(self):
        cont = 0
        while(1):          
            end = windll.user32.GetDC(0)
            rgb = windll.gdi32.GetPixel(end, treeX - 30, treeY - 130)
            stop = windll.gdi32.GetPixel(end, treeX - 30, treeY - 100)
            print(str(self.get_color(rgb)))
            if self.get_color(rgb) == (161, 116, 56) or self.get_color(rgb) == (153, 110, 54):       
                pyautogui.typewrite(['right'])
                pyautogui.typewrite(['right'])
            elif self.get_color(rgb) != (161, 116, 56) and self.get_color(rgb) != (153, 110, 54):
                pyautogui.typewrite(['left'])
                pyautogui.typewrite(['left'])
            cont += 2
            if self.get_color(stop) == (255,255,255) or cont >= 420:
                return 0
            time.sleep(0.075)   # Speed of lumberjack


if __name__ == "__main__":
    # LUMBERJACK WINDOWS MUST BE CLEAR
    playX, playY = pyautogui.locateCenterOnScreen('playButton.png')
    pyautogui.moveTo(playX, playY)  # Start the game by pressing play button
    pyautogui.click()
    time.sleep(1)
    treeX, treeY = pyautogui.locateCenterOnScreen('tree.png') # Recognize tree position
    time.sleep(1)
    print("Im playing...")
    lumberjackBot(playX, playY, treeX, treeY).play()




'''  SCORE:

0.15 -> 254, 254, 256
0.12 -> 278X, 288, 42, 314, 314
0.11 -> 314, 314, 314
0.1 -> 334, 334, 144X, 334, 334
0.099 -> 334, 334, 334
0.08 -> 354, 354, 352
0.075 -> 116X, 28X, 84X, 122X
0.07 -> 70X, 250X, 104X, 8X, 34X

'''