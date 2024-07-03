import allure
import requests
from constants import MAIN_PAGE_URL, API_LOGIN


@allure.title('Проверка авторизации курьера')
class TestLogInCourier:

    @allure.step('Проверка возможности логина курьера при заполнении обязательных полей')
    def test_log_in_courier_positive(self, create_courier):
        response = requests.post(f'{MAIN_PAGE_URL}/{API_LOGIN}', data=create_courier)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.step('Проверка возможности логина курьера при неправильном заполнении пароля')
    @allure.description('Ожидаемый код: 404')
    def test_log_in_wrong_password_negative(self, create_courier):
        data = create_courier
        data['password'] = '123'
        response = requests.post(f'{MAIN_PAGE_URL}/{API_LOGIN}', data=data)
        assert response.status_code == 404

    @allure.step('Проверка возможности логина курьера при неправильном заполнении логина')
    @allure.description('Ожидаемый код: 404')
    def test_log_in_wrong_password_negative(self, create_courier):
        data = create_courier
        data['login'] = '123'
        response = requests.post(f'{MAIN_PAGE_URL}/{API_LOGIN}', data=data)
        assert response.status_code == 404

