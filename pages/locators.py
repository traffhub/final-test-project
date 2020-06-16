from selenium.webdriver.common.by import By



class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner  p")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner p a")
    PRODUCT_IN_BASKET_COL = (By.CSS_SELECTOR, "//*[@id='content_inner']/div[1]/div/h2")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form button")
class AddToBasket():
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] p[class='price_color']")
    BASKET_NAME = (By.XPATH,"//*[@id='messages']/div[3]/div/p[1]/strong")
    BASKET_PRICE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-info']")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
