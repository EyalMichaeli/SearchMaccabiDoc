"""
2. create a req.txt -
3. add packages -
4. write code for main.py -
"""


from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pynput

keyboard_control = pynput.keyboard.Controller()
keyboard_key = pynput.keyboard.Key

mouse_control = pynput.mouse.Controller()
mouse_button = pynput.mouse.Button


'''
usr=input('Enter Email Id:')  
pwd=input('Enter Password:')  
'''
usr = '2018739'
pwd = 'or528491!'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://teva.net.hilan.co.il/login')
print("Opened Hilan")
sleep(1)

username_box = driver.find_element_by_id('user_nm')
username_box.send_keys(usr)
print("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('password_nm')
password_box.send_keys(pwd)
print("Password entered")
'''
for i in range(3):
    try:
        if i == 0:
            login_box = driver.find_element_by_class_name('submit')
        if i == 1:
            login_box = driver.find_element_by_link_text('submit')
        login_box = driver.find_element_by_tag_name('submit')
    except:
        print(i, 'didnt work')
        continue


login_box.click() 

'''

keyboard_control.press(keyboard_key.enter)
keyboard_control.release(keyboard_key.enter)

sleep(2)

first = driver.find_element_by_id('tabItem_9_3_SpanBackground')
sec = driver.find_element_by_id('innerNavBarItem_47')

ActionChains(driver).move_to_element(first).click(sec).perform()
'''
third = driver.find_element_by_name('ctl00$mp$RG_Days_09902018739_2020_12$cellOf_Symbol.SymbolId_EmployeeReports_row_0_0$Symbol.SymbolId_EmployeeReports_row_0_0')
third.click()
'''
sleep(3)


mouse_control.position = (732.0859375, 622.25390625)

#mouse_control.press(mouse_button.left)
keyboard_control.press(keyboard_key.space)

for i in range(6):
    keyboard_control.press(keyboard_key.up)
    keyboard_control.release(keyboard_key.up)

mouse_control.release(mouse_button.left)

keyboard_control.press(keyboard_key.enter)
keyboard_control.release(keyboard_key.enter)

keyboard_control.press(keyboard_key.enter)
keyboard_control.release(keyboard_key.enter)

print("Done")
sleep(60)
driver.quit()
print("Finished")







if __name__ == '__main__':
    pass
