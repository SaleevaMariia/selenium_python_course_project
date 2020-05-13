import pytest

from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('link', [link + "0", link + "1", link + "2", link + "3", link + "4",
                                  link + "5", link + "6", pytest.param(link + "7", marks=pytest.mark.xfail),
                                  link + "8", link + "9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    book_name = page.get_name_of_book()
    book_cost = page.get_cost_of_book()
    page.check_cost_basket(book_cost)
    page.check_name_of_book(book_name)
