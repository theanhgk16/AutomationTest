import time
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.select import Select

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()

# drp_country_element = driver.find_element(By.XPATH, "//select[@id='input-country']")
# print('drp_country_element :', drp_country_element)
# drp_country = Select(driver.find_element(By.ID, "//select[@id='input-country']"))
# print('drp_country :', drp_country)

# Select option for the dropdown
# drp_country.select_by_visible_text("India")
# # drp_country.select_by_value("10") #Argentina
# # drp_country.select_by_index(13) #index

# capture all the options and print them
# all_options = drp_country.options
# print("total number of options: ", len(all_options))
#
# for option in all_options:
#     print(option.text)

# select option from dropdown without using built-in method
# for option in all_options:
#     if option.text == "India":
#         option.click()
#         break

all_options = driver.find_elements(By.XPATH, "//*[@id='input-country]/option")
print(len(all_options))

time.sleep(10)
