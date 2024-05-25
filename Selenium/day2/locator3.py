import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.facebook.com/')
driver.maximize_window()

# CSS selectors:
# 1) tag - id                 : tagName#valueOfId
# 2) tag - class              : tagName.valueOfClass
# 3) tag - attribute          : tagName[attribute=value]
# 4) tag - class - attribute  : tagName.valueOfClass[attribute=value]

# 1) tag - id
# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, '#email').send_keys('abc@gmail.com')

# 2) tag - class
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, '.inputtext').send_keys('abc@gmail.com')

# 3) tag - attribute
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid="royal_email"]').send_keys('abcd@gmail.com')
# driver.find_element(By.CSS_SELECTOR, '[data-testid="royal_email"]').send_keys('abcd@gmail.com')

# 4) tag - class - attribute
driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid="royal_email"]').send_keys('abcde@gmail.com')

time.sleep(5)
