from .pages.locators import Links
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, Links.PRODUCT_LINK)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()