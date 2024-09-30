import pytest
from selenium import webdriver
import warnings
from pages.home_page import YaScooterHomePage
from pages.order_page import YaScooterOrderPage
from utils.urls import Urls

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pytest")

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_method(driver):
    ya_scooter_order_page = YaScooterOrderPage(driver)
    ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
    ya_scooter_home_page = YaScooterHomePage(driver)
    ya_scooter_home_page.click_cookie_accept()
    yield ya_scooter_order_page
    driver.quit()

@pytest.fixture(autouse=True)
def setup_home_page(driver):
    ya_scooter_home_page = YaScooterHomePage(driver)
    ya_scooter_home_page.go_to_site()
    ya_scooter_home_page.click_cookie_accept()
    return ya_scooter_home_page