from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators, MainPageLocators

class BasketPage(BasePage):
    def go_to_main_page_by_message_link(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_LINK)
        link.click()

    def should_be_message_about_empty_basket(self):
        self.go_to_main_page_by_message_link()
        assert self.is_element_present(*MainPageLocators.WELCOME_LINK), "No message about empty basket"

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LINK), "Goods should not be in basket"
