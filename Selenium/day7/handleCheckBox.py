import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://artoftesting.com/samplesiteforselenium')
driver.maximize_window()

# 1) select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='male']").click()
# driver.find_element(By.CLASS_NAME, 'Automation').click()

# 2) select all the checkbox
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@class, 'value')]")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

#Appraoch1
# for i in range(len(checkbox)):
#     checkbox[i].click()

#Appraoch2
# for checkbox in checkboxes:
#     checkbox.click()

# 3) select multiple checkboxes by choices
# for checkbox in checkboxes:
#     name = checkbox.get_attribute('class')
#     print('start')
#     if name == "Automation" or "Performance":
#         checkbox.click()

# 4) select element last checkboxes
#total number of elements - 1 = strating index
# for i in range(len(checkboxes)-1, len(checkboxes)):
#     checkboxes[i].click()

# 5) select element first checkboxes
#total number of elements - 1 = strating index
# for i in range(len(checkboxes)):
#     if i < 1:
#         checkboxes[i].click()

# 6) clearing all the checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()

time.sleep(10)
driver.quit()
