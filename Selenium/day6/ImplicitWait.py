import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10) #seconds #implicitly

driver.get('https://www.google.com/')
driver.maximize_window()

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Selenium')
search_box.submit()

# time.sleep(10)
# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()

driver.quit()
