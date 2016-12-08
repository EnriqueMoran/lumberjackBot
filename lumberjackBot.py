import pyautogui
import time


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

    def play(self):
        while(1):
            branch = pyautogui.screenshot(region=(treeX - 30, treeY - 130, 1, 1)) # Pixel of tree left side
            obstacle = branch.getpixel((0,0))
            end = pyautogui.screenshot(region=(treeX - 30, treeY - 100, 1, 1))
            stop = end.getpixel((0,0))
            if obstacle == (161, 116, 56):              
                self.move("right")
            else:
                self.move("left")
            time.sleep(0.1)   # Speed of lumberjack
            if stop == (255,255,255):
                return 0


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

0.15 -> 180, 188, 180
0.12 -> 246, 204, 72X, 222
0.11 -> 218X, 128X, 62X, 232, 6X
0.1 -> 12X, 84X, 16X, 6X, 28X
0.099 -> 164X, 108X, 114X
0.08 -> 24X, 34X, 6X, 4X, 24X
0.07 -> 4X, 8X, 2X 

'''