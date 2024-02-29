import time

import allure
from allure_commons.types import Severity
from selenium.common import NoSuchElementException

from Pages.any_product_page import SingleProduct
from Pages.home_page import Main
from Pages.all_products_page import AllProducts
from External.data import *


@allure.severity(Severity.NORMAL)
@allure.epic("Function")
@allure.feature("Products page testing")
class Tests:

    @allure.severity(Severity.NORMAL)
    @allure.title("8 - Open a product page")
    @allure.feature("Click on any product and open it's page for more details")
    def test_open_product(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.product_list(Products.BIKE_LIGHT)
        expected = Products.BIKE_LIGHT
        p3 = SingleProduct(self.driver)
        actual = p3.product_name()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.NORMAL)
    @allure.title("9 - Add product to cart")
    @allure.feature("Add product to cart from products page")
    def test_add_product(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.add_to_cart(ProductsID.FLEECE)
        expected = str(1)
        actual = p2.shopping_cart_qty()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.NORMAL)
    @allure.title("10 - Remove product from cart")
    @allure.feature("Remove product from cart from products page")
    def test_remove_product(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.add_to_cart(ProductsID.T_SHIRT)
        p2.remove_from_cart()
        try:
            p2.shopping_cart_qty()
            assert False
        except NoSuchElementException:
            pass

    @allure.severity(Severity.NORMAL)
    @allure.title("11 - Add all products")
    @allure.feature("Add all products to cart from products page")
    def test_add_all_products(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.add_all_to_cart()
        expected = "6"
        actual = p2.shopping_cart_qty()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.NORMAL)
    @allure.title("12 - Remove all products")
    @allure.feature("Remove all products from cart from products page")
    def test_remove_all_products(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.add_all_to_cart()
        p2.remove_all_from_cart()
        try:
            p2.shopping_cart_qty()
            assert False
        except NoSuchElementException:
            pass

    @allure.severity(Severity.NORMAL)
    @allure.title("13 - List sorting")
    @allure.feature("Sort the product list using all options")
    def test_sort(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        p2.sort_list(Sort.LOHI)
        expected = Sort.LOHI
        actual = p2.sort_active()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
        time.sleep(2)
        p2.sort_list(Sort.AZ)
        expected = Sort.AZ
        actual = p2.sort_active()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
        time.sleep(2)
        p2.sort_list(Sort.HILO)
        expected = Sort.HILO
        actual = p2.sort_active()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
        time.sleep(2)
        p2.sort_list(Sort.ZA)
        expected = Sort.ZA
        actual = p2.sort_active()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.severity(Severity.NORMAL)
    @allure.title("14 - Comparing images.")
    @allure.feature("Comparing actual image with expected image. \n This test should failed")
    def test_compare_images(self):
        p1 = Main(self.driver)
        p1.login(Users.PROBLEM, Password.VALID)
        p2 = AllProducts(self.driver)
        expected = ProductsImages.BACKPACK
        actual = p2.image_source(Products.BACKPACK)
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
