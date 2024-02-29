import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Information(BasePage):
    TITLE_TEXT = (By.CSS_SELECTOR, ".title")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#last-name")
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE = (By.CSS_SELECTOR, "#continue")
    CANCEL = (By.CSS_SELECTOR, "#cancel")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Fill your information with:\n"
                 "First name: {first_name}\n"
                 "Last name: {last_name}\n"
                 "Zip Code: {zip_code}")
    def fill_info(self, first_name, last_name, zip_code):
        self.fill_text(self.FIRST_NAME_FIELD, first_name)
        self.fill_text(self.LAST_NAME_FIELD, last_name)
        self.fill_text(self.ZIP_CODE_FIELD, zip_code)

    @allure.step("Continue with checkout")
    def checkout_continue(self):
        self.click(self.CONTINUE)

    @allure.step("Cancel checkout")
    def cancel_checkout(self):
        self.click(self.CANCEL)

    @allure.step("Get information page header name")
    def page_title_text(self):
        return self.get_text(self.TITLE_TEXT)

    @allure.step("Get error message")
    def error_message(self):
        return self.get_text(self.ERROR_MSG)
