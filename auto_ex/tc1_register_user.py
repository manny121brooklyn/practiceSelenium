
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HOST_URL = "http://automationexercise.com"

#Launch browser
options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options)

# try:

print('Navigate to URL')
driver.get(HOST_URL)

print('Verify that home page is visible successfully')
print(f'Home page title is {driver.title}')
assert driver.title == 'Automation Exercise'

print("Click on 'Signup/Login' button")
driver.find_element(By.XPATH, "//*[contains(text(), ' Signup / Login')]").click()
time.sleep(0)
print("Verify 'New User Signup!' is visible")
print(f'Home page title is {driver.title}')
assert driver.title == 'Automation Exercise - Signup / Login'

print('Enter name and email address')
# name = driver.find_element(By.NAME, 'name').clear()
driver.find_element(By.NAME, 'name').send_keys('Mansur')
driver.find_element(By.XPATH, "(//*[@name='email'])[2]").send_keys('manny142@gmail.com')


print("Click 'Signup' button")
driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button").click()

print("Verify that 'ENTER ACCOUNT INFORMATION' is visible")
print(f'Home page title is {driver.title}')
assert driver.title == 'Automation Exercise - Signup'

print("Fill details: Title, Name, Email, Password, Date of birth")
title = driver.find_element(By.ID, 'id_gender1').click()

name = driver.find_element(By.NAME, 'name')
name.clear()
name.send_keys('Mansur')


pwd = driver.find_element(By.XPATH, "//*[@type='password']")
pwd.clear()
# pwd = driver.find_element(By.ID, "password")
pwd.send_keys('123a')


date_of_birth= driver.find_element(By.ID, 'days')
day_select = Select(date_of_birth)
day_select.select_by_value('1')


month_of_birth = driver.find_element(By.ID, 'months')
month_select = Select(month_of_birth)
month_select.select_by_visible_text('January')

year_of_birth = driver.find_element(By.ID, 'years')
year_select = Select(year_of_birth)
year_select.select_by_value('1984')

print("Select checkbox 'Sign up for our newsletter!'")
checkbox = driver.find_element(By.ID, 'newsletter')
checkbox.click()

print("Select checkbox 'Receive special offers from our partners!'")
checkbox1 = driver.find_element(By.ID, "optin")
checkbox.click()

print("Fill details: First name, Last name, Company, Address, "
      "Address2, Country, State, City, Zipcode, Mobile Number")
# first name
first_name = driver.find_element(By.ID, 'first_name')
first_name.clear()
first_name.send_keys('Mansur')
time.sleep(2)

# last name
last_name = driver.find_element(By.ID, 'last_name')
last_name.clear()
last_name.send_keys('Abdurakhmanov')


# company
company = driver.find_element(By.ID, 'company')
company.clear()
company.send_keys('MAG, LLC')


# address 1
address1 = driver.find_element(By.ID, 'address1')
address1.clear()
address1.send_keys('141 Nept Ave, Bronx')


# address 2
address2 = driver.find_element(By.ID, 'address2')
address2.clear()
address2.send_keys('FL 2')


# country
country_select = driver.find_element(By.ID, 'country')
country_dd = Select(country_select)
country_dd.select_by_index(1)


# state
state_select = driver.find_element(By.ID, 'state')
state_select.clear()
state_select.send_keys('New York')


# city
city_select = driver.find_element(By.ID, 'city')
city_select.clear()
city_select.send_keys('New York')


# zipcode
zipcode = driver.find_element(By.ID, 'zipcode')
zipcode.clear()
zipcode.send_keys('11254')


    # mobile
mob_numb = driver.find_element(By.ID, 'mobile_number')
mob_numb.clear()
mob_numb.send_keys('1234567890')

print("Click 'Create Account button'")
create_button = driver.find_element(By.XPATH, "(//*[@type='submit'])[1]")
driver.execute_script('arguments[0].click();', create_button)

print("Verify that 'ACCOUNT CREATED!' is visible")
acc_created = driver.find_element(By.XPATH, "//*[@id='form']//h2/b")
print(acc_created.text)

print("Click 'Continue' button")
continue_button = driver.find_element(By.XPATH, "//*[@class='pull-right']/a")
continue_button.click()
title = "Automation Exercise - Account Created"
assert title == driver.title
print(driver.title)

# print("Verify that 'Logged in as username' is visible")

verify_logged_in_user = driver.find_element(By.XPATH, "//*[@class='col-sm-8']//ul/li[10]/a")
verify_logged_in_user.is_displayed()
print(verify_logged_in_user.text)

# print("Click 'Delete Account' button")
wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), ' Delete Account')]"))).click()


print("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button")
acct_deleted = driver.find_element(By.XPATH, "//*[@id='form']//h2/b")
print(acct_deleted.text)

# except Exception as err:
#     print('Python exception: test failed with the following exception')
#     print(err)
#
# except (NoSuchElementException, TimedoutException) as err:
#     print(err)
#     print('Selenium Exception: test failed with the following exception')
#
# finally:
#     driver.quit()

