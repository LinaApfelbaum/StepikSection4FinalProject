from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD_FIELD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CONFIRMATION_BAR_PRODUCT_NAME = (
        By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    BASKET_PRICE_BAR = (
        By.CSS_SELECTOR, "#messages :nth-child(3) .alertinner strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS_BAR = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_BAR = (By.CSS_SELECTOR, "#content_inner > p")
