from .pages.locators import Links
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])

@pytest.mark.xfail(run=False)
def test_guest_can_add_product_to_basket(browser, link):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, url)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
# тест с проверками сообщений об успешном добавлении и сообщении того, что именно эта книга была добавлена

@pytest.mark.xfail(run=False)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Links.PRODUCT_LINK_CLEAN
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail(run=False)
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Links.PRODUCT_LINK_CLEAN)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(run=False)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.PRODUCT_LINK_CLEAN)
    page.open()
    page.press_button_add_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.should_message_to_disappeared()

@pytest.mark.xfail(run=False)
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Links.LINK_FOR_TEST)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(run=False)
def test_guest_can_go_to_login_page_from_product_page (browser):
    page = ProductPage(browser, Links.LINK_FOR_TEST)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(run=False)
def test_guest_can_see_empty_basket_opened_from_product_page(browser):
    page = BasketPage(browser, Links.PRODUCT_LINK_CLEAN)
    page.open()
    page.go_to_basket_page()
    page.basket_are_empty()
    page.text_about_basket_is_empty()

@pytest.mark.xfail(run=False)
def test_guest_can_see_full_basket_opened_from_product_page(browser):
    page = BasketPage(browser, Links.PRODUCT_LINK_CLEAN)
    page.open()
    page.go_to_basket_page()
    page.basket_are_not_empty()
    page.text_about_basket_is_not_empty ()

@pytest.mark.test_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "123qwe"
        page = LoginPage(browser, Links.LINK_URL)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, Links.PRODUCT_LINK_CLEAN)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, Links.PRODUCT_LINK_CLEAN)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

# pytest -v --tb=line test_product_page.py