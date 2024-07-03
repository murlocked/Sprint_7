import allure
import requests
from user_generator import register_new_courier_and_return_login_password
from constants import MAIN_PAGE_URL, API_COURIER


@allure.title('Проверка возможности создания курьера')
@allure.description('Ожидаемый код: 201')
class TestCreateCourier:
    @allure.step('Проверка возможности создания курьера с заполнением всех полей')
    def test_create_courier_positive(self):
        assert register_new_courier_and_return_login_password()

    @allure.step('Проверка возможности создания двух одинаковых курьеров')
    @allure.description('Ожидаемый код: 409')
    def test_create_courier_duplicate_negative(self, create_courier_full):
        response = requests.post(f'{MAIN_PAGE_URL}/{API_COURIER}', data=create_courier_full)
        assert response.status_code == 409

    @allure.step('Проверка возможности создания курьера без заполнения поля "Пароль"')
    @allure.description('Ожидаемый код: 400')
    def test_create_courier_without_password_negative(self):
        data = {
            'login': 'pewpew',
            'password': None,
            'firstName': 'pewpew'
        }
        response = requests.post(f'{MAIN_PAGE_URL}/{API_COURIER}', data=data)
        assert response.status_code == 400

    @allure.step('Проверка возможности создания курьера без передачи в ручку всех полей')
    @allure.description('Ожидаемый код: 400')
    def test_create_courier_without_one_field_negative(self):
        data = {
            'login': 'pewpew',
            'firstName': 'pewpew'
        }
        response = requests.post(f'{MAIN_PAGE_URL}/{API_COURIER}', data=data)
        assert response.status_code == 400

    @allure.step('Проверка возможности создания курьера с существующим логином')
    @allure.description('Ожидаемый код: 409')
    def test_create_courier_with_existing_login(self, create_courier):
        existing_login = create_courier['login']

        data = {
            'login': existing_login,
            'password': '123`',
            'firstName': 'pewpew'
        }

        response = requests.post(f'{MAIN_PAGE_URL}/{API_COURIER}', data=data)
        assert response.status_code == 409
