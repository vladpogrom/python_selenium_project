from selenium.webdriver.common.by import By


class Links():
    LINK_MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    LINK_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/accounts/login/"
    PRODUCT_LINK_OFFER = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    PRODUCT_LINK_CLEAN = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    LINK_FOR_TEST = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FORM_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn-block")