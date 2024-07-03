import allure
import requests
from constants import MAIN_PAGE_URL, API_ORDERS


@allure.title('Проверка возвращения списка заказов в теле ответа')
class TestOrderList:
    def test_order_list(self):
        response = requests.get(f'{MAIN_PAGE_URL}/{API_ORDERS}/?limit=1')

        assert 'orders' in response.json()
