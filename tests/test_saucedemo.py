from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
    
    
#tipos de ejecucion:
#pytest tests/test_saucedemo.py -v
#tests/test_sausedemo.py::test_catalogo_productos -v
#pytest tests/test_saucedemo.py::test_login -v

#validar que se pueda agregar un producto al carrito de compras
def test_agregar_producto_al_carrito(driver):
    login(driver, "standard_user", "secret_sauce")
    #wait para que se cargue el catalogo de productos
    wait = WebDriverWait(driver, 10)
    #declaramos el nombre del producto a agregar al carrito de compras
    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    #verificar que el producto esta ticketeado en el catalogo
    boton_add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
    boton_add_to_cart.click()
    #valida carrito de compras
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carrito.text >= "1"
    #click en el carrito de compras
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    #valida que el producto agregado al carrito se muestra en la pagina del carrito de compras
    producto_carrito  = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert producto_carrito.text == nombre_producto
    
    #pytest tests/test_saucedemo.py::test_agregar_producto_al_carrito -v
    
def test_menu_lateral(driver):
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)
    
    # Click en el menu lateral
    menu_lateral = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
    menu_lateral.click()
    
    # Valida que los elementos del menu se muetran correctamente
    try:
        elemento_menu = wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link"))).text
        assert elemento_menu == "All Items"
        
        elemento_menu = driver.find_element(By.ID, "about_sidebar_link").text
        assert elemento_menu == "About"
        
        elemento_menu = driver.find_element(By.ID, "logout_sidebar_link").text
        assert elemento_menu == "Logout"
        
        elemento_menu = driver.find_element(By.ID, "reset_sidebar_link").text
        assert elemento_menu == "Reset App State"
    
    except Exception as e:
        print("Error:", e)
        print("HTML de la página:", driver.page_source)
