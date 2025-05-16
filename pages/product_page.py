from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")

    def add_product_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BTN).click()

    def should_be_added_to_basket(self, expected_name):
        actual_name = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert actual_name == expected_name, \
            f"Expected product name '{expected_name}', got '{actual_name}'"

    def should_be_correct_price_in_basket(self, expected_price):
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert expected_price in basket_total, \
            f"Expected price '{expected_price}' in basket total, got '{basket_total}'"
    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text