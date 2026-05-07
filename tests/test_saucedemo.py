from utils.helpers import login
from selenium.webdriver.common.by import By
# test para verificar que el login se realiza correctamente y se muestra el catalogo de productos despues de iniciar sesion
def test_login(driver):
    login(driver, "standard_user", "secret_sauce") 
    assert "inventory.html" in driver.current_url
    
    title = driver.find_element(By.CLASS_NAME, "title")
    assert title.text == "Products"
# test para verificar que el catalogo de productos se muestra correctamente despues de iniciar sesion  
def test_catalogo_productos(driver):
    login(driver, "standard_user", "secret_sauce")
    
    title = driver.find_element(By.CLASS_NAME, "title")
    assert title.text == "Products"
    #validar que se muestran los productos en el catalogo
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    