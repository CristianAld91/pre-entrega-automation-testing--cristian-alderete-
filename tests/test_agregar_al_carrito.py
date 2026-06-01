from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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