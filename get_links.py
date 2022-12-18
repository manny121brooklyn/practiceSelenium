from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.google.com'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    print(link.get_attribute('href'))

print(len(links))

driver.quit()