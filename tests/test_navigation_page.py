from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.navigation_page import NavigationPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.set_preference("dom.webdriver.enabled", False)
    driver = webdriver.Firefox(options=options)
    driver.get('https://qa-scooter.praktikum-services.ru/order')
    yield driver
    driver.quit()



@allure.feature('Тесты навигации')
class TestNavigation:
    @allure.title('Тест перехода на главную страницу через лого Самоката')
    def test_go_to_main_page_from_scooter_logo(self, driver):
        navigation_page = NavigationPage(driver)
        navigation_page.click_scooter_logo()
        assert navigation_page.get_main_title_text() == "Самокат"





    @allure.title('Тест перехода в Дзен через логотип Яндекса')
    def test_go_to_dzen_from_yandex_logo(self, driver):
        navigation_page = NavigationPage(driver)
        navigation_page.click_logo_yandex()
        navigation_page.switch_to_new_tab()

        about_dzen = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a.dzen-layout--sidebar-meta-links__link-3E")
            )
        )
        assert about_dzen.get_attribute("aria-label") == "Всё о Дзене"






















