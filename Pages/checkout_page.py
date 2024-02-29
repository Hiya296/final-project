import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Checkout(BasePage):
    TITLE_TEXT = (By.CSS_SELECTOR, ".title")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Your Cart page options")
    def your_cart(self):
        self.click(self.SHOPPING_CART)

    @allure.step("Get products page header name")
    def page_title_text(self):
        return self.get_text(self.TITLE_TEXT)
