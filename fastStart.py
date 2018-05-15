import os ## OS stuff
import subprocess ## Process-related stuff
import pyautogui ## GUI modification
import time ## Time-related stuff
import webbrowser ## Web browser related stuff

## test = os.chdir(r"C:\Git\java-notes\chapter-3")

print('Program running...')

subprocess.run(r"C:/cmder/Cmder.exe") ## Run cmder
time.sleep(0.5) ## Wait half a second
pyautogui.typewrite(r"cd C:\Git\java-notes\chapter-3") ## Type input to cmder(cmder is currently active)
pyautogui.press('enter') ## Press enter
pyautogui.typewrite("ng serve") ## Initiate Angular
pyautogui.press('enter')

subprocess.run(r"C:/cmder/Cmder.exe") ## Run cmder
time.sleep(0.5) ## Wait half a second
pyautogui.typewrite(r"cd C:\Git\java-notes\chapter-3") ## Type input to cmder(cmder is currently active)
pyautogui.press('enter') ## Press enter
pyautogui.typewrite("##server command") ## Initiate Server
time.sleep(3) ## Wait 3 seconds
pyautogui.typewrite("##project selector command") ## Select project
pyautogui.press('enter') ## Press enter
pyautogui.typewrite("##project run") ## run project
pyautogui.press('enter') ## Press enter

subprocess.run(r"C:\Program Files (x86)\Firefox Developer Edition") ## Run Firefox dev edition
webbrowser.open(r"http://localhost:4200",new=2) ## Open URL with a new tab if possible
webbrowser.open(r"http://localhost:9000",new=2) ## Open URL with a new tab if possible