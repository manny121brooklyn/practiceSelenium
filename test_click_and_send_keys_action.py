from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://qavbox.github.io/demo/signup'
username = 'username'
send = 'QAVBOX'

def test_sample():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    assert 'Registration' in driver.title

    action = ActionChains(driver)
    uname = driver.find_element((By.ID, username))
    action.click(uname).perform()
    time.sleep(3)
    action.send_keys(send).perform()
    time.sleep(3)
    action.send_keys_to_element(username, 'qavbox').perform()

    time.sleep(2)
    driver.quit()