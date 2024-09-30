import allure
from pages.base_page import BasePage
from utils.locators import BasePageLocator
from utils.locators import YaScooterHomePageLocator as Locators

class YaScooterHomePage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        self.click_element(Locators.TOP_ORDER_BUTTON)

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        self.click_element(Locators.BOTTOM_ORDER_BUTTON)

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        elems[question_number].click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        self.switch_to_window(window_number)

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        self.click_element(BasePageLocator.YANDEX_SITE_BUTTON)

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        self.click_element(BasePageLocator.COOKIE_ACCEPT_BUTTON)

    @allure.step('Проверить URL')
    def verify_url(self, expected_url):
        assert self.current_url() == expected_url