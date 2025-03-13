from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_PAGE_BUTTON_ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")

    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")

    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")