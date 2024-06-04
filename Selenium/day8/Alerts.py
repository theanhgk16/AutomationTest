import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://demoqa.com/alerts')
driver.maximize_window()
alert = Alert(driver)

# Opens alert window
driver.find_element(By.ID, "promtButton").click()

time.sleep(5)

alert_window = driver.switch_to.alert
print("alert_window :", alert_window.text)
alert_window.send_keys("Welcome")

# alert_window.accept() #close alert window by using OK button
alert_window.dismiss() #close alert window by using Cancel button
