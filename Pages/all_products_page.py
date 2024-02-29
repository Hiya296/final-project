import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class AllProducts(BasePage):
    TITLE_TEXT = (By.CSS_SELECTOR, ".title")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn_primary")
    REMOVE_FROM_CART = (By.CSS_SELECTOR, "[id*='remove']")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    SHOPPING_CART_QTY = (By.CSS_SELECTOR, ".shopping_cart_badge")
    SORT = (By.CSS_SELECTOR, ".product_sort_container > option")
    SORT_ACTIVE = (By.CSS_SELECTOR, ".active_option")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    IMAGE_ATTR = (By.TAG_NAME, "img")
    PRODUCT_BASE = (By.CSS_SELECTOR, ".inventory_item")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get products page header name")
    def page_title_text(self):
        return self.get_text(self.TITLE_TEXT)

    @allure.step("Get product name")
    def product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    @allure.step("Product selection")
    def product_list(self, title):
        self.lists(self.PRODUCT_NAME, title)

    @allure.step("Add to cart")
    def add_to_cart(self, value):
        return self.click_on_add(self.ADD_TO_CART, value)

    @allure.step("Remove from cart")
    def remove_from_cart(self):
        self.click(self.REMOVE_FROM_CART)

    @allure.step("Add all to cart")
    def add_all_to_cart(self):
        i = 0
        while i <= 5:
            if self.get_text(self.ADD_TO_CART) == "Add to cart":
                self.click(self.ADD_TO_CART)
                i += 1
            else:
                break

    @allure.step("Remove all from cart")
    def remove_all_from_cart(self):
        i = 0
        while i <= 5:
            if self.get_text(self.REMOVE_FROM_CART) == "Remove":
                self.click(self.REMOVE_FROM_CART)
                i += 1
            else:
                break

    @allure.step("Click on shopping cart")
    def shopping_cart(self):
        self.click(self.SHOPPING_CART)

    @allure.step("Shopping cart quantity")
    def shopping_cart_qty(self):
        return self.get_text(self.SHOPPING_CART_QTY)

    @allure.step("Sort list {option}")
    def sort_list(self, option):
        self.lists(self.SORT, option)

    @allure.step("Active sort option")
    def sort_active(self):
        return self.get_text(self.SORT_ACTIVE)

    @allure.step("Get image source value")
    def image_source(self, name):
        return self.image_attribute(self.IMAGE_ATTR, name)
