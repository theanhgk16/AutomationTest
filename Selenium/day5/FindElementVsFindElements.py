import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://demo.nopcommerce.com/')

# find_element() - return single web element

#1)Locator matching with single webelement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys('T-shirts')

#2)Locator matching with multiple webelement
element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(element.text) #Print first link from the footer "Sitemap"

time.sleep(10)
