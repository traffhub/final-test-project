from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_product_in_basket(self):
        print('check basket for products...')
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_COL), 'Basket is not empty.'
    def should_not_product_in_basket_text(self):
        print('get empy text...')
        assert self.is_element_presented(*BasketPageLocators.EMPTY_BASKET_TEXT), 'Cant Find Basket Text.'
