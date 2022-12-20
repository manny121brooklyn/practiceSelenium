'''
get_cookies
get_cookie
add_cookies
delete_cookie
delete_all_cookies
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.google.com'

# create an object
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
# get all cookies present in the web app of google.com
# cookies = driver.get_cookies()
# # print all cookies
# for cookie in cookies:
#     print(cookie)

# get a cookies with name 'NID'
# nid = driver.get_cookie('NID')
# print(nid)

# delete all cookies
# cookies = driver.delete_all_cookies()
# let's check if any cookie is left
# print(cookies)

# get cookie with name 'OGPC'
cookie = driver.get_cookie('OGPC')
print(cookie)

driver.quit()