from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


url = 'https://www.python.org'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get(url)

# scroll down to the bottom
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# scroll by 500 pxl
# driver.execute_script('window.scrollBy(0,800);')

time.sleep(2)

driver.quit()


