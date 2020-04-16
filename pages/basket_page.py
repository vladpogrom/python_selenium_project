from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_are_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Basket have any product, but dont"

    def basket_are_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Basket are empty, but dont"

    def text_about_basket_is_empty(self):
        text_for_check = "Your basket is empty"
        text_from_basket = self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET).text
        assert text_for_check in text_from_basket, "Basket are not empty"

    def text_about_basket_is_not_empty(self):
        text_for_check = "Your basket is empty"
        text_from_basket = self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET).text
        assert not text_for_check in text_from_basket, "Basket are empty"