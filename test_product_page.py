from pages.main_page import MainPage
from pages.locators import AddToBasket
from pages.product_page import BasketPage
import time
import pytest

src = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer"
promo_list =[f"{i}" for i in range(1)]
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# @pytest.mark.parametrize("offer", promo_list)
# def test_guest_can_add_item_to_basket(browser,offer):
#     link = f"{src}{offer}"
#     print('OPEN THIS LINK...')
#     page = BasketPage(browser,link)
#     page.open()
#     page.get_product_info()
#     page.should_not_be_success_message()
#     page.add_product_to_basket()
#     time.sleep(1)
#     page.solve_quiz_and_get_code()
#     time.sleep(1)
#     page.view_basket()
#     time.sleep(5)
#     page.should_not_be_success_message()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,offer):
#     link = f"{src}{offer}"
#     print('OPEN THIS LINK...')
#     page = BasketPage(browser, link)
#     page.open()
#     time.sleep(6)
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message1()
#     time.sleep(10)
#
# @pytest.mark.parametrize("offer", promo_list)
# def test_guest_cant_see_success_message(browser,offer):
#     link = f"{src}{offer}"
#     print('OPEN THIS LINK...')
#     page = BasketPage(browser, link)
#     page.open()
#     time.sleep(6)
#     page.should_not_be_success_message1()
#
# def test_message_disappeared_after_adding_product_to_basket(browser,offer):
#     link = f"{src}{offer}"
#     print('OPEN THIS LINK...')
#     page = BasketPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_login_link()
