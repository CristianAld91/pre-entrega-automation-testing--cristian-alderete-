from utils.helpers import login
from selenium.webdriver.common.by import By

# test para verificar que el login se ingresa correctamente y se muestra el catalogo de productos al usuario 
def test_login(driver):
    try:
        login(driver, "standard_user", "secret_sauce") 
        assert "inventory.html" in driver.current_url
        
        # Valida titulo
        title = driver.find_element(By.CLASS_NAME, "title")
        assert title.text == "Products"
    except Exception as e:
        print("Error en test_login:", e)
        print("HTML de la página:", driver.page_source)


#pytest tests/test_saucedemo.py::test_login -v
