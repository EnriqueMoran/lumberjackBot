# LumberJack Telegram Bot
Simple bot made for LumberJack telegram game. It recognises a couple of key pixels on your screen and makes lumberjack dodge tree's branches. **pyautogui library is needed!**


## How it works
The script recognises LumberJack's game window and clicks on play button. Uses player's position to locate branches and dodge them.

![alt tag](http://i.imgur.com/H7v3zwo.png)


_Recognises this area as start/restart button._

<br />
<br />
<br />
<br />
![alt tag](http://i.imgur.com/hKTuuio.png)


_Checks if indicated pixel is the same color as branch's. If true, lumberjack moves right, else left._


## Score record

| Speed (sec)  | Score (avg) V1.1 |Score (avg) V1.2|
| ------------ | -----------      |-----------     |
| 0.15         | 182              |254             |
| 0.12         | 186              |247             |
| 0.11         | 129              |314             |
| 0.1          | 29               |296             |
| 0.099        | 128              |334             |
| 0.08         | 18               |354             |
| 0.075        | -                |87              |
| 0.07         | 7                |93              |
<br />

![alt tag](http://i.imgur.com/hH5dY26.png)
<br />
<br />
<br />
## Usage example

Resize and place your telegram window as the image. Open the script with python IDLE, place next to telegram and run it (F5). Don't place IDLE's window above telegram's.



![alt tag](http://i.imgur.com/tiV3Eze.png)
