import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@title='Sign in']").click() #Login button
time.sleep(5)
driver.switch_to.alert.accept()

time.sleep(5)
