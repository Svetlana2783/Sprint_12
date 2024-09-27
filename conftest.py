import pytest
from selenium import webdriver
import warnings
from pages.home_page import YaScooterHomePage

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pytest")

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup_method(driver):
    ya_scooter_home_page = YaScooterHomePage(driver)
    ya_scooter_home_page.go_to_site()
    ya_scooter_home_page.click_cookie_accept()
    return ya_scooter_home_page