import pytest

from utils.helpers import get_driver
#decorador para inicializar el driver antes de cada test y cerrarlo despues de cada test
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
    