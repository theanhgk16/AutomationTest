import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.maximize_window()

print('start___')
driver.switch_to.default_content()

driver.switch_to.frame("packageListFrame")
print('start')
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
# back to default web page frame
driver.switch_to.default_content()
#
#
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.LINK_TEXT, "WebDriver").click()
# back to default web page frame
driver.switch_to.default_content()
#
#
# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
# back to default web page frame
driver.switch_to.default_content()

time.sleep(5)
