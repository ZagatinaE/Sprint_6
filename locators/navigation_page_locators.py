from selenium.webdriver.common.by import By



class NavigationPageLocators:
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    MAIN_TITLE = (By.CLASS_NAME, "Home_Header__iJKdX")
    SNACKBAR_DZEN = (By.XPATH, "//div[contains(@class, 'recommend-tech-snackbar__title') and contains(text(), 'В Дзене применяются')]")



