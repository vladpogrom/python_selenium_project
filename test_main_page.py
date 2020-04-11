from .pages.main_page import MainPage
from .pages.locators import Links


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, Links.LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, Links.LINK)
    page.open()
    page.should_be_login_link()