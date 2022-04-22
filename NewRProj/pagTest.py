#packages
import os
import time
import pyautogui as pag

#open Rstudio
os.system("open ''") #place path to RStudio here
time.sleep(5)

#simplify entire process
def moveToClick(png_name):
    button = pag.locateCenterOnScreen(png_name)
    x_coord = button[0]/2
    y_coord = button[1]/2
    pag.click(x=x_coord,y=y_coord,clicks=1)
    time.sleep(0.5)

#Project
moveToClick("Pointers/Proj_dropdown.png")

#New Project
moveToClick("Pointers/newProj_gray.png")

#New Directory
moveToClick("Pointers/newDirectory.png")

#New Project
moveToClick("Pointers/newProj.png")

#enter directory name
pag.write('test_dir')

#press enter
pag.press('enter')
time.sleep(5)

#click New Folder
moveToClick("Pointers/newFolder.png")

#enter name (Input)
pag.write('Input')

#press enter
pag.press('enter')
time.sleep(3)

#click New Folder
moveToClick("Pointers/newFolder.png")

#enter name (Output)
pag.write('Output')

#press enter
pag.press('enter')

#show alert: done!
pag.alert('RProject folder with basic components has been created!.')