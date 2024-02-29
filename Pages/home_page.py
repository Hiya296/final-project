import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Main(BasePage):

    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Login with user name: {user_name} and password: {password}")
    def login(self, user_name, password):
        self.fill_text(self.USER_NAME, user_name)
        self.fill_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    @allure.step("Get error message")
    def error_message(self):
        return self.get_text(self.ERROR_MSG)
