import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.snapdeal.com/')
driver.get('https://www.amazon.com/')

driver.back() #snapdeal
driver.forward() #amazon

driver.refresh()
driver.quit()
