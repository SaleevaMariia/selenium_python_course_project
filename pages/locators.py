from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_BOOK_ADD_SUCCESS = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    MESSAGE_BASKET_COST = (By.CSS_SELECTOR, ".alert-info>.alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_COST = (By.CSS_SELECTOR, ".product_main p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ELEMENTS = (By.CSS_SELECTOR, ".basket-items")
