from .base_page import BasePage, solve_quiz_and_get_code
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        button_1 = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button_1.click()
        solve_quiz_and_get_code(self)
        time.sleep(60)
        #найти локатор названия книги на главной
        #найти локатор названия книги после добавления
        #найти локатор цены книги на главной
        #найти локатор цены книги после добавления
        #добавить ассерт на цену книги в проверку
        #добавить ассерт на название книги в проверку




