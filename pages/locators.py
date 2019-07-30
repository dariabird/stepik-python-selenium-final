from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_LABEL_COLOR = (By.CSS_SELECTOR, ".product_main .price_color")
    STATUS_MESSAGES = (By.CSS_SELECTOR, "#messages")
    #SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")
    BASKET_TOTAL_LABEL = (By.CSS_SELECTOR, ".basket-mini")
