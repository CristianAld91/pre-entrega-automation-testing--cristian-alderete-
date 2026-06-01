from page.login_page import LoginPage
#from data.users import USERS
import pytest
from utils.helpers import load_user_csv
from utils.helpers import load_user_json
from faker import Faker

load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")
fake = Faker()
#@pytest.mark.parametrize("username, password", USERS )
@pytest.mark.parametrize("username, password", load_json)
#@pytest.mark.parametrize("username, password", load_csv)

def test_login(driver, username, password):
    login = LoginPage(driver)

    login.open()
    login.login_page(username, password)

    name = fake.name()
    first_name =fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    codigo_postal = fake.postcode()
    
    print("datos generados:", name, first_name, last_name, email, codigo_postal)
    #pytest tests/test_login.py::test_login -v -s (mostar datos de faker con -s)