from selenium.webdriver.common.by import By



class OrderPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    COOKIES_ACCEPT = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")

    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle')]")

    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_POPUP = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")