import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://nhathuoclongchau.com.vn/')
driver.maximize_window()

# Absolute Xpath
# A_Xpath = driver.find_element(By.XPATH,
#                               "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[4]/div/div[1]/span/input")
# A_Xpath.send_keys("Omega 3")
#
# A_Xpath_1 = driver.find_element(By.XPATH,
#                         "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[4]/div/div[1]/span/button[2]")
# A_Xpath_1.click()


# Relative Xpath
# A_Xpath_1 = driver.find_element(By.XPATH,
#                               "//*[@id='search_header']")
# A_Xpath_1.send_keys("Omega 3")
#
# A_Xpath_1 = driver.find_element(By.XPATH,
#                         "//*[@id='__next']/div[1]/header/div/div[2]/div/div/div[4]/div/div[1]/span/button[2]")
# A_Xpath_1.click()

# OR
# A_Xpath_2 = driver.find_element(By.XPATH,
#                               "//input[@id='search_header' or @name='']")
# A_Xpath_2.send_keys("Omega 3")
#
# A_Xpath_2 = driver.find_element(By.XPATH,
#                         "//*[@id='__next']/div[1]/header/div/div[2]/div/div/div[4]/div/div[1]/span/button[2]")
# A_Xpath_2.click()

# Contains() & start-with()
A_Xpath_3 = driver.find_element(By.XPATH,
                              "")
A_Xpath_3.send_keys("Omega 3")

A_Xpath_3 = driver.find_element(By.XPATH,
                        "//*[@id='__next']/div[1]/header/div/div[2]/div/div/div[4]/div/div[1]/span/button[2]")
A_Xpath_3.click()


time.sleep(10)
