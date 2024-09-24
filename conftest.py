import pytest
from selenium import webdriver
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pytest")

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()