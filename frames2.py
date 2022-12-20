import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = "https://the-internet.herokuapp.com"

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)
frames = driver.find_element(By.LINK_TEXT, 'Frames').click()
n_frames = driver.find_element(By.LINK_TEXT, 'Nested Frames').click()
driver.switch_to.frame('frame-bottom')
txt = driver.find_element(By.XPATH, "//*[contains(text(), 'BOTTOM')]").text
print(txt)
driver.switch_to.default_content()

driver.quit()

