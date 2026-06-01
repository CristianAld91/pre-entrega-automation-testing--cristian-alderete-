#inicializar webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json

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
 #funcion para cargar los usuarios desde un archivo csv y devolver una lista de tuplas con el formato (username, password)   
def load_user_csv(path):
    users = []
    
    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row["username"] and row["password"]:
                users.append((row["username"], row["password"]))
    return users
#funcion para cargar los usuarios desde un archivo json y devolver una lista de tuplas con el formato (username, password)
def load_user_json(path):
    users = []
    with open(path, newline='') as file:
        data = json.load(file)
        for user in data:
            if user["username"] and user["password"]:
                users.append((user["username"], user["password"]))
    return users