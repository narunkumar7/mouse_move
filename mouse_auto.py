 #pip install pyautogui

import pyautogui
import time
import sys
from datetime import datetime
print(pyautogui.size())

a = 0
while a<100:
    pyautogui.moveTo(100, 100, duration = 1)
    pyautogui.moveTo(50, 300, duration = 1)
    time.sleep(2)
    a+= 25
    print(a)


'''
import pyautogui
import time
import sys
from datetime import datetime
#pyautogui.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])

while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
    '''