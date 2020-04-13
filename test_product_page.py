from .pages.locators import Links
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, Links.PRODUCT_LINK)
    page.open()
    page.add_to_basket()
    time.sleep(2)