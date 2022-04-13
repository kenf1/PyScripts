#packages
import os
import time
import pyautogui as pag

#open RStudio
os.system("open ''") #insert path to RStudio inside ' '
time.sleep(5)

def moveToclick(x_coord,y_coord):
    pag.click(x=x_coord,y=y_coord,clicks=1)
    time.sleep(0.5)

#click File
moveToclick(1736,67)

#click New Project
moveToclick(1638,95)

#click New Directory
moveToclick(747,477)

#click New Project
moveToclick(747,462)

#enter directory name
pag.write('test_dir')

#press enter
pag.press('enter')
time.sleep(5)

#click New Folder
moveToclick(1026,481)

#enter name (Input)
pag.write('Input')

#press enter
pag.press('enter')
time.sleep(3)

#click New Folder
moveToclick(1026,481)

#enter name (Output)
pag.write('Output')

#press enter
pag.press('enter')

#show alert: done!
pag.alert('RProject folder with basic components has been created!.')