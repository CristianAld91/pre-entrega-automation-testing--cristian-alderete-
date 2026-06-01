from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# test para verificar que el catalogo de productos se muestra correctamente 
def test_catalogo_productos(driver):
    try:
        login(driver, "standard_user", "secret_sauce")
        #valida titulo
        title = driver.find_element(By.CLASS_NAME, "title")
        assert title.text == "Products"
        
        # Valida que se muestran los productos en el catalogo
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0
        
        nombre_producto = productos[0].find_element(By.CLASS_NAME, "inventory_item_name")
        assert nombre_producto.text == "Sauce Labs Backpack"
    except Exception as e:
        print("Error en test_catalogo_productos:", e)
        print("HTML de la página:", driver.page_source)
    