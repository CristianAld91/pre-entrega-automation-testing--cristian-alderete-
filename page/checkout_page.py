from selenium.webdriver.common.by import By

class CheckoutPage:
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack") #delcaramos el localizador del boton agregar al carrito
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link") #declaramos el localizador del boton carrito
    CHECK_BUTTON_CART = (By.ID, "checkout") #declaramos el localizador del boton checkout
    FIRS_NAME = (By.ID, "first-name") #declaramos el localizador del campo first name
    LAST_NAME = (By.ID, "last-name") #declaramos el localizador del campo last name
    POSTAL_CODE = (By.ID, "postal-code") #declaramos el local
    CONTINUE = (By.ID, "continue") #declaramos el localizador del boton continue
    FINISH = (By.ID, "finish") #declaramos el localizador del boton finish
    COMPLETE_SUCESS = (By.CLASS_NAME, "complete-header") #declaramos el localizador del mensaje de compra exitosa
    
    def __init__(self, driver):
        self.driver = driver
        
    def agregar_producto(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def ir_carrito(self):
        self.driver.find_element(*self.CART_BUTTON).click()
     
    def iniciar_carrito(self):
        self.driver.find_element(*self.CHECK_BUTTON_CART).click()

    def completar_formulario(self, usuario):
        self.driver.find_element(*self.FIRS_NAME).send_keys(usuario['first_name'])
        self.driver.find_element(*self.LAST_NAME).send_keys(usuario['last_name'])
        self.driver.find_element(*self.POSTAL_CODE).send_keys(usuario['postal_code'])

    def continuar(self):
        self.driver.find_element(*self.CONTINUE).click()
    
    def finalizar_compra(self):
        self.driver.find_element(*self.FINISH).click()    
        
    def mensaje_exito(self):
        try:
            return self.driver.find_element(*self.COMPLETE_SUCESS).is_displayed()   
        except:
            return False