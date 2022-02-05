from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "Is not login link"

    def should_be_login_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM), \
            "Page doesn't contain login form"

    def should_be_register_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM), \
            "Page doesn't contain register form"

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()