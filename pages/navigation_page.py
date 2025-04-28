from locators.navigation_page_locators import NavigationPageLocators
from pages.base_page import BasePage
import allure




class NavigationPage(BasePage):
    @allure.step('Кликнуть на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_to_element(NavigationPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть на логотип "Янлекс"')
    def click_logo_yandex(self):
        self.click_to_element(NavigationPageLocators.YANDEX_LOGO)

    @allure.step('Получить текст заголовка главной страницы')
    def get_main_title_text(self):
        return self.get_text_from_element(NavigationPageLocators.MAIN_TITLE).strip().split('\n')[0].strip()

    @allure.step('Долистать до "Все о дзене" и проверить ')
    def check_about_dzen_present(self):
        self.scroll_to_element(NavigationPageLocators.ABOUT_DZEN)
        return self.get_text_from_element(NavigationPageLocators.ABOUT_DZEN)








