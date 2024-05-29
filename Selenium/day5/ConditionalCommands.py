import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
driver.maximize_window()

#Is_Displayed() , Is_Enabled()

# search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print('is_displayed :', search_box.is_displayed()) #True
#
# search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print('is_enabled :', search_box.is_enabled()) #True

#Is_Selected : for radio button and checkbox
radio_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
radio_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("default radio button status ......")
print('radio_male :', radio_male.is_selected()) #False
print('radio_female :', radio_female.is_selected()) #False

# Select male radio button
radio_male.click()
print("After selecting male radio button .......")
print(radio_male.is_selected()) #True
print(radio_female.is_selected()) #False

# Select male radio button
radio_female.click()
print("After selecting female radio button .......")
print(radio_male.is_selected()) #False
print(radio_female.is_selected()) #True

driver.quit()
