import pytest
from page.checkout_page import CheckoutPage
from page.login_page import LoginPage
from data.checkout_data import usuarios_checkout
from data.users import USERS

@pytest.mark.parametrize("username, password", USERS )
@pytest.mark.parametrize("checkout_data", [usuarios_checkout[0]])

def test_checkout(driver, username, password, checkout_data):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login_page(username, password)

    checkout_page.agregar_producto()
    checkout_page.ir_carrito()
    checkout_page.iniciar_carrito()
    checkout_page.completar_formulario(checkout_data)
    checkout_page.continuar()
    checkout_page.finalizar_compra()
    assert checkout_page.mensaje_exito() == True