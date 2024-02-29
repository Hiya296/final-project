import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class SingleProduct(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn_primary")
    REMOVE_FROM_CART = (By.CSS_SELECTOR, "[id*='remove']")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    SHOPPING_CART_QTY = (By.CSS_SELECTOR, ".shopping_cart_badge")
    BACK = (By.CSS_SELECTOR, "#back-to-products")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_details_name")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Product name")
    def product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    @allure.step("Add to cart")
    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    @allure.step("Remove from cart")
    def remove_from_cart(self):
        self.click(self.REMOVE_FROM_CART)

    @allure.step("Go back to products")
    def go_back(self):
        self.click(self.BACK)

    @allure.step("Click on shopping cart")
    def shopping_cart(self):
        self.click(self.SHOPPING_CART)

    @allure.step("Shopping cart quantity")
    def shopping_cart_qty(self):
        return self.get_text(self.SHOPPING_CART_QTY)

    @allure.step("Sort list options")
    def sort_list(self, option):
        self.lists(self.SORT, option)
