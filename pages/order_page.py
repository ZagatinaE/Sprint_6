from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure



class OrderPage(BasePage):
    @allure.step('Нажать на верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click_to_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажать на нижнюю кнопку "Заказать"')
    def click_low_order_button(self):
        self.scroll_to_element(MainPageLocators.LOW_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.LOW_ORDER_BUTTON)



    @allure.step('Заполнить первую страницу заказа')
    def fill_first_page(self, order_data):
        self.add_text_to_element(OrderPageLocators.FIRST_NAME, order_data["first_name"])
        self.add_text_to_element(OrderPageLocators.LAST_NAME, order_data["last_name"])
        self.add_text_to_element(OrderPageLocators.ADDRESS, order_data["address"])
        self.click_to_element(OrderPageLocators.METRO_STATION)
        metro_locator = (By.XPATH, f"//div[text()='{order_data['metro_station']}']")
        self.click_to_element(metro_locator)
        self.add_text_to_element(OrderPageLocators.PHONE, order_data["phone"])
        self.click_to_element(OrderPageLocators.COOKIES_ACCEPT)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить вторую страницу заказа')
    def fill_second_page(self, order_data):
        self.click_to_element(OrderPageLocators.DELIVERY_DATE)
        self.add_text_to_element(OrderPageLocators.DELIVERY_DATE, order_data["delivery_date"])
        self.select_selected_date()
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element((OrderPageLocators.RENTAL_OPTION[0], OrderPageLocators.RENTAL_OPTION[1].format(order_data["rental_period"])))

        if order_data["color"] == "black":
            self.click_to_element(OrderPageLocators.COLOR_BLACK)
        else:
            self.click_to_element(OrderPageLocators.COLOR_GREY)

        self.add_text_to_element(OrderPageLocators.COMMENT, order_data["comment"])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверить успешное оформление заказа')
    def check_success_order(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_POPUP).is_displayed()