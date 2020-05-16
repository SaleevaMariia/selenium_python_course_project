from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            "There is no button to add book to basket"
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()

    def get_name_of_book(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def get_cost_of_book(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_COST).text

    def check_cost_basket(self, book_cost):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_COST), \
            "There is no message about basket sum"
        cost_text = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_COST).text
        assert cost_text == book_cost, "Wrong sum of basket"

    def check_name_of_book(self, book_name):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_BOOK_ADD_SUCCESS), "There is no message about book name"
        name_text = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_ADD_SUCCESS).text
        assert name_text == book_name, "Wrong book in the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK_ADD_SUCCESS), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_BOOK_ADD_SUCCESS), \
            "Something isn't disappeared, but should"
