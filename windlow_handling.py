import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://the-internet.herokuapp.com"

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)

driver.find_element(By.LINK_TEXT, 'Multiple Windows').click()
driver.find_element(By.LINK_TEXT, 'Click Here').click()
handles = driver.window_handles  #find all window handlers
print(handles)
driver.switch_to.window(handles[0]) #switch to parent window
print(driver.current_window_handle)
time.sleep(3)
driver.switch_to.window(handles[1]) #swithc to child window
print(driver.current_window_handle)
print(driver.find_element(By.TAG_NAME, 'h3').text) #assert right window
time.sleep(2)
parent = driver.switch_to.window(handles[0]) #switch back to child window
print(driver.current_window_handle)
assert driver.title == 'The Internet'
print(driver.title)


time.sleep(2)

driver.quit()
