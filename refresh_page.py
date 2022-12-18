'''
Example of refresh method in selenium webdriver
The following code would:

load google website and
once it gets loaded it would refresh it (using refresh method in selenium webdriver) and
after refreshing it would close the window.
'''

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')
driver.refresh()

driver.close()