from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')
time.sleep(4)
driver.close()
