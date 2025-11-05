# 240, 80
import pyautogui
import time

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.moveTo(240, 80, duration=0.7)
time.sleep(1)
pyautogui.click()
pyautogui.write("previsão do tempo hoje", interval=0.10)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("previsao_tempo.png")
pyautogui.alert(text="Captura de tela da previsão do tempo gerada na raiz", 
                title="Automação realizada",
                button="OK")