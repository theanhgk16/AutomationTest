# AutomationTest
tạo môi trường ảo:
    python -m venv venv
    -> venv\Scripts\activate.bat

Selenium webdriver

What is WebDriver?
-> Web driver

Download Browser:

Chrome:

https://sites.google.com/chromium.org/driver/

Edge:

https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox:

https://github.com/mozilla/geckodriver/releases

Safari:

https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Lưu ý:

    from selenium.webdriver.common.by import By
    Next use this API:
    
    Old API	New API:
    
    find_element_by_id(‘id’)	find_element(By.ID, ‘id’)
    find_element_by_name(‘name’)	find_element(By.NAME, ‘name’)
    find_element_by_xpath(‘xpath’)	find_element(By.XPATH, ‘xpath’)