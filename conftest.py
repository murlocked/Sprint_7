import pytest
from user_generator import register_new_courier_and_return_login_password


@pytest.fixture(scope='function')
def create_courier_full():
    login, password, name = register_new_courier_and_return_login_password()

    data = {
        'login': login,
        'password': password,
        'firstName': name
    }

    return data


@pytest.fixture(scope='function')
def create_courier():
    login, password = register_new_courier_and_return_login_password()[:2]

    data = {
        'login': login,
        'password': password,
    }

    return data
