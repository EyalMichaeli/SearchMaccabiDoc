"""
Written by: Eyal Michaeli
Email: eyalmichaeli98@gmail.com
"""

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pynput
import json
import telegram_send
import clipboard
import time
import schedule


# read config json
with open("config.json") as f:
    config = json.load(f)

user_id = config["ID"]
pwd = config["password"]
doc_first_name = config["doc_first_name"]
doc_last_name = config["doc_last_name"]
doc_yeshuv = config["yeshuv"]
earliest_date = time.strptime(config["earliest_date"], "%d/%m/%Y")

keyboard_control = pynput.keyboard.Controller()
keyboard_key = pynput.keyboard.Key

mouse_control = pynput.mouse.Controller()
mouse_button = pynput.mouse.Button

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.maccabi4u.co.il/14-he/Maccabi.aspx')
print("Opened Maccabi website")
sleep(1)

mouse_positions = {
    "sign_in": (195, 333),
    "knisa_sisma": (1032, 326),
    "ID": (1050, 380),
    "pass": (963, 454),
    "knisa_ezor_ishi": (930, 565),
    "esc": "esc",
    "zimun_tor": (910, 440),
    "rofe": (1020, 534),
    "last_name": (895, 647),
    "first_name": (915, 687),
    "yeshuv": (908, 756),
    "click_city": (900, 782),
    "click": (430, 840),
    "date1": (630, 722),
    "date2": (715, 722)
}


def main():
    try:
        for key, value in mouse_positions.items():
            sleep(2)
            if key == "esc":
                keyboard_control.press(keyboard_key.esc)
                keyboard_control.release(keyboard_key.esc)
                continue

            if key == "date1":
                mouse_control.position = value
                sleep(1)
                mouse_control.press(mouse_button.left)
                mouse_control.position = mouse_positions["date2"]
                mouse_control.release(mouse_button.left)
                # copy (cmd + 'c')
                keyboard_control.press(keyboard_key.cmd)
                keyboard_control.press('c')
                keyboard_control.release('c')
                keyboard_control.release(keyboard_key.cmd)
                # send telegram message
                sleep(1)
                new_earliest_date = time.strptime(str(clipboard.paste()), "%d/%m/%Y")
                print(f"No earlier date for now. earliest date for the moment is: {clipboard.paste()}")
                if new_earliest_date < earliest_date or True:
                    telegram_send.send(
                        messages=[f"There is an earlier date for your doc! \n {doc_last_name}, {doc_first_name}"
                                  f"\nIt's on \n{clipboard.paste()}"])
                continue

            mouse_control.position = value
            sleep(1)
            mouse_control.press(mouse_button.left)
            mouse_control.release(mouse_button.left)

            if key in ("knisa_ezor_ishi", "zimun_tor"):
                sleep(2)
            if key == "ID":
                keyboard_control.type(str(user_id))
            if key == "pass":
                keyboard_control.type(str(pwd))
            if key == "last_name":
                sleep(2)
                keyboard_control.type(str(doc_last_name))
            if key == "first_name":
                keyboard_control.type(str(doc_first_name))
            if key == "yeshuv":
                keyboard_control.type(str(doc_yeshuv))
    except Exception as e:
        telegram_send.send(
            messages=[f"Error in SearchMaccabiDoc python program.\n error: {e}"])

    print("Done")
    sleep(10)
    driver.quit()
    print("Finished, closed chrome")


if __name__ == '__main__':
    main()

# schedule
# checkout this link for details: http://theautomatic.net/2020/11/18/how-to-schedule-a-python-script-on-a-mac/
# when i want to finish it:

'''
You can view jobs:
schedule.jobs
clear them:
schedule.clear()
'''

schedule.every(24).hours.do(main)

while True:
    schedule.run_pending()
