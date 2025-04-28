from selenium.webdriver.common.by import By



class MainPageLocators:

    QUESTION_LOCATOR = (By.ID, 'accordion__heading-{}')
    ANSWER_LOCATOR = (By.ID, 'accordion__panel-{}')
    QUESTION_LOCATOR_TO_SCROLL = (By.ID, 'accordion__heading-7')
    TOP_ORDER_BUTTON = (
    By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')][1]")
    LOW_ORDER_BUTTON = (
    By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')])[2]")
    COOKIE_CONFIRM_BUTTON = (By.ID, 'rcc-confirm-button')