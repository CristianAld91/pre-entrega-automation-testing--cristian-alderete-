from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
