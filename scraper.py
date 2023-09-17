import webbrowser
import pyautogui
import time

url = 'https://www.spitogatos.gr/enoikiaseis-katoikies/thessaloniki-kentro'
webbrowser.open(url)
time.sleep(10)

#click in the middle of the screen
screen_width, screen_height = pyautogui.size()
middle_x = screen_width // 2
middle_y = screen_height // 2
pyautogui.click(middle_x, middle_y, button='left')

time.sleep(2)
#take screenshot of the whole site (firefox)
pyautogui.hotkey('ctrl', 'shift', 's')
time.sleep(2)
#save image
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('enter')












