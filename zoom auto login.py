import os
import pyautogui
import time
from datetime import datetime
import pandas as pd



def joining(idm,pwd):
    os.system("open /Applications/zoom.us.app")
    time.sleep(10)
    pyautogui.click(x=573, y=298) #join
    pyautogui.write(idm) #id
    pyautogui.click(x=802, y=535) #id enter
    time.sleep(5)
    pyautogui.write(pwd) #password type
    pyautogui.click(x=844, y=578) #password click
    time.sleep(3000) #during class sleep 50 min
    
    pyautogui.click(x=175, y=34) #exit
    time.sleep(2)
    pyautogui.click(x=216, y=80) #leave meeting
    pyautogui.click(x=245, y=93) #exit zoom
    
    
ids=['730 0277 9324','730 0277 9324'] #enter id's
pd=['qXq3uq','qXq3uq'] #enter passwords
count=0
while True:
    now = datetime.now().strftime("%I:%M:%s") #start time
    print(now)
    idm=ids[count]
    pwd=pd[count]
    joining(idm,pwd)
    time.sleep(600) #10mins break
    count+=1
    