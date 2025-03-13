from .pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.locators import *
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.added_product_name_is_name_on_product_page()
    page.added_product_price_is_price_on_product_page()
