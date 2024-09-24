import allure
from utils.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}"
            )
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

    def find_elements(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}"
            )
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url
