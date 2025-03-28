from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket_link = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_BUTTON_ADD_TO_BASKET_LINK)
        button_add_to_basket_link.click()

    def added_product_name_is_name_on_product_page(self):
        message_book_name = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BOOK_NAME)
        book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME)
        assert book_name.text == message_book_name.text, "Название в сообщении не совпадает с добавленным товаром"

    def added_product_price_is_price_on_product_page(self):
        message_book_price = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BOOK_PRICE)
        product_price = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE)
        assert product_price.text == message_book_price.text, "Цена не совпадает с ценой на странице товара"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK_NAME), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_BOOK_NAME), \
            "Success message is presented, but should disappear"



