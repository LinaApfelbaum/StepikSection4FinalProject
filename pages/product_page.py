from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_the_same_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        confirmation_bar = self.browser.find_element(
            *ProductPageLocators.CONFIRMATION_BAR_PRODUCT_NAME).text

        assert self.is_element_present(
            *ProductPageLocators.CONFIRMATION_BAR_PRODUCT_NAME), \
            "No confirmation bar"
        assert product_name == confirmation_bar, \
            f"{product_name} is not equal to product in {confirmation_bar}"

    def should_be_the_same_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        basket_price_bar = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_BAR).text

        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRICE_BAR), "No basket price bar"
        assert product_price == basket_price_bar, \
            f"{product_price} is not equal to price in {basket_price_bar}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.CONFIRMATION_BAR_PRODUCT_NAME) == True, \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.CONFIRMATION_BAR_PRODUCT_NAME) == True, \
            "Success message hasn't disappeared but it should"
