import time

from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def fill_text(self, locator, text: str):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        time.sleep(1)
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def lists(self, locator, name):
        items = self.driver.find_elements(*locator)
        for item in items:
            if item.text == name:
                item.click()
                break

    def image_attribute(self, locator, alt_value):
        images = self.driver.find_elements(*locator)
        for image in images:
            if image.get_attribute("alt") == alt_value:
                src_value = image.get_attribute("src")
                return src_value

    def click_on_add(self, locator, id_value):
        buttons = self.driver.find_elements(*locator)
        for button in buttons:
            if button.get_attribute("id").__contains__(id_value):
                button.click()
                break
