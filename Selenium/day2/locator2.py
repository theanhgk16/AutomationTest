import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.alibaba.com/')
driver.maximize_window()

# ClassName and TagName
sliders = driver.find_elements(By.CLASS_NAME, 'industry-row')
print("Slider :", len(sliders)) #total number of slider: 22 on home page

links = driver.find_elements(By.TAG_NAME, 'a')
print("Links :", len(links)) #total number of links: 226 on home page

time.sleep(5)