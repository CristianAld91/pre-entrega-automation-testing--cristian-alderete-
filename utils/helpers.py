#inicializar webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#funcion para obtener el driver
def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver
#funcion para realizar login en saucedemo iniciando el driver, ingresando el usuario y contraseña y cliqueando el boton de login
def login(driver, username, password):
    #wait para que se cargue la pagina de login
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    #ingresar usuario y contraseña y cliqueando el boton de login
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
