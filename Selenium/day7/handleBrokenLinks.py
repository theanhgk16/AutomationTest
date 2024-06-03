import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)
    except:
        print('None---: ', None)

    if response.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, " is valid links")

print("Total number of broken links :", count)
