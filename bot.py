from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains 
import time

## lesen welches operating system und dann entsprechender driver
## wichtig du musst dir ein txt file mit dem name operating_system anlegen und windows reinschreiben
f = open('operating_system.txt', 'r')
t = f.readline().replace('\n', '')
f.close()

if t == 'windows': 
    browser = webdriver.Chrome('./chromedriver.exe')
if str(t) == 'linux':
    browser = webdriver.Chrome('./chromedriver')

# browser.get('http://www.instagram.com')
browser.get('https://hammerjs.github.io/')
time.sleep(5)

# accept_cookies = browser.find_element(By.CSS_SELECTOR, '.aOOlW.bIiDR')
# print(accept_cookies.get_attribute('innerHTML'))
# print(accept_cookies)

# accept_cookies.click()

action = ActionChains(browser) 
action.move_to_element(browser.find_element(By.CSS_SELECTOR, '#hitarea')) 
action.click_and_hold() 
action.move_by_offset(8,1) 
action.move_by_offset(6,1) 
action.move_by_offset(4,1) 
action.move_by_offset(2,1) 
action.move_by_offset(1,1) 
action.move_by_offset(1,2) 
action.move_by_offset(1,4) 
action.move_by_offset(1,6) 
action.move_by_offset(1,8) 
action.release() 
action.perform()

while 1:
    pass
browser.quit()
