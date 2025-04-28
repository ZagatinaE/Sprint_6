from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver=driver


    def click_to_element(self, some):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(some))
        self.driver.find_element(*some).click()


    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)


    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 25).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text


    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)


    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element) #ИЗ ДИПСИКА

    def select_selected_date(self):
        selected_date = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".react-datepicker__day--selected")
            )
        )
        selected_date.click()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])




