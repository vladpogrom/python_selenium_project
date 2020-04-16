from selenium.webdriver.common.by import By
from selenium import webdriver


class Links():
    LINK_URL = "http://selenium1py.pythonanywhere.com/"
    LINK_LOGIN = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    PRODUCT_LINK_1 = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_LINK_2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    PRODUCT_LINK_OFFER = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    PRODUCT_LINK_CLEAN = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")