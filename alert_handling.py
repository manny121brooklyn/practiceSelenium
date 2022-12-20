'''
There are two ways of handling alert in selenium python
1. by using switch_to.alert
accetpt()  - click ok
dismiss()  - click cancel
2. Import alert module
from selenium.webdriver.common.alert import Alert
create object of Alert class
alert = Alert(driver)
alert.accetp() - click ok
alert.dismiss() - click cancel

'''

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# url = 'https://testautomationpractice.blogspot.com/'
#
# # create an object
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get(url)
#
# alert_btn = driver.find_element(By.XPATH, "//*[@onclick='myFunction()']")
# driver.execute_script('arguments[0].click();', alert_btn)
# time.sleep(3)
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(3)
# driver.quit()
#

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

url = 'https://testautomationpractice.blogspot.com/'

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)

alert_btn = driver.find_element(By.XPATH, "//*[@onclick='myFunction()']")
driver.execute_script('arguments[0].click();', alert_btn)
alert = Alert(driver)
alert.accept()