import time
import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link_part = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-robot-novels_25/"


@pytest.mark.parametrize('link', [link_part + "0", link_part + "1", link_part + "2", link_part + "3", link_part + "4",
                                  link_part + "5", link_part + "6",
                                  pytest.param(link_part + "7", marks=pytest.mark.xfail),
                                  link_part + "8", link_part + "9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    book_name = page.get_name_of_book()
    book_cost = page.get_cost_of_book()
    page.check_cost_basket(book_cost)
    page.check_name_of_book(book_name)


@pytest.mark.skip(reason="this is fail test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="this is fail test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_alert_about_empty_basket()
    basket_page.should_not_be_product_in_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "12ewq"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        book_name = page.get_name_of_book()
        book_cost = page.get_cost_of_book()
        page.check_cost_basket(book_cost)
        page.check_name_of_book(book_name)
