from .base_page import BasePage
from pages.locators import AddToBasket
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class BasketPage(BasePage):
    def add_product_to_basket(self):
        self.click_element(*AddToBasket.BASKET_BUTTON)
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def get_product_info(self):
        self.wait_for_element(*AddToBasket.PRODUCT_PRICE,10)
        self.product_price = self.get_element_text(*AddToBasket.PRODUCT_PRICE)
        self.product_name = self.get_element_text(*AddToBasket.PRODUCT_NAME)
        print(f"Product Name = {self.product_name}. Product Price = {self.product_price}")
    def get_basket_info(self):
        self.wait_for_element(*AddToBasket.BASKET_PRICE,10)
        self.basket_name = self.get_element_text(*AddToBasket.BASKET_PRICE)
        self.basket_price = self.get_element_text(*AddToBasket.BASKET_NAME)
        print(f"Basket Name={self.basket_name}. Basket Price = {self.basket_price}")
    def check_product_in_basket(self):
        assert self.product_name == self.basket_name, f"Product Name Are Not Equal Basket Name, {self.product_name} != {self.basket_name}"
        assert self.product_price == self.basket_price, f"Product Price Are Not Equal Basket Name, {self.product_price} != {self.basket_price}"
        return print('Your product successfully add to basket')
    def clear_basket(self):
        pass

    def should_not_be_success_message(self):
        print('should_not_be_success_message check...')
        assert self.is_element_disappeared(*AddToBasket.BASKET_NAME,4), "Success message is not presented"

    def should_not_be_success_message1(self):
        assert self.is_not_element_present(*AddToBasket.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def view_basket(self):

        self.click_element(*AddToBasket.VIEW_BASKET_BUTTON)
