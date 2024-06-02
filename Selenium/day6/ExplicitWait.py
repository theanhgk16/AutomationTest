import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

my_wait = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception
    ])

driver.get('https://www.google.com/')
driver.maximize_window()

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Selenium')
search_box.submit()

search_link = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()

driver.quit()
