import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Complete(BasePage):
    TITLE_TEXT = (By.CSS_SELECTOR, ".title")
    BACK_HOME = (By.CSS_SELECTOR, "[id*='back']")

    def __init__(self, driver):
        super().__init__(driver)

    def title(self):
        return self.get_text(self.TITLE_TEXT)

    def go_back(self):
        self.click(self.BACK_HOME)
