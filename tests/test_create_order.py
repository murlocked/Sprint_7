import allure
import pytest
import requests
from constants import MAIN_PAGE_URL, API_ORDERS


@allure.title('Проверка создания заказа')
@allure.description('При создании заказа можно указать один цвет, '
                    'оба цвета (BLACK, GREY) или не указывать цвет вовсе. '
                    'В теле ответа содержится слово track')
@pytest.mark.parametrize('color_value', ['BLACK', 'GREY', ('BLACK', 'GREY'), None])
class TestCreateOrder:
    def test_create_order(self, color_value):
        order = {
            'firstName': 'Naruto',
            'lastName': 'Uchiha',
            'address': 'Konoha, 142 apt.',
            'metroStation': 4,
            'phone': '+7 800 355 35 35',
            'rentTime': 5,
            'deliveryDate': '2020-06-06',
            'comment': 'Saske, come back to Konoha',
            'color': color_value
        }
        response = requests.post(f'{MAIN_PAGE_URL}/{API_ORDERS}', data=order)
        assert 'track' in response.json() and response.status_code == 201
