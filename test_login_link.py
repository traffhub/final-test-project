from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/accounts/login/"

def test_login(browser):
    page = LoginPage(browser,link)
    page.open()
    page.should_be_login_page()
