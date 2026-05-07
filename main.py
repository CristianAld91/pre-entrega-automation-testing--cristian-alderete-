"""from selenium import webdriver
from selenium.webdriver.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftestej_emplo import chrome_driver

wait = WebDriverWait(chrome_driver, 10)
chrome_driver.get("https://www.google.com")

try:
    input_google = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
    )
    input_google.send_keys("Selenium WebDriver")
    input_google.send_keys(Keys.RETURN)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    
    chrome_driver.quit()   """