from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"
    _USERNAME = (By.ID, "user-name")
    _PASSWORD = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    #inicializar el driver y el wait
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        #metodo para abrir la pagina de login
    def open(self):
        self.driver.get(self.URL)
        #wait para que se cargue la pagina de login
    def login_page(self, username, password):
        self.wait.until(EC.presence_of_element_located(self._USERNAME)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(self._PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

