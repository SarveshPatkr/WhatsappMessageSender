import pyautogui
import time
import subprocess
import json
from contacts import find_phone_number

def send(name, message, waiting_time):
    phone_number = find_phone_number(name, "./contact.json")
    url = f'whatsapp://send?phone={phone_number}&text={message}'
    command = f'Start-Process "{url}"'
    subprocess.run(['powershell', '-Command', command])
    time.sleep(waiting_time/2)
    search_result = pyautogui.locateOnScreen('./search_result_dark.png')

    if search_result is None:
        search_result = pyautogui.locateOnScreen('./search_result_light.png')

    if search_result is not None:
        center = pyautogui.center(search_result)
        x, y = center
        x += 150
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(waiting_time/2)

    pyautogui.press('enter')
    return "Message sent Successfully"

send("Name 1", "hi how are you", 2)