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

Status code:

    Errorcode 400 - Bad Request
    Errorcode 401 - Unauthorized
    Errorcode 402 - Payment Required
    Errorcode 403 - Forbidden
    Errorcode 404 - Not Found
    Errorcode 405 - Method Not Allowed
    Errorcode 406 - Not Acceptable
    Errorcode 407 - Proxy Authentication Required
    Errorcode 408 - Request Timeout
    Errorcode 409 - Conflict
    Errorcode 410 - Gone
    Errorcode 411 - Length Required
    Errorcode 412 - Precondition Failed
    Errorcode 413 - Request Entity Too Large
    Errorcode 414 - Request-URI Too Long
    Errorcode 415 - Unsupported Media Type
    Errorcode 416 - Requested Range Not Satisfiable
    Errorcode 417 - Expectation Failed
    Errorcode 420 - Enhance Your Calm
    Errorcode 422 - Unprocessable Entity
    Errorcode 423 - Locked
    Errorcode 424 - Failed Dependency
    Errorcode 429 - Too Many Requests
    Errorcode 431 - Request Header Fields Too Large
    Errorcode 450 - Blocked by Windows Parental Controls
    Errorcode 500 - Internal Server Error
    Errorcode 501 - Not Implemented
    Errorcode 502 - Bad Gateway
    Errorcode 503 - Service Unavailable
    Errorcode 504 - Gateway Timeout
    Errorcode 505 - HTTP Version Not Supported
    Errorcode 506 - Variant Also Negotiates
    Errorcode 507 - Insufficient Storage
    Errorcode 509 - Bandwidth Limit Exceeded
    Errorcode 510 - Not Extended
