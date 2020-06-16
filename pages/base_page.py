from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, MainPageLocators


class BasePage():
    def __init__(self,browser,url,timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def is_element_presented(self,how,what):
        try:
            self.browser.find_element(how,what)
        except(NoSuchElementException):
            return False
        return True
    def go_to_baslet(self):
        self.click_element(*MainPageLocators.VIEW_BASKET_BUTTON)
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()
    def should_be_login_link(self):
        assert self.is_element_presented(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def click_element(self,how,what):
        try:
            self.browser.find_element(how,what)
        except(NoSuchElementException):
            return False
        return self.browser.find_element(how, what).click()
    def get_element_text(self,how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return self.browser.find_element(how, what).text
    def wait_for_element(self, how, what, timeout=5):
        WebDriverWait(self.browser, timeout, 1).until(
        EC.element_to_be_clickable((how, what))
        )

    def is_element_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    def send_keys_element(self,how,what,text):
        try:
            self.browser.find_element(how,what)
        except(NoSuchElementException):
            return False
        return self.browser.find_element(how, what).send_keys(text)

    def should_be_authorized_user(self):
        assert self.is_element_presented(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

