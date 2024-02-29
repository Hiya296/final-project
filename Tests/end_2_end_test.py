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


@allure.epic("Function")
class Tests:

    @allure.severity(Severity.CRITICAL)
    @allure.title("1 - End to End test")
    @allure.feature("Full scenario from login to purchase confirmation")
    def test_end2end(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.add_to_cart(ProductsID.BIKE_LIGHT)
        p2.product_list(Products.FLEECE)
        p3 = SingleProduct(self.driver)
        p3.add_to_cart()
        p3.shopping_cart()
        p4 = Checkout(self.driver)
        p4.your_cart()
        p5 = YourCart(self.driver)
        p5.continue_shopping()
        p2.shopping_cart()
        p5.check_out()
        p6 = Information(self.driver)
        p6.fill_info("John", "Doe", "12345")
        p6.checkout_continue()
        p7 = Overview(self.driver)
        p7.finish_purchase()
        p8 = Complete(self.driver)
        expected = PagesTitle.COMPLETE
        actual = p8.title()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
