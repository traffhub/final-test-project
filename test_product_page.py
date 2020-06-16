import time
import pytest
from pages.product_page import BasketPage
from pages.login_page import LoginPage



@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    print('OPEN THIS LINK...')
    page = BasketPage(browser,link)
    page.open()
    page.get_product_info()
    page.should_not_be_success_message()
    page.add_product_to_basket()
    time.sleep(1)
    # page.solve_quiz_and_get_code()
    time.sleep(1)
    page.view_basket()
    time.sleep(5)
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    print('OPEN THIS LINK...')
    page = BasketPage(browser, link)
    page.open()
    time.sleep(6)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    time.sleep(10)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    print('OPEN THIS LINK...')
    page = BasketPage(browser, link)
    page.open()
    time.sleep(6)
    page.should_not_be_success_message1()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    print('OPEN THIS LINK...')
    page = BasketPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    basket = BasketPage(browser,link)
    basket.open()
    basket.go_to_baslet()
    basket.should_not_be_success_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, link)
        page.open()
        time.sleep(5)
        page.goto_registration_link()
        time.sleep(5)
        page.register_new_user(email,email)
        time.sleep(5)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        print('OPEN THIS LINK...')
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = BasketPage(browser, link)
        page.open()
        time.sleep(6)
        page.should_not_be_success_message1()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        print('OPEN THIS LINK...')
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = BasketPage(browser, link)
        page.open()
        page.get_product_info()
        page.should_not_be_success_message()
        page.add_product_to_basket()
        time.sleep(1)
        page.view_basket()
        time.sleep(5)
        page.should_not_be_success_message()

