import pyautogui
import time


class lumberjackBot():

	 __author__ = "EnriqueMoran"

	def __init__(self, playX, playY, playerX, playerY):
		self.playX = playX
		self.playY = playY
		self.playerX = playerX
		self.playerY = playerY		

	def move(self, direction):
		if direction == "left":
			pyautogui.typewrite(['left'])
			pyautogui.typewrite(['left'])
		elif direction == "right":
			pyautogui.typewrite(['right'])
			pyautogui.typewrite(['right'])

	def play(self):
		while(1):
			branch = pyautogui.screenshot(region=(playerX, playerY - 85, 1, 1)) # Pixel of tree right side
			obstacle = branch.getpixel((0,0))
			if obstacle == (161, 116, 56):
				self.move("left")
			else:
				self.move("right")
			time.sleep(0.09)	# Speed of lumberman



if __name__ == "__main__":
	# LUMBERJACK WINDOWS MUST BE CLEAR
	playX, playY = pyautogui.locateCenterOnScreen('playButton.png')
	pyautogui.moveTo(playX, playY)	# Start the game by pressing play button
	pyautogui.click()
	time.sleep(1)
	playerX, playerY = pyautogui.locateCenterOnScreen('player.png') # Recognize position of player
	time.sleep(1)
	print("Im playing... To stop me click on IDLE window and press ctrl + C")
	lumberjackBot(playX, playY, playerX, playerY).play()
