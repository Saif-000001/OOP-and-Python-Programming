# import pyautogui
# from time import sleep
# sleep(5)
# for i in range(0,5):
#     pyautogui.write("#", interval = 0.25)
#     pyautogui.press("Enter")


import pyautogui  
levels = int(input())
for i in range(1, levels + 1):
        pyramid_row = '#' * i
        pyautogui.typewrite(pyramid_row, interval=0.25)
        pyautogui.press('enter')


