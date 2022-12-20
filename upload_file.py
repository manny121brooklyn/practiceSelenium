import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
xpath_locator = "//input[@type='file']"

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
driver.execute_script('window.scrollBy(0,400);')
upload_file = driver.find_element(By.XPATH, xpath_locator)
time.sleep(3)
# driver.execute_script('arguments[0].click();', upload_file)
upload_file.send_keys('C:/reports/google.png')
time.sleep(3)
driver.quit()


