from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_BOOK_ADD_SUCCESS = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    MESSAGE_BASKET_COST = (By.CSS_SELECTOR, ".alert-info>.alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_COST = (By.CSS_SELECTOR, ".product_main p.price_color")

