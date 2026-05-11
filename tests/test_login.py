from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from data.users import USERS
import pytest
@pytest.mark.parametrize("username, password", USERS [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])
def test_login(driver, username, password):
    try:
        LoginPage(driver).login_page(username, password)
        LoginPage(driver).open(
            username, password
        )
        
    except Exception as e:
        print("Error en test_login:", e)
        print("HTML de la página:", driver.page_source)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_page("standard_user", "secret_sauce")
