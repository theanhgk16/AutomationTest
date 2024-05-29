import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()

print('title :', driver.title)  #OrangeHRM
print('current_url :', driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print('page_source :', driver.page_source)

driver.quit()
time.sleep(10)

