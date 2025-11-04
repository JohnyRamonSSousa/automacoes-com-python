import pyautogui
import time


# comando da tela
print(pyautogui.size())

# posição atual do curso
print(pyautogui.position())

# aplicação para ver a posição do mouse em tempo real 
# digite Python no termial
# from pyautogui import mouseinfo
# mouseInfo()

# move o cursor do mouse
pyautogui.moveTo(1256, 53, duration=0.8)
time.sleep(1)
pyautogui.click()

# realizado o scroll
pyautogui.moveTo(1566, 53)
pyautogui.click()
time.sleep(1)
pyautogui.scroll(4000)
