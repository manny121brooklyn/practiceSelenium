from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')
driver.save_screenshot('C:/reports/google1.png')
# driver.get_screenshot_as_file('C:/reports/google.png')
print('The title of this page is', driver.title)
print(f'Title of this page is {driver.title}')
print('Test complete')
driver.close()

