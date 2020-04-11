from selenium.webdriver.common.by import By


class Links():
    LINK_URL = "http://selenium1py.pythonanywhere.com/"
    LINK_LOGIN = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")