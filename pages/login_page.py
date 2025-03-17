from .base_page import BasePage
from .locators import LoginPageLocators
import faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.go_to_login_page()

        WebDriverWait(self.browser, 20).until(
        EC.element_to_be_clickable((LoginPageLocators.REGISTRATION_EMAIL_LINK))).send_keys(email)

        password_input = WebDriverWait(self.browser, 20).until(
        EC.element_to_be_clickable((LoginPageLocators.REGISTRATION_PASSWORD_LINK)))
        password_input.send_keys(password)

        password_repeat_input = WebDriverWait(self.browser, 20).until(
        EC.element_to_be_clickable((LoginPageLocators.REGISTRATION_REPEATED_PASSWORD_LINK)))
        password_repeat_input.send_keys(password)

        registration_button = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable((LoginPageLocators.REGISTRATION_SUBMIT_LINK)))
        registration_button.click()

    def registration(self):
        fake_data = faker.Faker()
        email = fake_data.email()
        password = fake_data.password(10)
        self.register_new_user(str(email), str(password))

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_string = "login"
        url_string = self.browser.current_url
        index = url_string.find(login_string)
        assert index != -1, f"expected '{login_string}' to be substring of '{url_string}'" # "login" in browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_LINK), "Register form is not presented"
