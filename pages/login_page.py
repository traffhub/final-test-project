from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'No \'Login\' in Url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), 'No Login Form Here Idiot'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM), 'No Registration Form Idiot'
    def register_new_user(self,email,password):
        self.send_keys_element(*LoginPageLocators.EMAIL_FORM,email)
        self.send_keys_element(*LoginPageLocators.PASSWORD_FORM,password)
        self.send_keys_element(*LoginPageLocators.REPEAT_PASSWORD_FORM,password)
        self.click_element(*LoginPageLocators.REGISTRATION_BUTTON)
    def goto_registration_link(self):
        self.click_element(*MainPageLocators.REGISTRATION_FORM)