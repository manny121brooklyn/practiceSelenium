from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')
time.sleep(2)
driver.get('https://www.python.org')
time.sleep(2)
driver.refresh()
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)

driver.close()