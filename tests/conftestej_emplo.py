"""#revisarar hora clse 20:45

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def chrome_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    
    driver.quit()"""