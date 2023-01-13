from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import io
import subprocess

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
executor_url = driver.command_executor._url
session_id = driver.session_id

print(session_id)
print(executor_url)

driver.get("https://www.hotbit.io/exchange?symbol=XRP_USDT")


time.sleep(10)
en = driver.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div[1]/div[1]/div[4]/ul/li/form[1]/section[1]/div[4]/div/div/div[1]')
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(50, 0).release().perform()