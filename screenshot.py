from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')
driver.save_screenshot('C:/reports/google1.png')
# driver.get_screenshot_as_file('C:/reports/google.png')

driver.close()