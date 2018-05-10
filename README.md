# LumberJack Telegram Bot
Bot made for LumberJack telegram game. It recognises a couple of key pixels on your screen and makes lumberjack dodge tree's branches. **pyautogui and Pillow libraries is needed!**


## How it works
The script recognises LumberJack's game window and clicks on play button. Uses tree's position to locate branches and dodge them.

![alt tag](http://i.imgur.com/H7v3zwo.png)


_Recognises this area as start/restart button._


![alt tag](http://i.imgur.com/hKTuuio.png)


_Checks if indicated pixel is the same color as branch's. If true, lumberjack moves right, else left._


## Score record

| Speed (sec)  | Score (avg) V1.1 |Score (avg) V1.2|Score V1.3 (No longer depends on speed)| Score V1.4 |
| ------------ | -----------      |-----------     |-----------                            |----------  |
| **0.15**     | 182              |254             |358                                    |470         |
| **0.12**     | 186              |247             |368                                    |482         |
| **0.11**     | 129              |314             |370                                    |480         |
| **0.1**      | 29               |296             |366                                    |480         |
| **0.099**    | 128              |334             |366                                    |484         |
| **0.08**     | 18               |354             |372                                    |460         |
| **0.075**    | -                |87              |358                                    |460         |
| **0.07**     | 7                |93              |374                                    |472         |
<br />

![alt tag](http://i.imgur.com/yYEl4Nm.png)
<br />
<br />
<br />
## Usage example

Resize and place your telegram window as the image. Open the script with python IDLE, place next to telegram and run it (F5). Don't place IDLE's window above telegram's.



![alt tag](http://i.imgur.com/tiV3Eze.png)
