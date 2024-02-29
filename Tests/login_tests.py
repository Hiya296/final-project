import allure
from allure_commons.types import *
from Pages.home_page import Main
from Pages.all_products_page import AllProducts
from External.data import *


@allure.severity(Severity.CRITICAL)
@allure.epic("Security")
@allure.feature("Login options")
class Tests:

    @allure.description("Logging in with valid user name and password")
    @allure.title("2 - Valid login")
    @allure.story("As a user I want to login after entering valid credentials")
    def test_valid_login(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.VALID)
        p2 = AllProducts(self.driver)
        expected = PagesTitle.PRODUCTS_PAGE
        actual = p2.page_title_text()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.description("Logging in with invalid user name")
    @allure.title("3 - Invalid user name login")
    @allure.story("As a user I want to see a failure login after entering invalid user name")
    def test_invalid_username(self):
        p1 = Main(self.driver)
        p1.login(Users.INVALID, Password.VALID)
        expected = ErrorMsgs.NO_MATCH
        actual = p1.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.description("Logging in with invalid password")
    @allure.title("4 - Invalid password login")
    @allure.story("As a user I want to see a failure login after entering invalid password")
    def test_invalid_password(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, Password.INVALID)
        expected = ErrorMsgs.NO_MATCH
        actual = p1.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.description("Logging in without user name")
    @allure.title("5 - Login without user name")
    @allure.story("As a user I want to see a failure login after entering only password")
    def test_no_username(self):
        p1 = Main(self.driver)
        p1.login("", Password.VALID)
        expected = ErrorMsgs.NO_USER
        actual = p1.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.description("Logging in without password")
    @allure.title("6 - Login without password")
    @allure.story("As a user I want to see a failure login after entering only user name")
    def test_no_password(self):
        p1 = Main(self.driver)
        p1.login(Users.STANDARD, "")
        expected = ErrorMsgs.NO_PASSWORD
        actual = p1.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")

    @allure.description("Logging to locked out user")
    @allure.title("7 - Locked out user login")
    @allure.story("As a user I want to see a failure when login to locked out user")
    def test_locked_out_user(self):
        p1 = Main(self.driver)
        p1.login(Users.LOCKED, Password.VALID)
        expected = ErrorMsgs.LOCKED_OUT
        actual = p1.error_message()
        assert expected == actual
        allure.attach(expected, "Expected")
        allure.attach(actual, "Actual")
