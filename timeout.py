from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.google.com'

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)

# add time limit of 20 seconds to load the page
driver.set_page_load_timeout(20)

driver.quit()