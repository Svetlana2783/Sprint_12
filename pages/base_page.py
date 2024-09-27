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

    def click_element(self, locator, time=10):
        element = self.find_element(locator, time)
        element.click()

    def send_keys_to_element(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.send_keys(text)

    def get_element_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    def is_element_displayed(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.is_displayed()

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    def switch_to_window(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))