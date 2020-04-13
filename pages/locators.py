from selenium.webdriver.common.by import By


class Links():
    LINK_URL = "http://selenium1py.pythonanywhere.com/"
    LINK_LOGIN = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    #NAME_MAIN = (text The shellcoder's handbook)
    #NAME_ALERT = (<div class="alertinner "> <strong>The shellcoder's handbook</strong> был добавлен в вашу корзину.)
    #PRICE_VALUE_MAIN = (class= price-color + value 9,99 £)
    #PRICE_ALERT = (<strong>9,99&nbsp;£</strong>)