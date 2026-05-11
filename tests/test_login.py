from page.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login(driver):
    try:
        LoginPage(driver).login_page("standard_user", "secret_sauce")
        LoginPage(driver).open(
            "standard_user", "secret_sauce"
        )
        
    except Exception as e:
        print("Error en test_login:", e)
        print("HTML de la página:", driver.page_source)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_page("standard_user", "secret_sauce")
