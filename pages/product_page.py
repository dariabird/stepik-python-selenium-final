from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_LABEL_COLOR).text

    def get_item_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_basket_total(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_LABEL).text

    def should_be_message_about_adding_to_cart(self):
        messages = self.browser.find_elements(*ProductPageLocators.STATUS_MESSAGES)
        assert self.get_item_title() in messages[0].text

    def should_be_equal_price_and_total(self):
        assert self.get_item_price() in self.get_basket_total()
