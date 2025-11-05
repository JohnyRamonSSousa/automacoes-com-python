import pyautogui
from time import sleep

with open("files/alunos.txt", "r", encoding="utf-8") as file:
    for line in file:
        nome = line.split(",")[0]
        email = line.split(",")[1]
        pyautogui.click(1083, 283, duration=0.70)
        pyautogui.write(nome)
        pyautogui.click(1096, 322, duration=0.70)
        pyautogui.write(email)
        pyautogui.click(1113, 357, duration=0.4)
        pyautogui.screenshot(f"files/img/{nome}.png")
        sleep(1)