import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class YourCart(BasePage):
    TITLE_TEXT = (By.CSS_SELECTOR, ".title")
    CHECK_OUT = (By.CSS_SELECTOR, "#checkout")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#continue-shopping")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_FROM_CART = (By.CSS_SELECTOR, "[id*='remove']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Product name in cart")
    def cart_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    @allure.step("Check out")
    def check_out(self):
        self.click(self.CHECK_OUT)

    @allure.step("Go back and continue shopping")
    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    @allure.step("Remove from cart")
    def remove_from_cart(self):
        self.click(self.REMOVE_FROM_CART)

    @allure.step("Get your cart page header name")
    def page_title_text(self):
        return self.get_text(self.TITLE_TEXT)
