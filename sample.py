# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# url = 'https://www.google.com'
# search_box = 'q'
# search_string = 'Python for beginners'
# button = 'btnK'
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
# search = driver.find_element(By.NAME, search_box)
# search.send_keys(search_string)
# btn = driver.find_element(By.NAME, button)
# driver.execute_script('arguments[0].click();', btn)
# driver.close()
#
# driver.get('https://www.youtube.com')


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# url = 'https://www.google.com'
# search_box = 'q'
# search_string = 'Python for beginners'
# button = 'btnK'
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
# search = driver.find_element(By.NAME, search_box)
# search.send_keys(search_string)
# btn = driver.find_element(By.NAME, button)
# driver.execute_script('arguments[0].click();', btn)
# driver.quit()
#
# driver.get('https://www.youtube.com')


url = 'https://www.google.com'
search_box = 'q'
search_string = 'Python for beginners'
button = 'btnK'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
search = driver.find_element(By.NAME, search_box)
search.send_keys(search_string)
btn = driver.find_element(By.NAME, button)
driver.execute_script('arguments[0].click();', btn)

driver.quit()

driver.get('https://www.youtube.com')
