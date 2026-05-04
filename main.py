from selenium import webdriver
from selenium.webdriver.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")

input_google = driver.find_element(By.NAME, "q")
input_google.send_keys("Selenium WebDriver")
input_google.send_keys(Keys.RETURN)
driver.quit()