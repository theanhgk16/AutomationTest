import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.alibaba.com/')
# maxsize the browser window
driver.maximize_window()

# id & name locator
# driver.find_element(By.ID, "js-search").send_keys("Dell")
# driver.find_element(By.NAME, "q").send_keys("dell")

# linktext & partial linktext
# driver.find_element(By.LINK_TEXT, "Sign up").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Sig").click()

# driver.close()
# driver.quit()
time.sleep(5)
