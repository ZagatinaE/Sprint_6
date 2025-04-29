from conftest import order_page
import allure
from pages.navigation_page import NavigationPage



@allure.feature('Тесты навигации')
class TestNavigation:
    @allure.title('Тест перехода на главную страницу через лого Самоката')
    def test_go_to_main_page_from_scooter_logo(self, order_page):
        navigation_page = NavigationPage(order_page)
        navigation_page.click_scooter_logo()
        assert navigation_page.get_main_title_text() == "Самокат"


    @allure.title('Тест перехода в Дзен через логотип Яндекса')
    def test_go_to_dzen_from_yandex_logo(self, order_page):
        navigation_page = NavigationPage(order_page)
        navigation_page.click_logo_yandex()
        navigation_page.switch_to_new_tab()

        navigation_page.check_about_dzen_present()
        assert navigation_page.check_about_dzen_present() == "В Дзене применяются"























