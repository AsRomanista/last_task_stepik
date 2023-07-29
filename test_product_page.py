# test_product_page.py
import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Bug in the system')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear&promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_basket_total_message()
    page.should_be_correct_product_name()
    page.should_be_correct_basket_total()
