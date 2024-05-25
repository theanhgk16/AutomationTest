# Test case
# -------------------------
# 1) open web brower(Chorme/firefox/edge)
# 2) open url ..........
# 3) enter username
# 4) enter password
# 5) click on login
# 6) capture title of the home page (Actucal title)
# 7) verify title of the page: orangeHRN (Expected)
# 8) close browser

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="C:/Webdrivers/chromedriver_win32.zip/chromedriver.exe")

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.get("https://github.com/login")

driver.find_element(By.NAME, "login").send_keys("theanhgk16@gmail.com")
driver.find_element(By.NAME, "password").send_keys("phuonganh1639@")
driver.find_element(By.NAME, "commit").click()

act_title = driver.title
exp_title = "Sign in to GitHub"

if act_title == exp_title:
    print("Logged In")

else:
    print("Login Failed")

driver.close()
