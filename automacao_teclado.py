import pyautogui
import time

# pyautogui.write("Olá mundo")

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("calculadora", interval=0.20)
pyautogui.press("enter")

pyautogui.moveTo(520, 40)
time.sleep(5)
pyautogui.click()