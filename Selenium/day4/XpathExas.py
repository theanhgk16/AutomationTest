import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://money.rediff.com/gainers')
driver.maximize_window()

# Ancester
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Bal Pharma Ltd')]/ancestor::tr").text
# print(text_msg)

# Descendant
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Bal Pharma Ltd')]/ancestor::tr/descendant::*").text
# print(text_msg)
# print("Number of nodes:", len(text_msg))

# Following
# text_msg = driver.find_elements(By.XPATH, "//a[contains(text(), 'Bal Pharma Ltd')]/ancestor::tr/following::*")
# print(text_msg)
# print("Number of nodes:", len(text_msg))

# Following-sibling
# text_msg = driver.find_elements(By.XPATH,
#                                "//a[contains(text(), 'Bal Pharma Ltd')]/ancestor::tr/following-sibling::tr")
# print(text_msg)
# print("Number of nodes:", len(text_msg))

# Preceding
# text_msg = driver.find_elements(By.XPATH, "//a[contains(text(), 'Bal Pharma Ltd')]/ancestor::tr/preceding::*")
# print(text_msg)
# print("Number of nodes:", len(text_msg))

# Preceding-sibling
text_msg = driver.find_elements(By.XPATH, "//a[contains(text(), 'Bal Pharma Ltd')]/ancestor::tr/preceding-sibling::tr")
print(text_msg)
print("Number of nodes:", len(text_msg))

time.sleep(10)
