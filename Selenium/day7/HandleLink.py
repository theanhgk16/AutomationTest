import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# click on link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# find number of the links in a page
# links = driver.find_elements(By.TAG_NAME, 'a')
links = driver.find_elements(By.XPATH, '//a')
print("total number of links :", len(links))

# print all the link name
for link in links:
    print(link.text)

time.sleep(10)
