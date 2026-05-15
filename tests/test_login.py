from page.login_page import LoginPage
from data.users import USERS
import pytest
@pytest.mark.parametrize("username, password", USERS )
def test_login(driver, username, password):
    """ try:
        LoginPage(driver).login_page(username, password)
        LoginPage(driver).open(
            username, password
        )
        
    except Exception as e:
        print("Error en test_login:", e)
        print("HTML de la página:", driver.page_source)
    """
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(username, password)