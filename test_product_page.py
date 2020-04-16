from .pages.locators import Links
from .pages.product_page import ProductPage
import pytest
import time


#@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                  pytest.param(7, marks=pytest.mark.xfail),
#                                  8, 9])

#def test_guest_can_add_product_to_basket(browser, link):
#    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#    page = ProductPage(browser, url)
#    page.open()
#    page.press_button_add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.should_be_message_about_adding()
#    page.should_be_message_basket_total()
# тест с проверками сообщений об успешном добавлении и сообщении того, что именно эта книга была добавлена

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Links.PRODUCT_LINK_CLEAN
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Links.PRODUCT_LINK_CLEAN)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.PRODUCT_LINK_CLEAN)
    page.open()
    page.press_button_add_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.should_message_to_disappeared()

# pytest -v --tb=line test_product_page.py