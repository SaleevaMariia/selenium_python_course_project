from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_alert_about_empty_basket(self):
        # проверяем, что есть сообщение о том, что карзина пуста
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "Basket is not alert about empty basket"

    def should_not_be_product_in_basket(self):
        # проверяем, что в карзине нет продуктов
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENTS), "Basket is not empty"
