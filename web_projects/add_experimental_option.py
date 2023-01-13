from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


times = ""
start_page = ""
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def start_pages(target_page):
    for x in range(0, len(page_number)):
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        driver.get(target_page)
        chrome_options.add_experimental_option("detach", True)


while times == "":
    times = input("How many pages do you want?\n")

url = input("Yeezy Supply or Adidas?""\nEither 'YS' or 'Adidas'\n")
url_choice = url.lower()

page_number = list()
for i in range(0, int(times)):
    page_number.append(times)

if url_choice == 'ys':
    start_page = 'https://yeezysupply.com/'
    start_pages(start_page)
elif url_choice == 'adidas':
    start_page = 'https://www.adidas.com/yeezy'
    start_pages(start_page)

