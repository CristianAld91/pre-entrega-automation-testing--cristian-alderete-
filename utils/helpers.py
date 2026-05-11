#inicializar webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from page.login_page import LoginPage
#funcion para obtener el driver
def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver
#funcion para realizar login en saucedemo iniciando el driver, ingresando el usuario y contraseña y cliqueando el boton de login
def login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_page(username, password)