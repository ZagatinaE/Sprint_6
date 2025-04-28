import pytest
from locators.order_page_locators import OrderPageLocators
from conftest import driver
import allure
from data import TestData
from pages.order_page import OrderPage



@allure.feature('Тесты заказа самоката')
class TestOrderScooter:
    def _complete_order_flow(self, order_page, order_data):
        with allure.step('Заполняем форму заказа и принимаем куки'):
            order_page.fill_first_page(order_data)
            order_page.fill_second_page(order_data)

        with allure.step('Подтверждаем заказ'):
            order_page.confirm_order()

        with allure.step('Проверяем успешное оформление'):
            assert order_page.check_success_order(), "Не появилось подтверждение заказа"
            success_text = order_page.get_text_from_element(OrderPageLocators.SUCCESS_POPUP)
            assert "Заказ оформлен" in success_text, f"Неверный текст подтверждения: {success_text}"

    @allure.title('Заказ через верхнюю кнопку')
    @pytest.mark.parametrize('order_data', TestData.ORDER_DATA)
    def test_order_top_button(self, driver, order_data):
        order_page = OrderPage(driver)
        with allure.step('Нажимаем верхнюю кнопку "Заказать"'):
            order_page.click_top_order_button()
        self._complete_order_flow(order_page, order_data)


    @allure.title('Заказ через нижнюю кнопку')
    @pytest.mark.parametrize('order_data', TestData.ORDER_DATA)
    def test_order_low_button(self, driver, order_data):
        order_page = OrderPage(driver)
        with allure.step('Нажимаем нижнюю кнопку "Заказать"'):
            order_page.click_low_order_button()
        self._complete_order_flow(order_page, order_data)
