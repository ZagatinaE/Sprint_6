import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import Urls


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def order_page():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    driver.get(Urls.ORDER_PAGE)
    yield driver
    driver.quit()

