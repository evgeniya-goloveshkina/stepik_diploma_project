from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS_LINK = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, ".content div#content_inner p a")


class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WELCOME_LINK = (By.CSS_SELECTOR, ".well-blank")


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEATED_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    PRODUCT_PAGE_BUTTON_ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")

    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")

    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")