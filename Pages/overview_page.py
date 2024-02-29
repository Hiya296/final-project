import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class Overview(BasePage):
    TITLE_TEXT = (By.CSS_SELECTOR, ".title")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    FINISH = (By.CSS_SELECTOR, "#finish")
    CANCEL = (By.CSS_SELECTOR, "#cancel")

    def __init__(self, driver):
        super().__init__(driver)

    def title(self):
        return self.get_text(self.TITLE_TEXT)

    @allure.step("Finish purchase")
    def finish_purchase(self):
        self.click(self.FINISH)

    @allure.step("Cancel purchase")
    def cancel_purchase(self):
        self.click(self.CANCEL)
