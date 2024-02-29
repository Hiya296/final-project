import allure
from allure_commons.types import Severity
from selenium.common import NoSuchElementException

from Pages.any_product_page import SingleProduct
from Pages.home_page import Main
from Pages.all_products_page import AllProducts
from External.data import *


@allure.severity(Severity.CRITICAL)
@allure.epic("Function")
@allure.feature("Single product page testing")
class Tests:

    @allure.severity(Severity.CRITICAL)
    @allure.title("15 - Go back to products page")
    @allure.feature("Enter to product page and go back to products page")
    def test_insert_go_back(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.product_list(Products.ONESIE)
        p3 = SingleProduct(self.driver)
        p3.go_back()
        expected = PagesTitle.PRODUCTS_PAGE
        actual = p2.page_title_text()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.NORMAL)
    @allure.title("16 - Add product to cart")
    @allure.feature("Add product to cart from product page")
    def test_add_product(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.product_list(Products.ONESIE)
        p3 = SingleProduct(self.driver)
        p3.add_to_cart()
        expected = str(1)
        actual = p3.shopping_cart_qty()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.NORMAL)
    @allure.title("17 - Remove product from cart")
    @allure.feature("Remove product from cart from product page")
    def test_remove_product(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.product_list(Products.ALL_THINGS)
        p3 = SingleProduct(self.driver)
        p3.add_to_cart()
        p3.remove_from_cart()
        try:
            p3.shopping_cart_qty()
            assert False
        except NoSuchElementException:
            pass
