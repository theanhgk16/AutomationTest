import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# driver.get('https://the-internet.herokuapp.com/basic_auth')
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

driver.maximize_window()

time.sleep(5)
