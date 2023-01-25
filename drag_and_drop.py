import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


HOST = 'https://www.w3schools.com/html/html5_draganddrop.asp'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(HOST)

# locators
source = 'drag1'
target = 'div2'

# # steps
# f = driver.find_element(By.ID, source)
# t = driver.find_element(By.ID, target)
#
# move = ActionChains(driver)
# move.drag_and_drop(f, t).perform()
# time.sleep(5)


wait = WebDriverWait(driver, 20)
f = wait.until(EC.element_to_be_clickable((By.ID, source)))
t = wait.until(EC.element_to_be_clickable((By.ID, target)))
move = ActionChains(driver)
move.drag_and_drop(f, t).perform()
