import allure
from allure_commons.types import Severity

from External.data import *
from Pages.any_product_page import SingleProduct
from Pages.checkout_page import Checkout
from Pages.complete_page import Complete
from Pages.home_page import Main
from Pages.all_products_page import AllProducts
from Pages.information_page import Information
from Pages.overview_page import Overview
from Pages.your_cart_page import YourCart


@allure.severity(Severity.CRITICAL)
@allure.epic("Function")
@allure.feature("Checkout processes testing")
class Tests:

    @allure.severity(Severity.CRITICAL)
    @allure.title("18 - Missing information")
    @allure.feature("Continue with checkout without all or some information")
    def test_missing_information(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.product_list(Products.FLEECE)
        p3 = SingleProduct(self.driver)
        p3.add_to_cart()
        p3.shopping_cart()
        p4 = Checkout(self.driver)
        p4.your_cart()
        p5 = YourCart(self.driver)
        p5.check_out()
        p6 = Information(self.driver)
        p6.fill_info("", "", "")
        p6.checkout_continue()
        expected = ErrorMsgs.NO_FIRST
        actual = p6.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
        p6.fill_info("John", "", "")
        p6.checkout_continue()
        expected = ErrorMsgs.NO_LAST
        actual = p6.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
        p6.fill_info("John", "Doe", "")
        p6.checkout_continue()
        expected = ErrorMsgs.NO_POSTAL
        actual = p6.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.CRITICAL)
    @allure.title("19 - Cancel process (information)")
    @allure.feature("Cancel checkout and return to cart")
    def test_cancel_information(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.product_list(Products.FLEECE)
        p3 = SingleProduct(self.driver)
        p3.add_to_cart()
        p3.shopping_cart()
        p4 = Checkout(self.driver)
        p4.your_cart()
        p5 = YourCart(self.driver)
        p5.check_out()
        p6 = Information(self.driver)
        p6.fill_info("John", "Doe", "12345")
        p6.cancel_checkout()
        expected = PagesTitle.CART_PAGE
        actual = p5.page_title_text()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.CRITICAL)
    @allure.title("20 - Cancel process (purchase)")
    @allure.feature("Cancel before complete the purchase and return to products page")
    def test_cancel_purchase(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.product_list(Products.FLEECE)
        p3 = SingleProduct(self.driver)
        p3.add_to_cart()
        p3.shopping_cart()
        p4 = Checkout(self.driver)
        p4.your_cart()
        p5 = YourCart(self.driver)
        p5.check_out()
        p6 = Information(self.driver)
        p6.fill_info("John", "Doe", "12345")
        p6.checkout_continue()
        p7 = Overview(self.driver)
        p7.cancel_purchase()
        expected = PagesTitle.PRODUCTS_PAGE
        actual = p2.page_title_text()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
