from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.google.com'

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)

driver.get(url)
element = driver.find_element(By.NAME, 'q')
element.send_keys('bdd approach')

btn = driver.find_element(By.NAME, 'btnK')
# use javascript executor
driver.execute_script('arguments[0].click()',btn)

driver.close()