'''
find frames by id, or by name
driver.swithc_to.frame('framename')
Example:
#     find frame by id or name
driver.switch_to.frame('frame-bottom')
# print frame text to assert the right frame
txt = driver.find_element(By.XPATH, "//*[contains(text(), 'BOTTOM')]").text
print(txt)
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://testautomationpractice.blogspot.com/'

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)

driver.switch_to.frame('frame-one1434677811')
time.sleep(2)
f_name = driver.find_element(By.NAME, 'RESULT_TextField-1')
f_name.send_keys('Mansur')
time.sleep(2)
driver.switch_to.default_content()

driver.quit()