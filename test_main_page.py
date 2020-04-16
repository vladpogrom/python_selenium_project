from .pages.main_page import MainPage
from .pages.locators import Links
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.xfail(run=False)
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, Links.LINK_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.xfail(run=False)
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, Links.LINK_URL)
    page.open()
    page.should_be_login_link()


def test_guest_can_see_empty_basket_opened_from_product_page(browser):
    page = BasketPage(browser, Links.LINK_URL)
    page.open()
    page.go_to_basket_page()
    page.basket_are_empty()
    page.text_about_basket_is_empty()


def test_guest_can_see_full_basket_opened_from_product_page(browser):
    page = BasketPage(browser, Links.LINK_URL)
    page.open()
    page.go_to_basket_page()
    page.basket_are_not_empty()
    page.text_about_basket_is_not_empty()

