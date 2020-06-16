from pages.main_page import MainPage
from pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        page = MainPage(browser,link)
        page.open()
        page.go_to_login_page()
    def test_guest_should_see_login_link(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    basket = BasketPage(browser,link)
    basket.open()
    basket.go_to_baslet()
    basket.should_not_product_in_basket()
    basket.should_not_product_in_basket_text()
