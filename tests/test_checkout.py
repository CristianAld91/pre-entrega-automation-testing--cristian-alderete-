import pytest
from page.checkout_page import CheckoutPage
from page.login_page import LoginPage
#from data.checkout_data import usuarios_checkout
from utils.helpers import load_user_csv, load_user_json

load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")
#el test_checkout se ejecutara con cada usuario del USERS y con el primer usuario del checkout_data, lo que nos permite validar el proceso de checkout.
@pytest.mark.parametrize("username, password", load_json)
def test_checkout(driver, username, password):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login_page(username, password)

    checkout_page.agregar_producto()
    checkout_page.ir_carrito()
    checkout_page.iniciar_carrito()
    checkout_page.completar_formulario()
    checkout_page.continuar()
    checkout_page.finalizar_compra()
    assert checkout_page.mensaje_exito() == True
    
    #pytest tests/test_checkout.py::test_checkout -v -s