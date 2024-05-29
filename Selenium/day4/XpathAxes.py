import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()

# Self
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Honda India Power')]/self::a").text
# print(text_msg) #Honda Indiwera Power

# Parent
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Honda India Power')]/parent::td").text
# print(text_msg) #Honda Indiwera Power

# Child
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Honda India Power')]/ancestor::tr/child::td").text
# print(text_msg) #Honda Indiwera Power
child = driver.find_elements(By.XPATH, "//a[contains(text(),'Honda India Power')]/ancestor::tr/child::td")
print(len(child)) #6



driver.close()
time.sleep(10)
