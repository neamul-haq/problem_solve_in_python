import pyautogui
from time import sleep

n = int(input())
sleep(3)
col=1
for i in range(0,n):
    for i in range(0,col):
        pyautogui.press('#')
    col+=1
    if col!=n+1:
        pyautogui.press('enter')
